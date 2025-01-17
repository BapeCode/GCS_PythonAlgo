import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..UI.login_ui import Ui_LoginWindow
from typing import Type
from ..Users.usersManager import UsersManager
from ..Products.productsManager import ProductsManager
from .dashboard import DashBoard_Windows


class LoginWindows(QMainWindow):
    def __init__(self, userManager: Type[UsersManager], productManager: Type[ProductsManager]):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.UserManager = userManager
        self.ProductManager = productManager
        self.dashboard_window = None

        self.ui.loginButton.clicked.connect(self.login)

    def login(self):
        username = self.ui.username_line.text()
        password = self.ui.password_line.text()

        if (username == "" or password == ""):
            self.ui.message.setText("Please fill all fields")
        else:
            Users = self.UserManager.login(username, password)
            if Users:
                self.hide()
                self.dashboard_window = DashBoard_Windows(Users, self.ProductManager)
                self.dashboard_window.show()
            else:
                self.ui.message.setText("Your identifiant or password is incorrect.")
        