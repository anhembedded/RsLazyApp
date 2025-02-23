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
    QApplication,
    QLineEdit
)
from PySide6.QtCore import QObject, Signal, Slot


class viewPySide_T(view_abstract_T):
    def __init__(self , viewModel : viewModel_abstract_T = None):
        super().__init__(viewModel)
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


        self.button.clicked.connect(self.viewModel.example_button_clicked_callback)
        self.variableText.setText(self.viewModel.variable)


    @override
    def run(self):
        self.__log.log(message="Running [viewPySide_T]", level=logging.INFO)
        app = QApplication(sys.argv)
        self.createWidgets()
        self.mainWindow.show()
        sys.exit(app.exec())