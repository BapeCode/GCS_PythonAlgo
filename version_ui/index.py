import sys
from .classes.Products.productsManager import ProductsManager
from .classes.Users.usersManager import UsersManager
from .classes.App.home import HomeWindow
from PySide6.QtWidgets import QApplication
from termcolor import colored
from .classes.tools.console import console

class GestionApp:

    def __init__(self):
        self.usersManager = UsersManager()
        self.productsManager = ProductsManager()


        console.debug("Loading Gestion App")
    

    def run(self):
        app = QApplication(sys.argv)
        window = HomeWindow()
        window.show()
        sys.exit(app.exec())

if __name__ == '__main__':
    console.warn("Application Started")
    app = GestionApp()
    app.run()