from PyQt6.QtWidgets import QApplication, QWidget
import sys

# sys.argv can be a param here IF cmdline args control QT
# BUT if not used the [] is required.
app = QApplication(sys.argv)

window = QWidget()
window.show()
app.exec()