# JsonEditorWidget - A PySide6 JSON Editor Widget

`JsonEditorWidget` is a customizable, syntax-highlighted JSON editor widget for PySide6 applications. It provides a user-friendly interface for displaying, editing, and validating JSON data. The widget supports zooming, syntax highlighting, and error handling, making it ideal for applications that require JSON manipulation.

---

## Features

* **Syntax Highlighting** : JSON keys, strings, numbers, and keywords are color-coded for better readability.
* **Editable JSON** : Users can directly modify JSON data in the widget.
* **Zoom Functionality** : Zoom in and out using `Ctrl + Mouse Wheel`.
* **Error Handling** : Displays error messages for invalid JSON.
* **Pretty Printing** : Automatically formats JSON with indentation.
* **Dark Theme** : Modern dark theme with customizable styling.

---

## Installation

1. Ensure you have Python installed (3.7 or higher).
2. Install PySide6:
   bash

   Copy

   ```powershell
   pip install PySide6
   ```
3. Copy the `JsonEditorWidget` class into your project or import it from a module.

---

## Usage

### Basic Integration

1. Add the `JsonEditorWidget` to your PySide6 application:
   python

   Copy

   ```python
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
   from json_editor_widget import JsonEditorWidget  # Replace with the actual module name

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           self.setWindowTitle("JSON Editor Example")
           self.resize(800, 600)

           # Create a central widget and layout
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           layout = QVBoxLayout(central_widget)

           # Add the JsonEditorWidget
           self.editor = JsonEditorWidget()
           layout.addWidget(self.editor)

           # Load sample JSON data
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
           self.editor.set_json(sample_data)

   if __name__ == "__main__":
       app = QApplication([])
       window = MainWindow()
       window.show()
       app.exec()
   ```
2. Run your application, and you'll see the JSON editor widget in action.

---

### Key Methods

* **`set_json(data)`** : Load JSON data into the editor.
  python

  Copy

```
  editor.set_json({"key": "value"})
```

* **`get_json()`** : Retrieve and validate JSON data from the editor. Returns `None` if the JSON is invalid.
  python

  Copy

```python
  json_data = editor.get_json()
  if json_data:
      print(json_data)
```

* **`validate_json()`** : Check if the current content is valid JSON.
  python

  Copy

```python
  if editor.validate_json():
      print("Valid JSON!")
  else:
      print("Invalid JSON!")
```

* **`clear()`** : Clear the editor.
  python

  Copy

```
  editor.clear()
```

* **`append_output(text, color=None)`** : Append text to the output area with optional color (hex format).
  python

  Copy

```
  editor.append_output("This is a message\n", "#4EC9B0")
```

---

### Zoom Functionality

* Hold the `Ctrl` key and scroll the mouse wheel up to zoom in.
* Hold the `Ctrl` key and scroll the mouse wheel down to zoom out.

---

### Customization

#### Styling

You can customize the appearance of the widget by modifying the `init_ui` method or using external stylesheets.

Example:

python

Copy

```python
self.text_edit.setStyleSheet("""
    QTextEdit {
        background-color: #000000;
        color: #00FF00;
        border: 1px solid #333333;
    }
""")
```

#### Font

Change the font by modifying the `QFont` initialization in `init_ui`:

python

Copy

```
font = QFont("Consolas", 12)  # Use Consolas font with size 12
self.text_edit.setFont(font)
```

#### Syntax Highlighting Colors

Modify the colors in the `JsonHighlighter` class:

python

Copy

```
key_format.setForeground(QColor("#FF0000"))  # Red for JSON keys
string_format.setForeground(QColor("#00FF00"))  # Green for JSON strings
```

---

### Example Commands

Here’s an example of how you can handle JSON data:

python

Copy

```
def handle_json():
    json_data = editor.get_json()
    if json_data:
        print("Retrieved JSON Data:", json_data)
    else:
        print("Invalid JSON data!")
```

---

### Error Handling

* Invalid JSON is highlighted with red underlines (can be extended further).
* Errors are displayed in a `QMessageBox`.

---

### Keyboard Shortcuts

* **Ctrl + Mouse Wheel Up** : Zoom in.
* **Ctrl + Mouse Wheel Down** : Zoom out.

---

### Dependencies

* PySide6

---

### License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

---

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---

Enjoy using `JsonEditorWidget` in your PySide6 applications! 🚀
