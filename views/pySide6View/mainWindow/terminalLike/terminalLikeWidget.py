from views.pySide6View.mainWindow.terminalLike.AutoGen_terminalLike import Ui_terminalLike_autoGen_T
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QProcess, Qt
from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                               QCompleter)
from PySide6.QtCore import Signal
from PySide6.QtCore import QStringListModel

class TerminalWidget_T(Ui_terminalLike_autoGen_T, QWidget):
    commandExecuted = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.commandList = QStringListModel()

        completion_list = [
            "apple",
            "banana",
            "orange",
            "grape",
            "watermelon",
            "pineapple",
            "strawberry",
            "blueberry",
            "raspberry",
            "mango",
            "peach",
            "pear",
        ]

        self.commandList.setStringList(completion_list)
        self.completer = QCompleter(self.commandList, self)
        self.completer.setModel(self.commandList)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive) # Make it case-insensitive
        self.completer.setCompletionMode(QCompleter.CompletionMode.UnfilteredPopupCompletion) # Show popup

        self.lineEdit_input.setCompleter(self.completer)

        self.plainTextEdit_output.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        # Command input
        self.lineEdit_input.setPlaceholderText("Enter command...")
        self.lineEdit_input.returnPressed.connect(self.runCommand)

        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.displayOutput)
        self.process.start("powershell.exe")  # Starts a persistent CMD session

    def runCommand(self):
        command = self.lineEdit_input.text().strip()
        if not command:
            return
        if command in self.commandList.stringList():
            self.commandExecuted.emit(command)
            self.plainTextEdit_output.appendPlainText(f"> {command}")  # Show input command
            self.lineEdit_input.clear()
        else:
            self.plainTextEdit_output.appendPlainText(f"> {command}")  # Show input command
            self.process.write((command + "\n").encode("utf-8"))  # Send command
            self.lineEdit_input.clear()

    def displayOutput(self):
        output = self.process.readAllStandardOutput().data().decode("utf-8")
        self.plainTextEdit_output.appendPlainText(output.strip())

    def closeEvent(self, event):
        """Ensure the process is terminated when the widget is closed."""
        if self.process.state() != QProcess.ProcessState.NotRunning:
            self.process.terminate()
            if not self.process.waitForFinished(1000):
                self.process.kill()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    terminal = TerminalWidget_T()
    terminal.addUserCommandList(["help", "clear", "exit"])
    terminal.resize(600, 400)
    terminal.show()
    app.exec()