from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_voice_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("OpenCat Voice Control")
        self.voice_send_button.clicked.connect(self.do_something)

        profile_icon = QIcon(":/images/favicon/icons8-user-account-100.png")
        self.pushButton_2.setIcon(profile_icon)

    def do_something(self):
        print(self.voice_line_edit.text(), " is received")