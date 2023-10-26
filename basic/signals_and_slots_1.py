import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)


def the_button_was_clicked():
    # the slot
    print('the button was clicked')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        button = QPushButton("Press me!")
        # the signal
        button.clicked.connect(the_button_was_clicked)
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec()