from PySide6.QtCore import QObject, Signal, Slot
from utility.log import Logger_T, logging
from viewModels.viewModel_abstract import viewModel_abstract_T

class model_abstract_T(QObject):
    def __init__(self, viewModel : viewModel_abstract_T):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [model_abstract_T]", level=logging.INFO)
        self.viewModel : viewModel_abstract_T = viewModel

    def task_buttonClicked(self):
        self.__log.log(message="task_buttonClicked", level=logging.INFO)