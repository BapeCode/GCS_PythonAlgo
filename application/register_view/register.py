import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .register_ui import Ui_RegisterWindow
from typing import Type
from ..classes.Users.usersManager import UsersManager
from ..classes.tools.console import console


class RegisterWindows(QMainWindow):
    def __init__(self, userManager: Type[UsersManager], HomeWindow):
        super().__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.UserManager = userManager
        self.HomeWindow = HomeWindow

        self.ui.registerButton.clicked.connect(self.register)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def register(self):
        email = self.ui.emailButton.text()
        username = self.ui.usernameButton.text()
        password = self.ui.passwordButton.text()

        if (email == "" or username == "" or password == ""):
            self.ui.succes.setText("Please fill all fields")
        else:
            if (self.UserManager.register(username, email, password)):
                console.success(f"New user has been created '{username}'")
                self.ui.succes.setText("Welcome")
            else:
                self.ui.succes.setText("Password is too weak. Please choose a stronger password.")

    def cancel(self):
        console.warn("Register canceled")
        self.HomeWindow.show()
        self.hide()