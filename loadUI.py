import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice  # Import QFile and QIODevice
import argparse  # Import argparse
from pathlib import Path


def load_ui_file(ui_file_path):
    """Loads a .ui file and returns the top-level widget.

    Args:
        ui_file_path: The path to the .ui file (str or Path).

    Returns:
        The loaded QWidget (or QMainWindow, QDialog, etc.) or None on error.
    """
    ui_file = QFile(ui_file_path)
    if not ui_file.open(QIODevice.OpenModeFlag.ReadOnly):  # Use QIODevice
        print(f"Cannot open {ui_file_path}: {ui_file.errorString()}")
        return None

    loader = QUiLoader()
    window = loader.load(ui_file)  # No need for parent here
    ui_file.close()

    if not window:
        print(loader.errorString())
        return None

    return window

def main():
    """Main function to parse arguments, load UI, and run the application."""

    parser = argparse.ArgumentParser(description="Load and display a PySide6 UI file.")
    parser.add_argument("ui_file", help="Path to the .ui file")
    args = parser.parse_args()

    ui_file_path = Path(args.ui_file)

    if not ui_file_path.exists():
        print(f"Error: UI file not found: {ui_file_path}")
        sys.exit(1)
    if not ui_file_path.is_file():
        print(f"Error: UI file path is not a file: {ui_file_path}")
        sys.exit(1)
    if ui_file_path.suffix.lower() != ".ui":
        print(f"Error: UI file path is not a ui file: {ui_file_path}")
        sys.exit(1)

    app = QtWidgets.QApplication(sys.argv)
    window = load_ui_file(str(ui_file_path)) # Convert Path to string

    if window is None:
        sys.exit(1)  # Exit if UI loading failed

    def do_something():
        # Example of accessing widgets (assuming these exist in your UI)
        try:
            print(window.full_name_line_edit.text(), "is a", window.occupation_line_edit.text())
        except AttributeError as e:
            print(f"Error accessing widgets: {e}.  Check your .ui file and widget names.")
            # You might want to exit here, or handle the missing widgets gracefully
            sys.exit(1)


    # Example of setting window title (if it's a QMainWindow or has a windowTitle property)
    if hasattr(window, "setWindowTitle"):  # Check if setWindowTitle exists
        window.setWindowTitle("RS_LazyApp_MainWindow")

    #Connect signal (assuming you have a button named 'my_button' in your UI)
    try:
        window.my_button.clicked.connect(do_something)
    except AttributeError:
        print("Warning: 'my_button' not found in UI.  Skipping signal connection.")
        # Do NOT exit here; the program can still run without this button

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()