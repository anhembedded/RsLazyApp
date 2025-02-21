from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox, QWidget, QVBoxLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click Me")
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

        # Connect using a lambda function
        self.button.clicked.connect(lambda: QMessageBox.information(self, "Message", "Button Clicked!"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())