import sys
import json
from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont, QFontDatabase
import re

class JsonHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.rules = []

        # Key (string in quotes)
        key_format = QTextCharFormat()
        key_format.setForeground(QColor(128, 0, 128))  # Purple
        self.rules.append((re.compile(r'"(\w+)":'), key_format))

        # String value
        string_format = QTextCharFormat()
        string_format.setForeground(QColor(0, 128, 0))  # Green
        self.rules.append((re.compile(r'(".*?")'), string_format))

        # Number value
        number_format = QTextCharFormat()
        number_format.setForeground(QColor(0, 0, 255))  # Blue
        self.rules.append((re.compile(r'\b(-?\d+(\.\d+)?)\b'), number_format))

        # Boolean value
        boolean_format = QTextCharFormat()
        boolean_format.setForeground(QColor(255, 0, 0)) # Red
        self.rules.append((re.compile(r'\b(true|false|null)\b'), boolean_format))

        # Brackets and braces
        bracket_format = QTextCharFormat()
        bracket_format.setForeground(QColor(128, 128, 128)) # Grey
        self.rules.append((re.compile(r'[\[\]\{\}\:]'), bracket_format))

    def highlightBlock(self, text):
        for pattern, format in self.rules:
            iterator = pattern.finditer(text)
            for match in iterator:
                start = match.start()
                length = match.end() - start
                self.setFormat(start, length, format)

class JsonDisplayWidget(QWidget):
    def __init__(self, json_data):
        super().__init__()

        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFontDatabase.systemFont(QFontDatabase.FixedFont)) # Monospace font
        self.highlighter = JsonHighlighter(self.text_edit.document())
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text_edit)

        self.set_json_data(json_data)

    def set_json_data(self, json_data):
        try:
            formatted_json = json.dumps(json_data, indent=4) # Pretty print
            self.text_edit.setPlainText(formatted_json)
        except (TypeError, json.JSONDecodeError):
            self.text_edit.setPlainText("Invalid JSON data.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    json_data = {
        "name": "Example",
        "age": 30,
        "is_active": True,
        "address": {
            "street": "123 Main St",
            "city": "Anytown"
        },
        "numbers": [1, 2, 3.14, "string"]
    }

    window = JsonDisplayWidget(json_data)
    window.show()

    sys.exit(app.exec())