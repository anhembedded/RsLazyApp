import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader() #Set up a loader object

app = QtWidgets.QApplication(sys.argv)
window = loader.load("views\pySide6View\mainWindow\mainWindow.ui", None) #Load the ui - happens at run time!

def do_something() :
    print(window.full_name_line_edit.text(),"is a ", window.occupation_line_edit.text())

#Changing the properties in the form
window.setWindowTitle("RS_LazyApp_MainWindow")

#Accessing widgets in the form
window.show()
app.exec()