from abc import abstractmethod
from utility.log import Logger_T, logging
from viewModels.viewModel_abstract import viewModel_abstract_T

class view_abstract_T:
    def __init__(self):
        self.__log = Logger_T()
        self.__log.log(message="Initializing [ViewAbstract_T]", level=logging.INFO)
        self.__viewModel = None

    def addViewModel(self, viewModel : viewModel_abstract_T):
        if viewModel is None:
            self.__viewModel = viewModel
        else:
            self.__log.log(message="ViewModel allready set", level=logging.ERROR)

    @abstractmethod
    def createWidgets(self):
        pass

    @abstractmethod
    def run(self):
        pass