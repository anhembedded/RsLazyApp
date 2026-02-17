from abc import abstractmethod
from utility.log import Logger_T, logging
from viewModels.viewModel_abstract import viewModel_abstract_T
from viewModels.viewModel import viewModel_T
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMainWindow

class view_abstract_T(QObject):
    def __init__(self):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [ViewAbstract_T]", level=logging.INFO)
        self.viewModel : viewModel_abstract_T = viewModel_T()

    @abstractmethod
    def run(self):
        pass