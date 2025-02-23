import sys
import time
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget, QLabel, QProgressBar)
from PySide6.QtCore import QObject, Signal, Slot, QTimer, QThread

# --- Model ---
class Model(QObject):
    taskStarted = Signal()
    taskProgress = Signal(int)
    taskCompleted = Signal(str)  # Pass a result string

    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.duration = 0
        self.progress_interval = 0
        self.current_progress = 0

    @Slot()  # Slot to start the task (triggered by ViewModel)
    def start_task(self):
        print("Model: Task started")
        self.duration = 3000  # Simulate a 3-second task
        self.progress_interval = 100
        self.current_progress = 0
        self.timer.setInterval(self.progress_interval)
        self.timer.start()
        self.taskStarted.emit()

    @Slot()
    def update_progress(self):
        self.current_progress += self.progress_interval
        if self.current_progress >= self.duration:
            self.timer.stop()
            print("Model: Task completed")
            self.taskCompleted.emit("Task Result: Success!")  # Emit result
        else:
            percentage = int((self.current_progress / self.duration) * 100)
            print(f"Model: Task progress: {percentage}%")
            self.taskProgress.emit(percentage)

    @Slot()
    def stop_task(self): #Added stop task
        if self.timer.isActive():
          self.timer.stop()
          print("Model: Task stop")

# --- ViewModel ---
class ViewModel(QObject):
    startTaskSignal = Signal()  # Signal to tell Model to start
    taskStarted = Signal()     # Relay Model's signals
    taskProgress = Signal(int)
    taskCompleted = Signal(str)

    def __init__(self):
        super().__init__()

        # --- Thread and Model setup ---
        self.model_thread = QThread()
        self.model = Model()
        self.model.moveToThread(self.model_thread) # Move to sub thread

        # --- Connections ---
        # Connect View's signal to ViewModel's slot
        self.startTaskSignal.connect(self.model.start_task)

        # Connect Model's signals to ViewModel's slots (and relay)
        self.model.taskStarted.connect(self.on_task_started)
        self.model.taskProgress.connect(self.on_task_progress)
        self.model.taskCompleted.connect(self.on_task_completed)

        # --- Thread Management ---
        # Quit the thread when the model finishes
        self.model.taskCompleted.connect(self.model_thread.quit)
        # Clean up thread after it's finished. VERY IMPORTANT
        self.model_thread.finished.connect(self.model_thread.deleteLater)
        # Clean up model after thread finish
        self.model_thread.finished.connect(self.model.deleteLater)


        self.model_thread.start() # Start Model thread.

    @Slot()
    def on_task_started(self):
        print("ViewModel: Task started")
        self.taskStarted.emit()

    @Slot(int)
    def on_task_progress(self, percentage):
        print(f"ViewModel: Task progress: {percentage}%")
        self.taskProgress.emit(percentage)

    @Slot(str)
    def on_task_completed(self, result_string):
        print(f"ViewModel: Task completed: {result_string}")
        self.taskCompleted.emit(result_string)



# --- View ---
class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.viewModel = ViewModel()  # Create ViewModel instance
        self.setWindowTitle("MVVM Threading Example")

        self.button = QPushButton("Start Task")
        self.progress_label = QLabel("Progress: 0%")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.result_label = QLabel("Result: ")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.result_label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # --- Connect View to ViewModel ---
        self.button.clicked.connect(self.on_button_clicked)
        self.viewModel.taskStarted.connect(self.on_task_started)
        self.viewModel.taskProgress.connect(self.on_task_progress)
        self.viewModel.taskCompleted.connect(self.on_task_completed)

    @Slot()
    def on_button_clicked(self):
        print("View: Button clicked, starting task...")
        self.button.setEnabled(False)  # Disable button during task
        self.viewModel.startTaskSignal.emit() # Emit signal to View Model

    @Slot()
    def on_task_started(self):
        self.progress_label.setText("Progress: 0%")
        self.progress_bar.setValue(0)
        self.result_label.setText("Result: ")

    @Slot(int)
    def on_task_progress(self, percentage):
        self.progress_label.setText(f"Progress: {percentage}%")
        self.progress_bar.setValue(percentage)

    @Slot(str)
    def on_task_completed(self, result_string):
        self.progress_label.setText("Progress: 100%")
        self.progress_bar.setValue(100)
        self.result_label.setText(f"Result: {result_string}")
        self.button.setEnabled(True)  # Re-enable button

# --- Main Application ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(app.exec())