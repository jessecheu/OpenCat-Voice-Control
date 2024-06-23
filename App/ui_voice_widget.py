# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'voice_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)
import resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(567, 571)
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 540, 256, 24))
        self.voice_signal_list = QListWidget(Widget)
        self.voice_signal_list.setObjectName(u"voice_signal_list")
        self.voice_signal_list.setGeometry(QRect(40, 130, 511, 391))
        self.preset_command_dropdown = QComboBox(Widget)
        self.preset_command_dropdown.addItem("")
        self.preset_command_dropdown.addItem("")
        self.preset_command_dropdown.addItem("")
        self.preset_command_dropdown.addItem("")
        self.preset_command_dropdown.setObjectName(u"preset_command_dropdown")
        self.preset_command_dropdown.setGeometry(QRect(130, 100, 321, 31))
        self.preset_send_button = QPushButton(Widget)
        self.preset_send_button.setObjectName(u"preset_send_button")
        self.preset_send_button.setGeometry(QRect(460, 100, 75, 24))
        self.voice_send_button = QPushButton(Widget)
        self.voice_send_button.setObjectName(u"voice_send_button")
        self.voice_send_button.setGeometry(QRect(460, 70, 75, 24))
        self.voice_label = QLabel(Widget)
        self.voice_label.setObjectName(u"voice_label")
        self.voice_label.setGeometry(QRect(90, 80, 29, 16))
        self.voice_line_edit = QLineEdit(Widget)
        self.voice_line_edit.setObjectName(u"voice_line_edit")
        self.voice_line_edit.setGeometry(QRect(130, 70, 321, 31))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Clear", None))
        self.preset_command_dropdown.setItemText(0, QCoreApplication.translate("Widget", u"Sit", None))
        self.preset_command_dropdown.setItemText(1, QCoreApplication.translate("Widget", u"Stand", None))
        self.preset_command_dropdown.setItemText(2, QCoreApplication.translate("Widget", u"Laydown", None))
        self.preset_command_dropdown.setItemText(3, QCoreApplication.translate("Widget", u"New Item", None))

        self.preset_command_dropdown.setCurrentText("")
        self.preset_command_dropdown.setPlaceholderText(QCoreApplication.translate("Widget", u"Select a preset Command", None))
        self.preset_send_button.setText(QCoreApplication.translate("Widget", u"Send Preset", None))
        self.voice_send_button.setText(QCoreApplication.translate("Widget", u"Send", None))
        self.voice_label.setText(QCoreApplication.translate("Widget", u"Voice", None))
        self.voice_line_edit.setText("")
    # retranslateUi

