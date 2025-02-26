from views.pySide6View.mainWindow.dhc.AutoGen_dhc import Ui_dhcWidget_autoGen_T
from PySide6.QtWidgets import QWidget

class dhcWidget_T(QWidget, Ui_dhcWidget_autoGen_T):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)