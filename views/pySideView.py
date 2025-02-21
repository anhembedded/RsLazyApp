from typing import override
from utility.log import Logger_T,logging
from views.view_abstract import ViewAbstract_T

import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QPushButton, QWidget

class viewPySide_T(ViewAbstract_T, QWidget):
    def __init__(self):
        ViewAbstract_T.__init__(self)  # Explicitly call ViewAbstract_T's __init__
        QWidget.__init__(self)  # Explicitly call QMainWindow's __init__
        self.__log = Logger_T()
        self.__log.log(message="Initializing [viewPySide]", level=logging.INFO)

    @override
    def createWidgets(self):
        self.__log.log(message="Creating widgets", level=logging.DEBUG)
        self.__layout = QVBoxLayout()
        self.__label = QLabel("Wating for update...")
        self.__button = QPushButton("Start Task")
        self.__layout.addWidget(self.__label)
        self.__layout.addWidget(self.__button)
        self.setLayout(self.__layout)

        self.__button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.__log.log(message="Button clicked", level=logging.INFO)

    @override
    def run(self):
        self.__log.log(message="Running [viewPySide_T]", level=logging.INFO)
        self.show()