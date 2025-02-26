from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QLineEdit
from PySide6.QtCore import QProcess, Qt
from PySide6.QtGui import QTextOption




class TerminalWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fast Embedded Terminal")
        self.setGeometry(100, 100, 600, 400)


        layout = QVBoxLayout()


        # Output display
        self.output_display = QPlainTextEdit(self)
        self.output_display.setReadOnly(True)
        self.output_display.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)


        # Command input
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter command...")
        self.input_field.returnPressed.connect(self.run_command)


        # Add widgets to layout
        layout.addWidget(self.output_display)
        layout.addWidget(self.input_field)
        self.setLayout(layout)


        # Start persistent shell session
        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)  # Merge stdout and stderr
        self.process.readyReadStandardOutput.connect(self.display_output)
        self.process.start("powershell.exe")  # Starts a persistent CMD session


    def run_command(self):
        """Send command to the running shell"""
        command = self.input_field.text().strip()
        if not command:
            return


        self.output_display.appendPlainText(f"> {command}")  # Show input command
        self.process.write((command + "\n").encode("utf-8"))  # Send command
        self.input_field.clear()


    def display_output(self):
        """Read and display output from the shell"""
        output = self.process.readAllStandardOutput().data().decode("utf-8")
        self.output_display.appendPlainText(output.strip())
        self.output_display.moveCursor(self.output_display.textCursor().End)

    def addUserCommandList(self, command_list):
        pass


if __name__ == "__main__":
    app = QApplication([])
    terminal = TerminalWidget()
    terminal.show()
    app.exec()
