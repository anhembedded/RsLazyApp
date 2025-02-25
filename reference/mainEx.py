import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTextEdit,
    QMdiArea,
    QMdiSubWindow,
    QMessageBox,
    QGraphicsView,
    QGraphicsScene,
    QComboBox,
    QStyleFactory,
    QMenu,  # Import QMenu
)
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QWheelEvent, QPalette, QColor, QAction  # Import QAction


class ZoomableGraphicsView(QGraphicsView):
    """A QGraphicsView that supports zooming with the mouse wheel."""

    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setRenderHints(self.renderHints())  # Keep existing render hints
        self.setOptimizationFlags(
            self.optimizationFlags()
        )  # keep existing Optimization Flags
        self.setTransformationAnchor(
            QGraphicsView.AnchorUnderMouse
        )  # zoom in on the mouse
        self.setResizeAnchor(
            QGraphicsView.AnchorUnderMouse
        )  # keep same relative position on resize
        self.zoom_factor = 1.0
        self.zoom_step = 1.25  # 25% zoom increment

    def wheelEvent(self, event: QWheelEvent):
        """Handles mouse wheel events for zooming."""
        delta = event.angleDelta().y()
        if delta > 0:
            self.zoom_in()
        elif delta < 0:
            self.zoom_out()
        event.accept()

    def zoom_in(self):
        """Zooms in the view."""
        self.zoom_factor *= self.zoom_step
        self.scale(self.zoom_step, self.zoom_step)

    def zoom_out(self):
        """Zooms out the view."""
        self.zoom_factor /= self.zoom_step
        self.scale(1 / self.zoom_step, 1 / self.zoom_step)


class SubWindow(QWidget):
    """A simple reusable subwindow for our MDI area."""

    def __init__(self, title, content_widget=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)

        layout = QVBoxLayout()
        self.label = QLabel(title)  # Use the title as a label (for demo)
        layout.addWidget(self.label)

        if content_widget:
            layout.addWidget(content_widget)

        self.setLayout(layout)

    def closeEvent(self, event):
        # Example: Confirmation dialog before closing
        reply = QMessageBox.question(
            self,
            "Confirm Close",
            "Are you sure you want to close this window?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            event.accept()  # Allow the window to close
        else:
            event.ignore()  # Prevent the window from closing

    def contextMenuEvent(self, event):
        """Handles right-click context menu events."""
        menu = QMenu(self)

        # Add actions to the menu
        close_action = QAction("Close", self)
        close_action.triggered.connect(self.close)
        menu.addAction(close_action)

        maximize_action = QAction("Maximize", self)
        maximize_action.triggered.connect(self.maximize_window)
        menu.addAction(maximize_action)

        #You can add here other actions
        # ...

        # Show the menu at the cursor's position
        menu.exec(event.globalPos())


    def maximize_window(self):
        """Maximizes the subwindow within the MDI area."""
        #We need to go up the parent chain to the QMdiSubWindow.
        sub_window = self.parent()
        while sub_window is not None and not isinstance(sub_window, QMdiSubWindow):
            sub_window = sub_window.parent()

        if sub_window:
            sub_window.showMaximized()


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MDI Area with Context Menu")
        self.setGeometry(100, 100, 800, 600)

        # Create the MDI area
        self.mdi_area = QMdiArea()
        self.mdi_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdi_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdi_area)

        # --- Theme Selection ---
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(QStyleFactory.keys())  # Add available styles
        self.theme_combo.currentTextChanged.connect(self.change_theme)

        theme_label = QLabel("Select Theme:")
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch() # Push the theme selection to the left

        # --- Buttons ---
        button_layout = QHBoxLayout()

        # Button to add a new subwindow
        add_button = QPushButton("Add Subwindow")
        add_button.clicked.connect(self.add_subwindow)
        button_layout.addWidget(add_button)

        add_custom_button = QPushButton("Add Custom Subwindow")
        add_custom_button.clicked.connect(self.add_custom_subwindow)
        button_layout.addWidget(add_custom_button)

        add_textedit_button = QPushButton("Add TextEdit Subwindow")
        add_textedit_button.clicked.connect(self.add_textedit_subwindow)
        button_layout.addWidget(add_textedit_button)

        add_zoomable_button = QPushButton("Add Zoomable Subwindow")
        add_zoomable_button.clicked.connect(self.add_zoomable_subwindow)
        button_layout.addWidget(add_zoomable_button)

        # Button to tile subwindows
        tile_button = QPushButton("Tile Subwindows")
        tile_button.clicked.connect(self.mdi_area.tileSubWindows)
        button_layout.addWidget(tile_button)

        # Button to cascade subwindows
        cascade_button = QPushButton("Cascade Subwindows")
        cascade_button.clicked.connect(self.mdi_area.cascadeSubWindows)
        button_layout.addWidget(cascade_button)

        # Button to close all subwindows
        close_all_button = QPushButton("Close All")
        close_all_button.clicked.connect(self.close_all_subwindows)
        button_layout.addWidget(close_all_button)

        # --- Layout ---
        main_layout = QVBoxLayout()
        main_layout.addLayout(theme_layout)  # Add theme selection
        main_layout.addLayout(button_layout)  # Add buttons
        main_layout.addWidget(self.mdi_area)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.subwindow_count = 0

    def change_theme(self, style_name):
        """Changes the application's style."""
        QApplication.setStyle(style_name)
        # Force a style update on all widgets
        self.updateStyle()

    def updateStyle(self):
        """Recursively updates the style of the window and all its children."""
        self.style().polish(self) #update main window
        for child in self.findChildren(QWidget):
            self.style().polish(child) #update all children

    def add_subwindow(self):
        """Adds a simple subwindow."""
        self.subwindow_count += 1
        sub_window_content = SubWindow(f"Subwindow {self.subwindow_count}")

        # Create the QMdiSubWindow and set its widget and context menu policy
        sub_window = QMdiSubWindow()
        sub_window.setWidget(sub_window_content)
        sub_window.setAttribute(Qt.WA_DeleteOnClose)
        # sub_window.setContextMenuPolicy(Qt.CustomContextMenu) #No needed, the context menu is managed by SubWindow
        # sub_window.customContextMenuRequested.connect(sub_window_content.contextMenuEvent) #No needed

        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()


    def add_custom_subwindow(self):
        """Adds a subwindow with custom content (QLineEdit)."""
        self.subwindow_count += 1
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter text here...")
        sub_window_content = SubWindow(
            f"Custom Subwindow {self.subwindow_count}", content_widget=line_edit
        )

        #QMdiSubWindow
        sub_window = QMdiSubWindow()
        sub_window.setWidget(sub_window_content)
        sub_window.setAttribute(Qt.WA_DeleteOnClose)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

    def add_textedit_subwindow(self):
        """Adds a subwindow containing a QTextEdit."""
        self.subwindow_count += 1
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("Type your text here...")

        sub_window_content = SubWindow(
            f"TextEdit Subwindow {self.subwindow_count}", content_widget=text_edit
        )

        #QMdiSubWindow
        sub_window = QMdiSubWindow()
        sub_window.setWidget(sub_window_content)
        sub_window.setAttribute(Qt.WA_DeleteOnClose)  # Crucial
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

    def add_zoomable_subwindow(self):
        """Adds a subwindow with a zoomable QGraphicsView."""
        self.subwindow_count += 1

        # Create a QGraphicsScene
        scene = QGraphicsScene(self)
        # Add some items to the scene (for demonstration)
        scene.addRect(-50, -50, 100, 100, Qt.red)
        scene.addEllipse(20, 20, 60, 80, Qt.blue)
        scene.addLine(-20, -20, 80, 50, Qt.green)
        text_item = scene.addText("Zoom Me!",)
        text_item.setPos(-30, 10)

        # Create a ZoomableGraphicsView and set the scene
        view = ZoomableGraphicsView(scene)
        view.setDragMode(QGraphicsView.ScrollHandDrag)  # Enable Drag

        sub_window_content = SubWindow(
            f"Zoomable Subwindow {self.subwindow_count}", content_widget=view
        )

        # Create a QMdiSubWindow and set the view as its widget
        sub_window = QMdiSubWindow()
        sub_window.setWidget(sub_window_content)
        sub_window.setWindowTitle(f"Zoomable Subwindow {self.subwindow_count}")
        sub_window.setAttribute(Qt.WA_DeleteOnClose)

        self.mdi_area.addSubWindow(sub_window)

        sub_window.show()
        sub_window.resize(400, 300)  # give it an initial size

    def close_all_subwindows(self):
        """Closes all subwindows in the MDI area."""
        self.mdi_area.closeAllSubWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())