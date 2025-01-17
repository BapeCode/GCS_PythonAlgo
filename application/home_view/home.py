import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .home_ui import Ui_MainWindow
from ..login_view.login import LoginWindows
from ..register_view.register import RegisterWindows
from typing import Type
<<<<<<< Updated upstream:application/home_view/home.py
from ..classes.Users.usersManager import UsersManager
from ..classes.Products.productsManager import ProductsManager
=======
from ..Users.usersManager import UsersManager
from ..Products.productsManager import ProductsManager
>>>>>>> Stashed changes:version_ui/classes/App/home.py


class HomeWindow(QMainWindow):
    def __init__(self, UserManager: Type[UsersManager], ProductManager: Type[ProductsManager]):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user_manager = UserManager
        self.product_manager = ProductManager
        self.login_window = None
        self.register_window = None


        # Connect Buttons
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)
        self.ui.exitButton.clicked.connect(self.exit)

    def login(self):
<<<<<<< Updated upstream:application/home_view/home.py
        self.login_window = LoginWindows(self.user_manager, self.product_manager, self)
=======
        self.login_window = LoginWindows(self.user_manager, self.product_manager)
>>>>>>> Stashed changes:version_ui/classes/App/home.py
        self.login_window.show()
        self.hide()

    def register(self):
        self.register_window = RegisterWindows(self.user_manager, self)
        self.register_window.show()
        self.hide()
        

    def exit(self):
        sys.exit()
