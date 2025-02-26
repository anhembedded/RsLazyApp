from views.pySide6View.mainWindow.config.AutoGen_config import Ui_configWidget_autoGen_T
from PySide6.QtWidgets import QWidget

class configWidget_T(QWidget, Ui_configWidget_autoGen_T):
    def __init__(self, parent=None):
        super(configWidget_T, self).__init__(parent)
        self.setupUi(self)