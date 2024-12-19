import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..UI.home_ui import Ui_MainWindow
from .login import LoginWindows
from .register import RegisterWindows


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.login_window = None
        self.register_window = None


        # Connect Buttons
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)
        self.ui.exitButton.clicked.connect(self.exit)

    def login(self):
        self.login_window = LoginWindows()
        self.login_window.show()

    def register(self):
        self.register_window = RegisterWindows()
        self.register_window.show()
        

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec_())