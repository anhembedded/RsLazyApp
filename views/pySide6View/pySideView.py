from typing import override
import sys
from utility.log import Logger_T, logging
from views.view_abstract import view_abstract_T
from viewModels.viewModel_abstract import viewModel_abstract_T
from views.pySide6View.mainWindow.mainWindow import mainWindow_T
from views.pySide6View.Widget.terminalLike.terminalLike import TerminalWidget_T
from views.pySide6View.Widget.jsonEditor.JsonEditor import JsonEditorWidget_T
from views.pySide6View.mainWindow.config.configWidget import configWidget_T
from views.pySide6View.mainWindow.dhc.dhcWidget import dhcWidget_T
from views.pySide6View.mainWindow.vls.vlsWidget import vlsWidget_T

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

    def createWidgets(self):
        self.mainWindow = mainWindow_T()
        self.terminalLike = TerminalWidget_T()
        self.jsonEditor = JsonEditorWidget_T()
        self.configWidget = configWidget_T()
        self.dhcWidget = dhcWidget_T()
        self.vlsWidget = vlsWidget_T()


        self.mainWindow.mdiArea_app.addSubWindow(self.configWidget).setWindowTitle("Config")
        self.mainWindow.mdiArea_app.addSubWindow(self.dhcWidget).setWindowTitle("DHC")
        self.mainWindow.mdiArea_app.addSubWindow(self.vlsWidget).setWindowTitle("VLS")
        self.mainWindow.show()

    @override
    def run(self):
        self.__log.log(message="Running [viewPySide_T]", level=logging.INFO)
        self.createWidgets()
        self.mainWindow.show()