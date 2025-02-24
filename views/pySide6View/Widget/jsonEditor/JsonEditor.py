import json
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QMessageBox
from PySide6.QtGui import QTextCharFormat, QColor, QFont, QSyntaxHighlighter, QTextCursor
from PySide6.QtCore import Qt, QRegularExpression, QEvent


class JsonHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for JSON data."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        # JSON keys
        key_format = QTextCharFormat()
        key_format.setForeground(QColor("#4EC9B0"))  # Light blue
        self.highlighting_rules.append((QRegularExpression(r'"(\\"|[^"])*"\s*:'), key_format))

        # JSON strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))  # Light orange
        self.highlighting_rules.append((QRegularExpression(r'"(\\"|[^"])*"'), string_format))

        # JSON numbers
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))  # Light green
        self.highlighting_rules.append((QRegularExpression(r'\b\d+\b'), number_format))

        # JSON keywords (true, false, null)
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))  # Blue
        keywords = ["true", "false", "null"]
        for word in keywords:
            self.highlighting_rules.append((QRegularExpression(fr'\b{word}\b'), keyword_format))

    def highlightBlock(self, text):
        """Apply syntax highlighting to the current text block."""
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)


class JsonEditorWidget(QWidget):
    """A widget for displaying and editing JSON data with syntax highlighting and zoom."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components."""
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Text edit for JSON input
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Courier New", 10))
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #CCCCCC;
                border: 1px solid #3F3F3F;
            }
        """)
        self.layout.addWidget(self.text_edit)

        # Syntax highlighter
        self.highlighter = JsonHighlighter(self.text_edit.document())

        # Enable zoom with Ctrl + Mouse Wheel
        self.text_edit.setMouseTracking(True)
        self.text_edit.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        """Handle mouse wheel events for zooming."""
        if obj == self.text_edit.viewport() and event.type() == QEvent.Type.Wheel:
            if event.modifiers() == Qt.ControlModifier:
                self.zoom_text(event.angleDelta().y())
                return True
        return super().eventFilter(obj, event)

    def zoom_text(self, delta):
        """Zoom in or out based on the mouse wheel delta."""
        current_font = self.text_edit.font()
        current_size = current_font.pointSize()

        if delta > 0:  # Zoom in
            new_size = current_size + 1
        else:  # Zoom out
            new_size = max(6, current_size - 1)  # Minimum font size of 6

        current_font.setPointSize(new_size)
        self.text_edit.setFont(current_font)

    def set_json(self, data):
        """Load JSON data into the editor."""
        try:
            formatted_json = json.dumps(data, indent=4)
            self.text_edit.setPlainText(formatted_json)
        except Exception as e:
            self.show_error(f"Invalid JSON data: {e}")

    def get_json(self):
        """Retrieve and validate JSON data from the editor."""
        try:
            json_data = json.loads(self.text_edit.toPlainText())
            return json_data
        except json.JSONDecodeError as e:
            self.show_error(f"Invalid JSON: {e}")
            return None

    def show_error(self, message):
        """Display an error message."""
        QMessageBox.critical(self, "Error", message)

    def validate_json(self):
        """Check if the current content is valid JSON."""
        try:
            json.loads(self.text_edit.toPlainText())
            return True
        except json.JSONDecodeError:
            return False

    def clear(self):
        """Clear the editor."""
        self.text_edit.clear()


# Example Usage
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    # Sample JSON data
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "address": {
            "street": "123 Main St",
            "city": "Anytown"
        },
        "hobbies": ["reading", "coding", "gaming"]
    }

    # Create and show the widget
    editor = JsonEditorWidget()
    editor.set_json(sample_data)
    editor.resize(600, 400)
    editor.show()

    # Retrieve JSON data
    def print_json():
        json_data = editor.get_json()
        if json_data:
            print("Current JSON Data:", json_data)

    # Simulate retrieving JSON after a delay
    from PySide6.QtCore import QTimer
    QTimer.singleShot(3000, print_json)

    app.exec()