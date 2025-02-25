import sys
from PySide6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("This is a label with margins.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the label to the layout, and use layout margins.
        layout.addWidget(label)
        layout.setContentsMargins(20, 20, 20, 20) # left, top, right, bottom

        self.setLayout(layout)
        self.setWindowTitle("Label with Margins (Layout)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())