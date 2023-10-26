"""
Here a QLineEdit widget and a QLabel is added to the window.
In the __init__ for the window we connect our line edit .textChanged signal
to the .setText method on the QLabel. Now any time the text changes in the
QLineEdit the QLabel will receive that text to it’s .setText method.
"""

import sys

import layout
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QWidget,
    QVBoxLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Copy Cat')                     # set the window title
        self.setFixedSize(300, 100)                         # set window fixed size
        self.label = QLabel()                               # init label widget
        self.input = QLineEdit()                            # init lineEdit widget
        # the signal + signal = same line!
        self.input.textChanged.connect(self.label.setText)

        my_layout = QVBoxLayout()                           # init layout var
        my_layout.addWidget(self.input)                     # add input widget
        my_layout.addWidget(self.label)                     # add label widget

        container = QWidget()                               # this too is a widget
        container.setLayout(my_layout)                      # set it to defined layout
        self.setCentralWidget(container)                    # set the central widget of the window


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()