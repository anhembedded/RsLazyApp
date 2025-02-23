from typing import override
import sys
from utility.log import Logger_T, logging
from views.view_abstract import view_abstract_T
from viewModels.viewModel_abstract import viewModel_abstract_T
from views.pySide6View.mainWindow.mainWindow import mainWindow_T

from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit
)
from PySide6.QtCore import QObject, Signal, Slot


class viewPySide_T(view_abstract_T):
    def __init__(self):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [viewPySide]", level=logging.INFO)

    @override
    def createWidgets(self):
        # UI elements (initialize here for consistency)
        self.mainWindow = mainWindow_T()
        self.mainWindow.show()

    @override
    def run(self):
        self.__log.log(message="Running [viewPySide_T]", level=logging.INFO)
        self.createWidgets()
        self.mainWindow.show()