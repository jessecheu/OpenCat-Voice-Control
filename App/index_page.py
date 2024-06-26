from PySide6.QtWidgets import QMainWindow, QMenu 
from PySide6.QtGui import QAction 
from ui_index import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("OpenCat Voice Control Playground")

        #Hide Widget Menu 
        self.icon_only_widget.setHidden(True)

        #Hide Dropdowns
        self.voice_dropdown.setHidden(True)

        #Connect Buttons to switch to different pages
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.about_1.clicked.connect(self.switch_to_about_page)
        self.about_2.clicked.connect(self.switch_to_about_page)

        self.voice_dashboard.clicked.connect(self.switch_to_voice_dashboard_page)
        self.voice_playground.clicked.connect(self.switch_to_voice_playground_page)
        self.voice_settings.clicked.connect(self.switch_to_voice_settings_page)


        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

        # Connect Buttons to respective context menus
        self.voice_1.clicked.connect(self.voice_context_menu)

    #Methods to switch to different pages
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_about_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_voice_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_voice_playground_page(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_voice_settings_page(self):
        self.stackedWidget.setCurrentIndex(4)
        
    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(5)

    #Methods to show context menus
    def voice_context_menu(self): 
        self.show_custom_context_menu(self.voice_1, ["Voice Dashboard", "Voice Playground", "Voice Settings"]) 

    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)

        #Set styling for the menu
        menu.setStyleSheet(""" 
            QMenu {
                background-color: black;
                           color: white;               
            }
                           
            QMenu:selected {
                background-color: white;
                color: #12B298;             
            }
             """)
        #Adding actions to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        #Show the menu 
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()

        if text == "Voice Dashboard":
            self.switch_to_voice_dashboard_page()
        elif text == "Voice Playground":
            self.switch_to_voice_playground_page()
        elif text == "Voice Settings":
            self.switch_to_voice_settings_page()
        else:
            self.switch_to_dashboard_page()