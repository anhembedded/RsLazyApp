import sys
from PySide6.QtWidgets import (QApplication, QWidget, QTabWidget,
                               QVBoxLayout, QPushButton, QLabel)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tab_widget)

        # Create two initial tabs
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(QLabel("This is Tab 1"))
        self.tab_widget.addTab(tab1, "Tab 1")

        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(QLabel("This is Tab 2"))
        self.tab_widget.addTab(tab2, "Tab 2")

        # Button to add widget to Tab 2
        add_button = QPushButton("Add Widget to Tab 2")
        add_button.clicked.connect(self.add_widget_to_tab2)
        self.layout.addWidget(add_button)

    def add_widget_to_tab2(self):
        # Get the index of Tab 2
        tab_index = self.tab_widget.indexOf(self.tab_widget.widget(1)) # index 1 is the 2nd tab.
        if tab_index == -1:
            return # Tab not found

        # Get the widget of Tab 2
        tab_widget = self.tab_widget.widget(tab_index)

        # Get the layout of Tab 2
        tab_layout = tab_widget.layout()

        # Create the new widget
        new_widget = QPushButton("New Widget in Tab 2")

        # Add the new widget to the layout
        tab_layout.addWidget(new_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())