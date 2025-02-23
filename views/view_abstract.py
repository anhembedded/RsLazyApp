from abc import abstractmethod
from utility.log import Logger_T, logging
from viewModels.viewModel_abstract import viewModel_abstract_T

class view_abstract_T:
    def __init__(self):
        self.__log = Logger_T()
        self.__log.log(message="Initializing [ViewAbstract_T]", level=logging.INFO)
        self.viewModel : viewModel_abstract_T = None

    def addViewModel(self, viewModel : viewModel_abstract_T):
        self.__log.log(message="Adding ViewModel", level=logging.DEBUG)
        if self.viewModel is None:
            self.viewModel = viewModel
        else:
            self.__log.log(message="ViewModel allready set", level=logging.ERROR)

    @abstractmethod
    def run(self):
        pass