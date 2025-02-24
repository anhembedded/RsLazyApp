
# TerminalWidget - PySide6 Terminal-like Widget

`TerminalWidget` is a customizable, terminal-like widget for PySide6 applications. It provides a read-only output area, a command input field, command history navigation, and colored output support. It is designed to be easily integrated into any PySide6-based UI.

---

## Features

- **Read-Only Output Area**: Displays terminal output in a scrollable, read-only text area.
- **Command Input Field**: Dedicated area for user input.
- **Command History**: Navigate through previously entered commands using the **Up** and **Down** arrow keys.
- **Colored Output**: Supports colored text output for better readability.
- **Monospace Font**: Ensures consistent character spacing for a terminal-like appearance.
- **Dark Theme**: Modern dark theme with customizable styling.
- **Signal-Based Command Handling**: Emits a signal when a command is executed for easy integration.

---

## Installation

1. Ensure you have Python installed (3.7 or higher).
2. Install PySide6:
   ```bash
   pip install PySide6
   ```
3. Copy the `TerminalWidget` class into your project or import it from a module.

---

## Usage

### Basic Integration

1. Add the `TerminalWidget` to your PySide6 application:

   ```python
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
   from terminal_widget import TerminalWidget  # Replace with the actual module name

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           self.setWindowTitle("Terminal Widget Example")
           self.resize(800, 600)

           # Create a central widget and layout
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           layout = QVBoxLayout(central_widget)

           # Add the TerminalWidget
           self.terminal = TerminalWidget()
           layout.addWidget(self.terminal)

           # Connect to the command_executed signal
           self.terminal.command_executed.connect(self.handle_command)

       def handle_command(self, command):
           self.terminal.append_output(f"Executed: {command}\n", "#CE9178")
           if command == "clear":
               self.terminal.clear()

   if __name__ == "__main__":
       app = QApplication([])
       window = MainWindow()
       window.show()
       app.exec()
   ```
2. Run your application, and you'll see the terminal widget in action.

---

### Key Methods

- **`append_output(text, color=None)`**: Append text to the output area. Optionally specify a color (hex format).

  ```python
  terminal.append_output("Hello, World!\n", "#4EC9B0")
  ```
- **`clear()`**: Clear the output area.

  ```python
  terminal.clear()
  ```
- **`command_executed` Signal**: Emitted when a command is entered. Connect to this signal to handle commands.

  ```python
  terminal.command_executed.connect(self.handle_command)
  ```

---

### Customization

#### Styling

You can customize the appearance of the terminal by modifying the `init_style` method or using external stylesheets.

Example:

```python
self.output_area.setStyleSheet("""
    QTextEdit {
        background-color: #000000;
        color: #00FF00;
        border: 1px solid #333333;
    }
""")
self.input_line.setStyleSheet("""
    QLineEdit {
        background-color: #111111;
        color: #FFFFFF;
        border: 1px solid #555555;
    }
""")
```

#### Font

Change the font by modifying the `QFont` initialization in `init_style`:

```python
font = QFont("Consolas", 10)  # Use Consolas font with size 10
```

---

## Example Commands

Here’s an example of how you can handle commands:

```python
def handle_command(self, command):
    if command == "help":
        self.terminal.append_output("Available commands: help, clear, echo\n", "#4EC9B0")
    elif command.startswith("echo"):
        self.terminal.append_output(f"{command[5:]}\n", "#CE9178")
    elif command == "clear":
        self.terminal.clear()
    else:
        self.terminal.append_output(f"Unknown command: {command}\n", "#FF5555")
```

---

## Keyboard Shortcuts

- **Up Arrow**: Navigate to the previous command in history.
- **Down Arrow**: Navigate to the next command in history.
- **Escape**: Clear the current input.
- **Enter**: Execute the command.

---

## Dependencies

- PySide6

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---

Enjoy using `TerminalWidget` in your PySide6 applications! 🚀
