import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .add_products_ui import Ui_AddProducts
from typing import Type
from ..classes.Users.usersManager import UsersManager
from ..classes.Products.productsManager import ProductsManager
from ..classes.tools.console import console

class AddWindows(QMainWindow):
    def __init__(self, User, productManager: Type[ProductsManager], view):
        super().__init__()
        self.ui = Ui_AddProducts()
        self.ui.setupUi(self)
        self.User = User
        self.ProductManager = productManager
        self.view = view
        
        # Connection button
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def save(self):
        productName = str(self.ui.productLine.text())
        productQuantity = int(self.ui.stockBox.text())
        productPrice = float(self.ui.priceBox.text().replace(',', '.'))

        self.ProductManager.add_product(productName, productPrice, productQuantity, self.User.username)
        self.view(self.ProductManager.load_products(self.User.username))
        self.hide()

    def cancel(self):
        console.warn("Add products canceled")
        self.hide()
        