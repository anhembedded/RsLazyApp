from utility.log import Logger_T, logging
from views.view_abstract import ViewAbstract_T
from views.pySideView import viewPySide_T  # Import your corrected viewPySide_T
from viewModels.viewModel_abstract import viewModelAbstract_T
import sys
from PySide6.QtWidgets import QApplication
from threading import Thread

class lazyAppUI_T:
    def __init__(self):
        self.__log = Logger_T()
        self.__log.log(message="Initializing [lazyAppUI_T]", level=logging.INFO)
        self.__uiThread = Thread(target=self.__uiTask, daemon=True)
        self.app = None  # Initialize to None
        self.__view: ViewAbstract_T = None
        self.__viewModel: viewModelAbstract_T = None

    def run(self):
        self.__log.log(message="Running [lazyAppUI_T]", level=logging.DEBUG)
        self.__uiThread.start()
        self.__uiThread.join()
        # Do *NOT* join the UI thread here!

    def __uiTask(self):
        self.__log.log(message="Running [UI task]", level=logging.DEBUG)
        self.app = QApplication(sys.argv)
        self.__view = viewPySide_T()
        self.__view.run()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    appUI = lazyAppUI_T()
    appUI.run()