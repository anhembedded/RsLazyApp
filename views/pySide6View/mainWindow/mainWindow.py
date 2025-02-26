from views.pySide6View.mainWindow.AutoGen_mainWindow import Ui_MainWindow_autoGen_T
from PySide6.QtWidgets import  QMainWindow

from views.pySide6View.Widget.terminalLike.terminalLike import TerminalWidget_T
from views.pySide6View.Widget.jsonEditor.JsonEditor import JsonEditorWidget_T
from views.pySide6View.mainWindow.config.configWidget import configWidget_T
from views.pySide6View.mainWindow.dhc.dhcWidget import dhcWidget_T
from views.pySide6View.mainWindow.vls.vlsWidget import vlsWidget_T
from views.pySide6View.mainWindow.terminalLike.terminalLikeWidget import TerminalWidget_T

from PySide6.QtWidgets import (
    QMainWindow,
)

class mainWindow_T(QMainWindow,Ui_MainWindow_autoGen_T):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.terminalLike = TerminalWidget_T()
        self.jsonEditor = JsonEditorWidget_T()
        self.configWidget = configWidget_T()
        self.dhcWidget = dhcWidget_T()
        self.vlsWidget = vlsWidget_T()
        self.terminalLike = TerminalWidget_T()
        
        self.mdiArea_app.addSubWindow(self.configWidget).setWindowTitle("Config")
        self.mdiArea_app.addSubWindow(self.dhcWidget).setWindowTitle("DHC")
        self.mdiArea_app.addSubWindow(self.vlsWidget).setWindowTitle("VLS")
        self.groupBox_terminalLike.setLayout(self.terminalLike.layout())