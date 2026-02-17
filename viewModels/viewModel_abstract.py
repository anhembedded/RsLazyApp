from utility.log import Logger_T, logging
from PySide6.QtCore import Signal, QObject, Slot,QThread
from models.model import model_T


class viewModel_abstract_T(QObject):  # Inherit from QObject
    buttonClicked = Signal()  # Corrected signal name (camelCase convention)
    taskResult = Signal(str)
    def __init__(self):
        super().__init__()  # Initialize QObject
        self.__log = Logger_T()
        self.__log.log(message="Initializing [ViewModelAbstract_T]", level=logging.INFO)
        self.model = model_T()
        self.modelThread = QThread()
        self.model.moveToThread(self.modelThread)
        self.modelThread.start()

        self.buttonClicked.connect(self.model.task_buttonClicked)
        self.model.taskResult.connect(self.on_task_result)

    @Slot(str)
    def on_task_result(self, result):
        self.taskResult.emit(result)

    def cleanup(self):
        """Safely stop the model thread."""
        self.__log.log(message="Cleaning up [ViewModelAbstract_T]", level=logging.INFO)
        if hasattr(self, 'modelThread') and self.modelThread.isRunning():
            self.modelThread.quit()
            self.modelThread.wait()


