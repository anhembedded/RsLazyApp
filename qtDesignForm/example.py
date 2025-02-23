import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QMenuBar, QStatusBar

class MainWindow(QMainWindow):  # Inherits from QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMainWindow Example")

        # Central Widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)  # MUST set a central widget

        # Menu Bar
        menu_bar = self.menuBar() # Get QMainWindow menu bar
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("Open")
        file_menu.addAction("Save")

        # Toolbar
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction("Copy")
        toolbar.addAction("Paste")

        # Status Bar
        status_bar = self.statusBar() # Get QMainWindow status bar
        status_bar.showMessage("Ready", 3000)  # Display a message for 3 seconds

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())