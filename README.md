
# PySide6 Terminal

## Overview

This project is a simple terminal-like widget built using PySide6 (Qt for Python). It provides a graphical interface with an input field for entering commands and an output area for displaying responses. The application follows the **Model-View-Controller (MVC) pattern** to separate logic, UI, and control flow.

## Features

* **Read-Only Display**: The terminal output is read-only.
* **Command Input**: A dedicated input field allows the user to enter commands.
* **Command History**: Users can navigate through previously entered commands using the Up and Down arrow keys.
* **Cursor Control**: The cursor is restricted to the input area.
* **Handling Enter Key**: Commands are executed when the Enter key is pressed.
* **Scrollable Output**: The terminal output can be scrolled.
* **Monospace Font**: Uses a consistent monospace font for better readability.
* **Colored Output**: Command responses are displayed with different colors.

## Installation

Ensure you have **Python 3.7+** installed. Install the required dependencies using:

```
pip install PySide6
```

## Usage

Run the script using:

```
python terminalLike.py
```

## Commands

| Command                      | Description                       |
| ---------------------------- | --------------------------------- |
| `<span>help</span>`        | Displays available commands.      |
| `<span>clear</span>`       | Clears the terminal output.       |
| `<span>echo [text]</span>` | Displays the given text in green. |
| Unknown Command              | Shows an error message in red.    |

## Code Structure

This project follows an **MVC architecture**:

### 1. **Model (**`<span><strong>TerminalModel</strong></span>`**)**

* Manages command execution.
* Stores command history.
* Provides navigation for previous/next commands.

### 2. **View (**`<span><strong>TerminalView</strong></span>`**)**

* Handles the graphical UI.
* Displays command output.
* Manages user input interactions.
* Implements an **event filter** for capturing arrow key events.

### 3. **Controller (**`<span><strong>TerminalController</strong></span>`**)**

* Connects the **Model** and **View**.
* Processes user input and updates the output.
* Calls the **Model** to execute commands and retrieve history.

## How to Modify

### Change the Command Logic

Modify the `<span>execute_command</span>` method inside `<span>TerminalModel</span>`:

```
if command == "mycommand":
    return "<span style='color:blue;'>This is a custom command response!</span>"
```

### Customize UI Elements

Modify the `<span>init_ui</span>` method inside `<span>TerminalView</span>` to change font, colors, or layout:

```
self.output.setFont(QFont("Courier", 12))  # Change font size to 12
self.input.setStyleSheet("background-color: #222; color: white;")  # Dark theme input
```

### Add More Features

To extend the functionality, modify the **controller** to support additional input processing.

## Troubleshooting

### `<span>ModuleNotFoundError: No module named 'PySide6'</span>`

Ensure PySide6 is installed:

```
pip install PySide6
```

### UI Does Not Appear

Make sure the script is run directly:

```python-repl
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = TerminalController()
    sys.exit(app.exec())
```

## License

This project is licensed under the **MIT License**.

## Author

Created by AnhTH49
