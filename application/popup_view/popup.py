from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .popup_ui import Ui_Popup


class Popup_Window(QMainWindow):
    def __init__(self, text):
        super().__init__()
        self.ui = Ui_Popup()
        self.ui.setupUi(self)

        self.ui.text.setText(text)
        self.ui.closeButton.clicked.connect(self.close)

    def close(self):
        self.hide()
