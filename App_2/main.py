from PySide6.QtWidgets import QApplication
from index_page import MySideBar

import sys

app = QApplication(sys.argv)

window = MySideBar()

window.show()

app.exec()