from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QLineEdit,
                               QApplication)
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QLineEdit, QApplication)
from PySide6.QtGui import *
from PySide6 import *

from PySide6.QtCore import Qt, Signal, QEvent

class TerminalWidget_T(QWidget):
    command_executed = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.history = []
        self.history_index = 0
        self._current_draft = ""
        self.init_ui()
        self.init_style()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Output area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setUndoRedoEnabled(False)
        self.output_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Input area
        self.input_line = QLineEdit()
        self.input_line.installEventFilter(self)

        # Add widgets to layout
        self.layout.addWidget(self.output_area)
        self.layout.addWidget(self.input_line)

        # Connections
        self.input_line.returnPressed.connect(self.execute_command)

    def init_style(self):
        # Set monospace font
        font = QFont("Courier New")
        if not font.exactMatch():
            font.setFamily("Monospace")
        self.output_area.setFont(font)
        self.input_line.setFont(font)

        # Basic color scheme
        self.output_area.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                color: #CCCCCC;
                border: none;
            }
        """)
        self.input_line.setStyleSheet("""
            QLineEdit {
                background-color: #252525;
                color: #FFFFFF;
                border: 1px solid #3F3F3F;
                padding: 2px;
            }
        """)

    def eventFilter(self, obj, event):
        if obj == self.input_line and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Up:
                self.navigate_history(-1)
                return True
            elif event.key() == Qt.Key_Down:
                self.navigate_history(1)
                return True
            elif event.key() == Qt.Key_Escape:
                self.input_line.clear()
                return True
        return super().eventFilter(obj, event)

    def navigate_history(self, direction):
        if not self.history:
            return

        if direction < 0:  # Up
            self.history_index = max(0, self.history_index - 1)
        else:  # Down
            self.history_index = min(len(self.history), self.history_index + 1)

        if self.history_index < len(self.history):
            self.input_line.setText(self.history[self.history_index])
        else:
            self.input_line.clear()

    def execute_command(self):
        command = self.input_line.text().strip()
        if not command:
            return

        # Add to history
        if not self.history or self.history[-1] != command:
            self.history.append(command)
        self.history_index = len(self.history)

        # Display command
        self.append_output(f"> {command}\n", "#4EC9B0")
        
        # Emit signal and clear input
        self.command_executed.emit(command)
        self.input_line.clear()

    def append_output(self, text, color=None):
        cursor = self.output_area.textCursor()
        cursor.movePosition(QTextCursor.End)

        if color:
            format = QTextCharFormat()
            format.setForeground(QColor(color))
            cursor.setCharFormat(format)

        cursor.insertText(text)
        self.output_area.setTextCursor(cursor)
        self.output_area.ensureCursorVisible()

    def mousePressEvent(self, event):
        self.input_line.setFocus()
        super().mousePressEvent(event)

    def clear(self):
        self.output_area.clear()

# Example usage
if __name__ == "__main__":
    app = QApplication([])
    
    terminal = TerminalWidget_T()
    terminal.resize(600, 400)
    terminal.show()
    
    # Example command handler
    def handle_command(cmd):
        terminal.append_output(f"Executed: {cmd}\n", "#CE9178")
        if cmd == "clear":
            terminal.clear()
    
    terminal.command_executed.connect(handle_command)
    
    app.exec()