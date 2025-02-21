from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal, Slot, pyqtSignal # Using pyqtSignal (works in PySide6)
import sys
class MyEmitter(QObject):
    # Overloaded signal: one version with int, one with str
    my_signal = pyqtSignal(int)
    my_signal_str = pyqtSignal(str)


    def __init__(self):
        super().__init__()
        #Connect to the appropriate signal overload
        self.my_signal.connect(self.handle_int)
        self.my_signal_str.connect(self.handle_str)


    def emit_int(self, value):
        self.my_signal.emit(value)

    def emit_str(self, value):
        self.my_signal_str.emit(value) #Explicit call.

    @Slot(int)
    def handle_int(self, value):
        print(f"Received int: {value}")

    @Slot(str)
    def handle_str(self, value):
        print(f"Received str: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    emitter = MyEmitter()
    emitter.emit_int(42)
    emitter.emit_str("Hello")
    sys.exit(app.exec())