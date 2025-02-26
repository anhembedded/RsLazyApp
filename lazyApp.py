from utility.log import Logger_T, logging
from views.view_abstract import view_abstract_T
from views.pySide6View.pySideView import viewPySide_T  # Import your corrected viewPySide_T
import sys
from PySide6.QtWidgets import QApplication


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