from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox
from PySide6.QtCore import QObject, Signal, Slot
import sys

class MyObject(QObject):
    # Define a custom signal (no arguments)
    my_signal = Signal()

    def __init__(self):
        super().__init__()

    def emit_the_signal(self):
        self.my_signal.emit()  # Emit the signal

class MyWindow(QPushButton):
    def __init__(self):
        super().__init__("Click Me")
        self.clicked.connect(self.button_clicked)

    @Slot()
    def button_clicked(self):
        QMessageBox.information(self, "Message", "Button Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()

    # Example with a custom signal:
    obj = MyObject()
    obj.my_signal.connect(window.button_clicked) # Connect custom signal to slot
    obj.emit_the_signal() # This will now trigger button_clicked.

    window.show()
    sys.exit(app.exec())