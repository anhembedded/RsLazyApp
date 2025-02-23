from views.pySide6View.mainWindow.autoGen_mainWindow import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QMainWindow

class mainWindow_T(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)