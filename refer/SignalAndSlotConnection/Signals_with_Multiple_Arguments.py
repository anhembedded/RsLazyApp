from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QObject, Signal, Slot
import sys

class MyEmitter(QObject):
    # Signal with two arguments (int, str)
    my_signal = Signal(int, str)

    def emit_signal(self, number, text):
        self.my_signal.emit(number, text)

class MyReceiver(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Waiting for signal...")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

    @Slot(int, str)
    def receive_signal(self, number, text):
        self.label.setText(f"Received: Number={number}, Text={text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    emitter = MyEmitter()
    receiver = MyReceiver()

    emitter.my_signal.connect(receiver.receive_signal)
    emitter.emit_signal(42, "Hello")

    receiver.show()
    sys.exit(app.exec())