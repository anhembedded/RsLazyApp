from PySide6.QtWidgets import QApplication, QLineEdit, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Slot
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit()
        self.label = QLabel("Enter text:")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

        # Connect textChanged signal (which has a str argument)
        self.line_edit.textChanged.connect(self.text_changed_slot)

    @Slot(str)  # Specify the argument type in the decorator
    def text_changed_slot(self, new_text):
        self.label.setText(f"You typed: {new_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())