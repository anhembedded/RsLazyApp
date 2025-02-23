from typing import override
from utility.log import Logger_T, logging
from views.view_abstract import view_abstract_T

from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)
from PySide6.QtCore import QObject, Signal, Slot



class viewPySide_T(view_abstract_T, QMainWindow):  # Inherit from QMainWindow
    def __init__(self):
        view_abstract_T.__init__(self)
        QMainWindow.__init__(self)  # Call QMainWindow's __init__
        self.__log = Logger_T()
        self.__log.log(message="Initializing [viewPySide]", level=logging.INFO)
        self.createWidgets()

    @override
    def createWidgets(self):
        self.setWindowTitle("Development UI engine")
        # UI elements
        self.label = QLabel("Example label")
        self.button = QPushButton("Example label")
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)



    def on_button_clicked(self):
        self.__log.log(message="Button clicked", level=logging.INFO)

    @override
    def run(self):
        self.__log.log(message="Running [viewPySide_T]", level=logging.INFO)
        self.show()