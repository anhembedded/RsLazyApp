# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from __future__ import annotations
import sys
from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

# Create a basic window with a layout and a button
class MainForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.button = QPushButton("Click me!")
        self.layout.addWidget(self.button)

        # Connect the button's clicked signal to the slot update_str_field
        self.button.clicked.connect(self.start_thread)

        # Instantiate the worker thread
        self.worker = Worker(self)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.thread.deleteLater)
        # Start the thread
        self.thread.start()

    def start_thread(self):
        print("Main:", QThread.currentThread())
        self.worker.signals.signal_str.emit("This is the message")
        self.worker.signals.signal_int.emit(12345)

    # Create the Slots that will receive signals
    @Slot(str)
    def update_str_field(self, message):
        print(message)

    @Slot(int)
    def update_int_field(self, value):
        print(value)

# Signals must inherit QObject
class MySignals(QObject):
    signal_str = Signal(str)
    signal_int = Signal(int)

# Create the Worker Thread class
class Worker(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        # Instantiate signals and connect signals to the slots
        self.signals = MySignals()
        self.signals.signal_str.connect(parent.update_str_field)
        self.signals.signal_int.connect(parent.update_int_field)

    # The run method gets called when the thread starts
    @Slot()
    def run(self):
        print("Worker:", QThread.currentThread())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec())