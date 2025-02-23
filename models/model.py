from PySide6.QtCore import QObject, Signal, Slot
from utility.log import Logger_T, logging
from models.model_abstract import model_abstract_T
from viewModels.viewModel_abstract import viewModel_abstract_T

class model_T(model_abstract_T):
    def __init__(self, viewModel : viewModel_abstract_T):
        super().__init__(viewModel)
        self.__log = Logger_T()
        self.__log.log(message="Initializing [model_T]", level=logging.INFO)
        self.viewModel.buttonClicked.connect(self.task_buttonClicked)

