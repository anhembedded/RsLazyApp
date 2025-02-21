from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Close")
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

        # Connect clicked signal to the built-in close slot of QWidget
        self.button.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())