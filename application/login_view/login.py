import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .login_ui import Ui_LoginWindow
from typing import Type
from ..classes.Users.usersManager import UsersManager
from ..classes.Products.productsManager import ProductsManager
from ..dashboard_view.dashboard import DashBoard_Windows
from ..classes.tools.console import console

class LoginWindows(QMainWindow):
    def __init__(self, userManager: Type[UsersManager], productManager: Type[ProductsManager], HomeWindow):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.UserManager = userManager
        self.ProductManager = productManager
        self.dashboard_window = None
        self.HomeWindow = HomeWindow

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def login(self):
        username = self.ui.usernameLine.text()
        password = self.ui.passwordLine.text()

        if (username == "" or password == ""):
            self.ui.message.setText("Please fill all fields")
        else:
            Users = self.UserManager.login(username, password)
            if Users:
                self.dashboard_window = DashBoard_Windows(Users, self.ProductManager, self.HomeWindow)
                self.dashboard_window.show()
                self.hide()
            else:
                self.ui.message.setText("Your identifiant or password is incorrect.")
    
    def cancel(self):
        console.warn("Login canceled")
        self.HomeWindow.show()
        self.hide()