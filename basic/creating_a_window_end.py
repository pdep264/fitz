import sys

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
        self.setFixedSize(400, 100)  # NB refers to the main window
        self.setWindowTitle('My App')

        button = QPushButton("Press me!")
        # set central widget of the window
        # NB this makes btn fill the window!
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec()