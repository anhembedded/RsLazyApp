from utility.log import Logger_T,logging
from viewModels.viewModel_abstract import viewModel_abstract_T

class viewModel_T(viewModel_abstract_T):
    def __init__(self):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [ViewModelAbstract_T]", level=logging.INFO)