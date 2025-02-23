from PySide6.QtCore import QObject, Signal, Slot
from utility.log import Logger_T, logging
from models.model_abstract import model_abstract_T

class model_T(model_abstract_T):
    def __init__(self):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [model_T]", level=logging.INFO)

