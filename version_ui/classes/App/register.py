import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..UI.register_ui import Ui_RegisterWindow


class RegisterWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
