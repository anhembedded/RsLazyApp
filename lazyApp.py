from utility.log import Logger_T, logging
from views.view_abstract import view_abstract_T
from views.pySide6View.pySideView import viewPySide_T  # Import your corrected viewPySide_T
from viewModels.viewModel_abstract import viewModel_abstract_T
from viewModels.viewModel import viewModel_T
from models.model_abstract import model_abstract_T
from models.model import model_T
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread

class lazyAppUI_T:
    def __init__(self):
        self.__log = Logger_T()
        self.__log.log(message="Initializing [lazyAppUI_T]", level=logging.INFO)

        self.app = None  # Initialize to None
        self.__view: view_abstract_T = None

    def run(self):
        self.__log.log(message="Running [lazyAppUI_T]", level=logging.DEBUG)
        self.__uiTask()

    def __uiTask(self):
        self.__log.log(message="Running [UI task]", level=logging.DEBUG)
        self.app = QApplication(sys.argv)
        self.__view = viewPySide_T()
        self.__view.run()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    appUI = lazyAppUI_T()
    appUI.run()