from utility.log import Logger_T,logging

class viewModel_abstract_T:
    def __init__(self):
        self.__log = Logger_T()
        self.__log.log(message="Initializing [ViewModelAbstract_T]", level=logging.INFO)