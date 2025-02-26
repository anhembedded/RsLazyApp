from views.pySide6View.mainWindow.vls.AutoGen_vls import Ui_vls_autoGen_T
from PySide6.QtWidgets import QWidget

class vlsWidget_T(Ui_vls_autoGen_T, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)