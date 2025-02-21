from typing import override
from utility.log import Logger_T, logging
from views.view_abstract import ViewAbstract_T

from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)
from PySide6.QtCore import QObject, Signal, Slot



class viewPySide_T(ViewAbstract_T, QMainWindow):  # Inherit from QMainWindow
    def __init__(self):
        ViewAbstract_T.__init__(self)
        QMainWindow.__init__(self)  # Call QMainWindow's __init__
        self.__log = Logger_T()
        self.__log.log(message="Initializing [viewPySide]", level=logging.INFO)
        self.createWidgets()

    @override
    def createWidgets(self):
        self.setWindowTitle("Development UI engine")
        # UI elements
        self.status_label = QLabel("Ready")
        self.start_button = QPushButton("Start Task")
        self.stop_button = QPushButton("Stop Task")
        self.stop_button.setEnabled(False) # Initially disabled
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)



    def on_button_clicked(self):
        self.__log.log(message="Button clicked", level=logging.INFO)

    @override
    def run(self):
        self.__log.log(message="Running [viewPySide_T]", level=logging.INFO)
        self.show()