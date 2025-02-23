from utility.log import Logger_T, logging
from PySide6.QtCore import Signal, QObject  # Import QObject


class viewModel_abstract_T(QObject):  # Inherit from QObject
    buttonClicked = Signal()  # Corrected signal name (camelCase convention)

    def __init__(self):
        super().__init__()  # Initialize QObject
        self.__log = Logger_T()
        self.__log.log(message="Initializing [ViewModelAbstract_T]", level=logging.INFO)


    def example_button_clicked_callback(self):
        self.__log.log(message="Button clicked", level=logging.INFO)
        self.buttonClicked.emit()  # Corrected signal emission and name