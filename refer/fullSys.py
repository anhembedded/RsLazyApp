import sys
import time
from queue import Queue
from threading import Thread

from PySide6.QtCore import QObject, Signal, Slot, QThread, QTimer
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget, QLabel, QTextEdit)


class TaskItem:
    def __init__(self, action: str, data: any):
        self.action = action
        self.data = data

class ResultObject:
    def __init__(self, result_data: any):
        self.result_data = result_data

class ErrorObject:
    def __init__(self, exception: Exception, message: str):
        self.exception = exception
        self.message = message

class Worker(QObject):
    task_completed = Signal(ResultObject)
    task_error = Signal(ErrorObject)
    finished = Signal()

    def __init__(self, task_queue: Queue):
        super().__init__()
        self._task_queue = task_queue

    @Slot()
    def process_tasks(self):
        while True:
            try:
                task: TaskItem = self._task_queue.get()  # Blocks until a task is available
                if task is None: # Poison Pill
                    break
                result = self.process_task(task)
                self.task_completed.emit(result)
            except Exception as e:
                self.task_error.emit(ErrorObject(e, "Error processing task"))
        self.finished.emit()

    def process_task(self, task: TaskItem) -> ResultObject:
        # Simulate a long-running task
        if task.action == "long_task":
            time.sleep(5)  # Simulate work
            return ResultObject(f"Processed: {task.data}")
        elif task.action == "error_task":
            raise ValueError("Intentional Error")
        else:
            return ResultObject(f"Unknown action: {task.action}")

class Model(QObject):
    task_completed = Signal(ResultObject)
    task_error = Signal(ErrorObject)

    def __init__(self):
        super().__init__()
        self._task_queue = Queue()
        self._consumer_thread = QThread()
        self._worker = Worker(self._task_queue)
        self._worker.moveToThread(self._consumer_thread)
        self._consumer_thread.started.connect(self._worker.process_tasks)
        self._worker.task_completed.connect(self.on_task_completed)
        self._worker.task_error.connect(self.on_task_error)
        self._worker.finished.connect(self._consumer_thread.quit)
        self._consumer_thread.start() #start thread

    def process_user_action_async(self, action: str, data: any):
        # In a real application, this would create a TaskItem
        # based on the action and data.  For simplicity,
        # we just create a simple task here.
        task = TaskItem(action, data)
        self.enqueue_task(task)

    def enqueue_task(self, task: TaskItem):
        self._task_queue.put(task)

    @Slot(ResultObject)
    def on_task_completed(self, result: ResultObject):
        self.task_completed.emit(result)


    @Slot(ErrorObject)
    def on_task_error(self, error: ErrorObject):
        self.task_error.emit(error)

    def stop(self):
        # Add poison pill to stop
        self.enqueue_task(None)
        self._consumer_thread.wait() #wait finish

class ViewModel(QObject):
    data_changed = Signal(str)
    error_occurred = Signal(str)

    def __init__(self, model: Model):
        super().__init__()
        self._model = model
        self._data = "Initial Data"
        self._model.task_completed.connect(self.update_data)
        self._model.task_error.connect(self.show_error)


    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value:str):
        self._data = value
        self.data_changed.emit(self._data)

    @Slot(str, str)
    def handle_user_action(self, action: str, data:str):
        self._model.process_user_action_async(action, data)

    @Slot(ResultObject)
    def update_data(self, result: ResultObject):
        self.data = result.result_data


    @Slot(ErrorObject)
    def show_error(self, error: ErrorObject):
        self.error_occurred.emit(f"Error: {error.message}\n{error.exception}")


class View(QMainWindow):
    user_action = Signal(str, str)

    def __init__(self, view_model: ViewModel):
        super().__init__()
        self._view_model = view_model
        self.setWindowTitle("MVVM Example")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel(self._view_model.data)
        self.layout.addWidget(self.label)

        self.button_long_task = QPushButton("Start Long Task")
        self.button_long_task.clicked.connect(self.on_long_task_clicked)
        self.layout.addWidget(self.button_long_task)

        self.button_error_task = QPushButton("Start Error Task")
        self.button_error_task.clicked.connect(self.on_error_task_clicked)
        self.layout.addWidget(self.button_error_task)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)


        self._view_model.data_changed.connect(self.display_data)
        self._view_model.error_occurred.connect(self.display_error)

    @Slot(str)
    def display_data(self, data: str):
        self.label.setText(data)

    @Slot(str)
    def display_error(self, message: str):
        self.text_edit.append(message)

    def on_long_task_clicked(self):
        self.user_action.emit("long_task", "Some Data")

    def on_error_task_clicked(self):
        self.user_action.emit("error_task", "Error Data")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = Model()
    view_model = ViewModel(model)
    view = View(view_model)

    #connect singal user_action to handle_user_action method of ViewModel.
    view.user_action.connect(view_model.handle_user_action)
    view.show()

    try:
        sys.exit(app.exec())
    finally:
        model.stop()