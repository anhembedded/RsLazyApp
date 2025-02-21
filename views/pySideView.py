from typing import override
from utility.log import Logger_T, logging
from views.view_abstract import ViewAbstract_T

from threading import Thread

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QProgressBar,
)
from PySide6.QtCore import QObject, Signal, Slot



class viewPySide_T(ViewAbstract_T, QMainWindow):  # Inherit from QMainWindow
    def __init__(self):
        ViewAbstract_T.__init__(self)
        QMainWindow.__init__(self)  # Call QMainWindow's __init__
        self.__log = Logger_T()
        self.__log.log(message="Initializing [viewPySide]", level=logging.INFO)
        self.createWidgets()

    @override
    def createWidgets(self):
        self.setWindowTitle("PySide6 Threading Example")
        # UI elements
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.status_label = QLabel("Ready")
        self.start_button = QPushButton("Start Task")
        self.stop_button = QPushButton("Stop Task")
        self.stop_button.setEnabled(False) # Initially disabled

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connections
        self.start_button.clicked.connect(self.start_task)
        self.stop_button.clicked.connect(self.stop_task)

        # Threading setup
        self.worker_thread = None  # Store the worker thread
        self.worker = None  # Store the Worker object

    @Slot()
    def start_task(self):
        """Starts the long-running task in a separate thread."""

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.status_label.setText("Running...")
        self.progress_bar.setValue(0)


        self.worker = Worker()  # Create a *new* Worker instance
        self.worker_thread = Thread(target=self.worker.run)
        self.worker_thread.daemon = True  # Allow program to exit if only the thread remains
        self.worker_thread.start()


        # Connect signals from the worker to slots in the main thread
        self.worker.progress.connect(self.update_progress)
        self.worker.result.connect(self.show_result)
        self.worker.finished.connect(self.task_finished)
        self.worker.error.connect(self.handle_error)


    @Slot()
    def stop_task(self):
        """Stops the running task."""
        if self.worker:
            self.worker.stop()  # Signal the worker to stop
        self.status_label.setText("Stopping...")


    @Slot(int)
    def update_progress(self, value):
        """Updates the progress bar."""
        self.progress_bar.setValue(value)

    @Slot(str)
    def show_result(self, message):
        """Displays the result message."""
        self.status_label.setText(message)

    @Slot()
    def task_finished(self):
        """Handles the completion of the task."""
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        if self.status_label.text() == "Stopping...":
            self.status_label.setText("Stopped") # Show stopped status.
        # Clean up (important!)
        self.worker_thread = None
        self.worker = None

    @Slot(str)
    def handle_error(self, error_message):
        """Displays error message."""
        self.status_label.setText(f"Error: {error_message}")
        self.start_button.setEnabled(True)  # Re-enable start button on error
        self.stop_button.setEnabled(False)

    def on_button_clicked(self):
        self.__log.log(message="Button clicked", level=logging.INFO)

    @override
    def run(self):
        self.__log.log(message="Running [viewPySide_T]", level=logging.INFO)
        self.show()