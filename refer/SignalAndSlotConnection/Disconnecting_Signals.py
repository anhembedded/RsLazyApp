from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox, QVBoxLayout, QWidget
from PySide6.QtCore import Slot
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button1 = QPushButton("Connect")
        self.button2 = QPushButton("Disconnect")
        self.button3 = QPushButton("Emit Signal (No effect if disconnected)")
        layout = QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.button1.clicked.connect(self.connect_signal)
        self.button2.clicked.connect(self.disconnect_signal)
        self.button3.clicked.connect(self.show_message) # Connect to show_message

        self.connection = None  # Store the connection object

    @Slot()
    def connect_signal(self):
        if self.connection is None:
             self.connection = self.button3.clicked.connect(self.show_message)
             QMessageBox.information(self, "Message", "Signal Connected")

    @Slot()
    def disconnect_signal(self):
        if self.connection:
            self.button3.clicked.disconnect(self.show_message) #disconnect the clicked Signal
            self.connection = None  # Reset the connection
            QMessageBox.information(self, "Message", "Signal Disconnected")
        else:
            QMessageBox.information(self, "Message", "Signal Not Connected")

    @Slot()
    def show_message(self):
        QMessageBox.information(self, "Message", "Signal Received!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())