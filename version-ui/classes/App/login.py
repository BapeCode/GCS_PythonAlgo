import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..UI.login_ui import Ui_LoginWindow

class LoginWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.login)

    def login(self):
        username = self.ui.username_line.text()
        password = self.ui.password_line.text()
        print(username, password)

        if (username == "" or password == ""):
            self.ui.message.setText("Please fill all fields")
        else:
            print("Welcome")
