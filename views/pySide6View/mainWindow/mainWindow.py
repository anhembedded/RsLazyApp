from views.pySide6View.mainWindow.autoGen_mainWindow import Ui_MainWindow_autoGen_T
from PySide6.QtWidgets import  QMainWindow

class mainWindow_T(QMainWindow,Ui_MainWindow_autoGen_T):
    def __init__(self):
        super().__init__()
        self.setupUi(self)