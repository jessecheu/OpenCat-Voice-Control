# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 852)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 20, 1159, 832))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget1)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:checked { \n"
"	background-color:white;\n"
"	border-radius: 3px;\n"
"}")
        self.layoutWidget2 = QWidget(self.icon_only_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 61, 42))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/Icons/petoi_icon.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.layoutWidget3 = QWidget(self.icon_only_widget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(4, 60, 114, 381))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.dashboard_1 = QPushButton(self.layoutWidget3)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/Icons/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Icons/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.dashboard_1)

        self.about_1 = QPushButton(self.layoutWidget3)
        self.about_1.setObjectName(u"about_1")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/about_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.about_1.setIcon(icon1)
        self.about_1.setIconSize(QSize(100, 16))
        self.about_1.setCheckable(True)
        self.about_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.about_1)

        self.voice_1 = QPushButton(self.layoutWidget3)
        self.voice_1.setObjectName(u"voice_1")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/voice_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.voice_1.setIcon(icon2)
        self.voice_1.setIconSize(QSize(100, 20))
        self.voice_1.setCheckable(True)
        self.voice_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.voice_1)

        self.layoutWidget4 = QWidget(self.icon_only_widget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(0, 750, 114, 81))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.settings_1 = QPushButton(self.layoutWidget4)
        self.settings_1.setObjectName(u"settings_1")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Icons/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon3)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.layoutWidget4)
        self.signout_1.setObjectName(u"signout_1")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Icons/signoutsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_1.setIcon(icon4)
        self.signout_1.setIconSize(QSize(100, 16))
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.signout_1)


        self.horizontalLayout_7.addWidget(self.icon_only_widget)

        self.icon_text_widget = QWidget(self.layoutWidget1)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(241, 0))
        self.icon_text_widget.setMaximumSize(QSize(241, 16777215))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 170, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton { \n"
"	height: 30px;\n"
"	border: none;\n"
"}")
        self.layoutWidget5 = QWidget(self.icon_text_widget)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 750, 221, 84))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.settings_2 = QPushButton(self.layoutWidget5)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setStyleSheet(u"QPushButton { \n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked { \n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Icons/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon5)
        self.settings_2.setIconSize(QSize(100, 16))
        self.settings_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.layoutWidget5)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setStyleSheet(u"QPushButton { \n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked { \n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Icons/signout1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_2.setIcon(icon6)
        self.signout_2.setIconSize(QSize(100, 16))
        self.signout_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.signout_2)

        self.layoutWidget6 = QWidget(self.icon_text_widget)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 20, 221, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/Icons/petoi_icon.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget6)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.voice = QFrame(self.icon_text_widget)
        self.voice.setObjectName(u"voice")
        self.voice.setGeometry(QRect(10, 320, 206, 261))
        self.voice.setFrameShape(QFrame.Shape.StyledPanel)
        self.voice.setFrameShadow(QFrame.Shadow.Raised)
        self.voice_2 = QPushButton(self.voice)
        self.voice_2.setObjectName(u"voice_2")
        self.voice_2.setGeometry(QRect(0, 0, 204, 62))
        self.voice_2.setStyleSheet(u"QPushButton { \n"
"	padding-left:0px\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"	color: #12B298\n"
"}")
        self.voice_2.setIcon(icon2)
        self.voice_2.setIconSize(QSize(200, 60))
        self.voice_2.setCheckable(True)
        self.voice_dropdown = QFrame(self.voice)
        self.voice_dropdown.setObjectName(u"voice_dropdown")
        self.voice_dropdown.setGeometry(QRect(0, 70, 211, 104))
        self.voice_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.voice_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.voice_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.voice_dashboard = QPushButton(self.voice_dropdown)
        self.voice_dashboard.setObjectName(u"voice_dashboard")
        self.voice_dashboard.setCheckable(True)

        self.verticalLayout.addWidget(self.voice_dashboard)

        self.voice_playground = QPushButton(self.voice_dropdown)
        self.voice_playground.setObjectName(u"voice_playground")
        self.voice_playground.setCheckable(True)

        self.verticalLayout.addWidget(self.voice_playground)

        self.voice_settings = QPushButton(self.voice_dropdown)
        self.voice_settings.setObjectName(u"voice_settings")
        self.voice_settings.setCheckable(True)

        self.verticalLayout.addWidget(self.voice_settings)

        self.about_2 = QPushButton(self.icon_text_widget)
        self.about_2.setObjectName(u"about_2")
        self.about_2.setGeometry(QRect(10, 220, 201, 50))
        self.about_2.setStyleSheet(u"QPushButton { \n"
"	padding-left: -66px;\n"
"}\n"
"\n"
"QPushButton:checked { \n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/about_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/Icons/about_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.about_2.setIcon(icon7)
        self.about_2.setIconSize(QSize(200, 45))
        self.about_2.setCheckable(True)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setGeometry(QRect(20, 130, 211, 30))
        self.dashboard_2.setStyleSheet(u"QPushButton { \n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked { \n"
"	background-color: white;\n"
"	border-radius:3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/Icons/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon8)
        self.dashboard_2.setIconSize(QSize(100, 16))
        self.dashboard_2.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.icon_text_widget)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.header_widget = QWidget(self.layoutWidget1)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: none;")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_11.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(131, 131, 131);")

        self.verticalLayout_11.addWidget(self.label_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(315, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/Icons/petoi_icon.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_6)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_12.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget1)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(831, 751))
        self.main_screen_widget.setMaximumSize(QSize(831, 751))
        self.main_screen_widget.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 811, 731))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 0, 391, 61))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.label_7.setFont(font2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 0, 391, 61))
        self.label_8.setFont(font2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 391, 61))
        self.label_9.setFont(font2)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 0, 391, 61))
        self.label_10.setFont(font2)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 0, 391, 61))
        self.label_11.setFont(font2)
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.main_screen_widget)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.voice_2.toggled.connect(self.voice_dropdown.setHidden)
        self.voice_2.toggled.connect(self.voice_1.setChecked)
        self.about_2.toggled.connect(self.about_1.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.about_1.setText("")
        self.voice_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Voice Control", None))
        self.voice_2.setText("")
        self.voice_dashboard.setText(QCoreApplication.translate("MainWindow", u"Voice Dashboard", None))
        self.voice_playground.setText(QCoreApplication.translate("MainWindow", u"Voice Playground", None))
        self.voice_settings.setText(QCoreApplication.translate("MainWindow", u"Voice Settings", None))
        self.about_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.dashboard_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, [Person's Name]", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"[Pet's Name] Home Portal", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Voice Dashboard", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Voice Playground", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Voice Settings", None))
    # retranslateUi

