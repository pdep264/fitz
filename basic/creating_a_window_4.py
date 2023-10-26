import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)


# Subclass QMainWindow to customise app's main window
class MainWindow(QMainWindow):
    def __init__(self):
        # when you subclass a QT class you must always call super.__init__()
        super().__init__()

        self.setWindowTitle('My App')

        button = QPushButton("Press me!")

        # set central widget of the window
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec()