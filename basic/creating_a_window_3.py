from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# sys.argv can be a param here IF cmdline args control QT
# BUT if not used the [] is required.
app = QApplication(sys.argv)

window = QMainWindow()
'''QMainWindow gives access to: 
    sizing, toolbars, menus, statusbar, dockable widgets etc.
'''

window.show()
app.exec()