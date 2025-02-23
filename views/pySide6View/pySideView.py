from typing import override
import sys
from utility.log import Logger_T, logging
from views.view_abstract import view_abstract_T
from viewModels.viewModel_abstract import viewModel_abstract_T

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

    @override
    def createWidgets(self):
        # UI elements (initialize here for consistency)
        self.mainWindow = QMainWindow()
        self.label = QLabel("Example label")
        self.variableText = QLabel("Some text")
        self.button = QPushButton("Example button")
        self.mainWindow.setWindowTitle("Development UI engine")
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.variableText)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.mainWindow.setCentralWidget(central_widget)  # Corrected line!
        self.button.clicked.connect(self.buttonClicked)
        self.viewModel.taskResult.connect(self.updateVariableText)

    @Slot()
    def buttonClicked(self):
        self.viewModel.buttonClicked.emit()
    @Slot(str)
    def updateVariableText(self, text):
        self.variableText.setText(text)

    @override
    def run(self):
        self.__log.log(message="Running [viewPySide_T]", level=logging.INFO)
        self.createWidgets()
        self.mainWindow.show()