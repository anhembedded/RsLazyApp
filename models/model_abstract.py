from PySide6.QtCore import QObject, Signal, Slot
from utility.log import Logger_T, logging
from viewModels.viewModel_abstract import viewModel_abstract_T  # Assuming this exists
import time  # Import the time module


class model_abstract_T(QObject):
    taskCompleted = Signal()
    taskCompletedError = Signal(int)

    def __init__(self, viewModel: viewModel_abstract_T):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [model_abstract_T]", level=logging.INFO)
        self.viewModel: viewModel_abstract_T = viewModel
        self.__counter = 0

    def task_buttonClicked(self):
        self.__log.log(message="task_buttonClicked", level=logging.INFO)
        self.__log.log(message="Simulating delay for 1.5 seconds", level=logging.DEBUG)
        self.__counter += 1
        time.sleep(1.5)  # BLOCKING DELAY
        self.__log.log(message="Task completed", level=logging.INFO)
        print("Task completed")
        self.taskCompleted.emit()
        self.taskCompletedError.emit(self.__counter)