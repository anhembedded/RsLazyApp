import sys
from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

# Message Objects (for data transfer)
class MessageObject:
    def __init__(self, data):
        self.data = data

class ResultObject:
    def __init__(self, result):
        self.result = result

# Model (Sub Thread)
class Model(QObject):
    taskFinished = Signal(ResultObject)

    def __init__(self):
        super().__init__()

    def processData(self, message):
        # Simulate long-running task
        import time
        time.sleep(2)  # Simulate work
        result = message.data * 2
        self.taskFinished.emit(ResultObject(result))

# ViewModel (Main Thread)
class ViewModel(QObject):
    updateUI = Signal(ResultObject)

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.taskFinished.connect(self.dataProcessed)

    def requestTaskProcessing(self, message):
        self.model.processData(message)

    @Slot(ResultObject)
    def dataProcessed(self, result):
        self.updateUI.emit(result)

# View (Main Thread)
class View(QMainWindow):
    def __init__(self, viewModel):
        super().__init__()
        self.viewModel = viewModel
        self.initUI()
        self.viewModel.updateUI.connect(self.updateLabel)

    def initUI(self):
        self.setWindowTitle("PySide6 MVVM Threaded")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.button = QPushButton("Process Data")
        self.button.clicked.connect(self.onButtonClicked)
        self.layout.addWidget(self.button)

        self.label = QPushButton("Result: ")
        self.label.setEnabled(False)
        self.layout.addWidget(self.label)

    def onButtonClicked(self):
        self.viewModel.requestTaskProcessing(MessageObject(10))

    @Slot(ResultObject)
    def updateLabel(self, result):
        self.label.setText(f"Result: {result.result}")

# Application
class lazyApp_T(QObject):
    def __init__(self):
        super().__init__()
        self.model_thread = QThread()
        self.model = Model()
        self.model.moveToThread(self.model_thread)
        self.model_thread.start()
        self.viewModel = ViewModel(self.model)
        self.view = View(self.viewModel)

    def run(self):
        self.view.show()

    def close(self):
        self.model_thread.quit()
        self.model_thread.wait()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lazy_app = lazyApp_T()
    lazy_app.run()
    sys.exit(app.exec())
    lazy_app.close() #Close threads.