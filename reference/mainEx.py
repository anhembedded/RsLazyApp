import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTextEdit,
    QMdiArea,
    QMdiSubWindow,
    QMessageBox,
)
from PySide6.QtCore import Qt


class SubWindow(QWidget):
    """A simple reusable subwindow for our MDI area."""

    def __init__(self, title, content_widget=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)

        layout = QVBoxLayout()
        self.label = QLabel(title)  # Use the title as a label (for demo)
        layout.addWidget(self.label)

        if content_widget:
            layout.addWidget(content_widget)

        self.setLayout(layout)

    def closeEvent(self, event):
        # Example: Confirmation dialog before closing
        reply = QMessageBox.question(
            self,
            "Confirm Close",
            "Are you sure you want to close this window?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            event.accept()  # Allow the window to close
        else:
            event.ignore()  # Prevent the window from closing



class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MDI Area Example")
        self.setGeometry(100, 100, 800, 600)

        # Create the MDI area
        self.mdi_area = QMdiArea()
        self.mdi_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdi_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdi_area)

        # Create a layout for buttons
        button_layout = QHBoxLayout()

        # Button to add a new subwindow
        add_button = QPushButton("Add Subwindow")
        add_button.clicked.connect(self.add_subwindow)
        button_layout.addWidget(add_button)

        add_custom_button = QPushButton("Add Custom Subwindow")
        add_custom_button.clicked.connect(self.add_custom_subwindow)
        button_layout.addWidget(add_custom_button)
        
        add_textedit_button = QPushButton("Add TextEdit Subwindow")
        add_textedit_button.clicked.connect(self.add_textedit_subwindow)
        button_layout.addWidget(add_textedit_button)


        # Button to tile subwindows
        tile_button = QPushButton("Tile Subwindows")
        tile_button.clicked.connect(self.mdi_area.tileSubWindows)
        button_layout.addWidget(tile_button)

        # Button to cascade subwindows
        cascade_button = QPushButton("Cascade Subwindows")
        cascade_button.clicked.connect(self.mdi_area.cascadeSubWindows)
        button_layout.addWidget(cascade_button)
        
        # Button to close all subwindows
        close_all_button = QPushButton("Close All")
        close_all_button.clicked.connect(self.close_all_subwindows)
        button_layout.addWidget(close_all_button)


        # Add buttons to a container widget
        button_container = QWidget()
        button_container.setLayout(button_layout)

        # Main layout to hold buttons and MDI area
        main_layout = QVBoxLayout()
        main_layout.addWidget(button_container)
        main_layout.addWidget(self.mdi_area)  # Add MDI area *after* buttons

        # Central widget for the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.subwindow_count = 0  # Keep track of subwindows

    def add_subwindow(self):
        """Adds a simple subwindow to the MDI area."""

        self.subwindow_count += 1
        sub_window = QMdiSubWindow()
        sub_window.setWidget(SubWindow(f"Subwindow {self.subwindow_count}"))
        sub_window.setAttribute(Qt.WA_DeleteOnClose)  # Important for memory management
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()


    def add_custom_subwindow(self):
        """Adds a subwindow with custom content (QLineEdit)."""
        self.subwindow_count += 1
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter text here...")
        sub_window = QMdiSubWindow()
        sub_window_content = SubWindow(f"Custom Subwindow {self.subwindow_count}", content_widget=line_edit)
        sub_window.setWidget(sub_window_content)
        sub_window.setAttribute(Qt.WA_DeleteOnClose)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

    def add_textedit_subwindow(self):
        """Adds a subwindow containing a QTextEdit."""
        self.subwindow_count += 1
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("Type your text here...")
        sub_window = QMdiSubWindow()
        sub_window_content = SubWindow(f"TextEdit Subwindow {self.subwindow_count}", content_widget=text_edit)

        sub_window.setWidget(sub_window_content)
        sub_window.setAttribute(Qt.WA_DeleteOnClose)  # Crucial for memory management
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()


    def close_all_subwindows(self):
        """Closes all subwindows in the MDI area."""
        self.mdi_area.closeAllSubWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())