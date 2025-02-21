from utility.log import Logger_T, logging
from threading import Thread

from views.view_abstract import ViewAbstract_T
from views.pySideView import viewPySide_T
from viewModels.viewModel_abstract import viewModelAbstract_T


import sys
from PySide6.QtWidgets import QApplication

class lazyAppUI_T:
    def __init__(self):
        self.__log = Logger_T()
        self.__log.log(message="Initializing [lazyAppUI_T]", level=logging.INFO)
        self.__uiThread = Thread(target=self.__uiTask, daemon=True)
        self.app = QApplication(sys.argv)
        self.__view : ViewAbstract_T = viewPySide_T()
        self.__viewModel : viewModelAbstract_T = None



    def run(self):
        self.__log.log(message="Running [lazyAppUI_T]", level=logging.DEBUG)
        self.__uiThread.start()
        self.__uiThread.join()

    def __uiTask(self):
        self.__log.log(message="Running [UI task]", level=logging.DEBUG)
        self.__view.run()

    def __addViewModel(self, viewModel : viewModelAbstract_T):
        if viewModel is None:
            self.__viewModel = viewModel
        else:
            self.__log.log(message="ViewModel allready set", level=logging.ERROR)

    def __addView(self, view : ViewAbstract_T):
        if view is None:
            self.__view = view
        else:
            self.__log.log(message="View allready set", level=logging.ERROR)