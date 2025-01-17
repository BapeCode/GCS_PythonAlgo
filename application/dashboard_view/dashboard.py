from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from .dashboard_ui import Ui_Dashboard
from ..classes.tools.console import console
from ..add_products_view.addProducts import AddWindows
from ..pdf_view.pdf_view import PdfPreviewDialog
import sys

class DashBoard_Windows(QMainWindow):
    def __init__(self, Users, ProductManager, HomeWindow):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        self.productManager = ProductManager
        self.Users = Users
        self.HomeWindow = HomeWindow

        self.add_window = None
        self.home_window = None

        
        # Connect Buttons
        self.ui.actionExit.triggered.connect(self.exitCb)
        self.ui.actionLogout.triggered.connect(self.logout)

        self.ui.addButtons.clicked.connect(self.addProducts)
        self.ui.sortCombo.currentTextChanged.connect(lambda text: self.sort(text))
        self.ui.searchLine.textEdited.connect(self.search)
        self.ui.viewOrder.clicked.connect(self.on_order_selected)

        # Setup Tableau
        self.setup_table(
            self.ui.tableWidget,
            ['Product name', 'Product price', 'Product stock', 'Stock price ($)', 'Options']
        )
        self.setup_table(
            self.ui.tableWidget_2,
            ['Customer', 'Product name', 'Total price', 'Quantity', 'Date', 'Status']
        )


        self.view_products(self.productManager.load_products(self.Users.username))
        self.view_order(self.productManager.load_order(self.Users.username))

    def setup_table(self, table, headers, stretch_coloumn=0):
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        table.setRowCount(0)
        
        # Configuration des en-têtes
        table.setColumnCount(len(headers))
        for idx, header_text in enumerate(headers):
            table.setHorizontalHeaderItem(idx, QTableWidgetItem(header_text))
        
        # Ajustement des colonnes
        header = table.horizontalHeader()
        header.setSectionResizeMode(stretch_coloumn, QHeaderView.ResizeMode.Stretch)
        for i in range(len(headers)):
            if i != stretch_coloumn:
                header.setSectionResizeMode(i, QHeaderView.ResizeMode.Fixed)

    def view_order(self, orders):
        self.ui.tableWidget_2.setRowCount(0)
        
        for row, order in enumerate(orders):
            self.ui.tableWidget_2.insertRow(row)
            
            # Ajout des données
            columns_data = [
                order.customer,
                order.name,
                f"{float(order.price) * int(order.stock):.2f}€",
                str(order.stock),
                order.date
            ]
            
            for col, data in enumerate(columns_data):
                self.ui.tableWidget_2.setItem(row, col, QTableWidgetItem(data))
            
            # Widget de statut
            action_callback = lambda text, p=order: self.actionOrder(p, text) if text != order.status else None
            status_widget = self.create_action_widget(
                [order.status, "In await" if order.status == "Processed" else "Processed", "Cancel"],
                action_callback,
                initial_value=order.status
            )
            self.ui.tableWidget_2.setCellWidget(row, 5, status_widget)
        
    def view_products(self, products):
        self.ui.tableWidget.setRowCount(0)
        
        for row, product in enumerate(products):
            self.ui.tableWidget.insertRow(row)
            
            # Ajout des données
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(product.name))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(f"{product.price}€"))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(product.stock)))
            
            # Calcul et affichage du coût total
            stock_cost = float(product.price) * int(product.stock)
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(f"{stock_cost:.2f}€"))
            
            # Widget d'action
            action_callback = lambda text, p=product: self.actionItems(p, text) if text != "Action" else None
            action_widget = self.create_action_widget(["Action", "Supprimer"], action_callback)
            self.ui.tableWidget.setCellWidget(row, 4, action_widget)

    def on_order_selected(self):
        selected_items = self.ui.tableWidget_2.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            if (self.productManager.get_product_exist(self.ui.tableWidget_2.item(row, 1).text(), self.ui.tableWidget_2.item(row, 3).text())):
                self.selected_order = {
                    'customer': self.ui.tableWidget_2.item(row, 0).text(),
                    'product': self.ui.tableWidget_2.item(row, 1).text(),
                    'total_price': self.ui.tableWidget_2.item(row, 2).text(),
                    'quantity': self.ui.tableWidget_2.item(row, 3).text(),
                    'date': self.ui.tableWidget_2.item(row, 4).text()
                }
                dialog = PdfPreviewDialog(self.selected_order, self.Users)
                dialog.exec_()
            else:
                QMessageBox.warning(self, "Attention", "You can't preview a order. Because you don't have any quantity of this products")
        else:
            QMessageBox.warning(self, "Attention", "Veuillez sélectionner une commande d'abord.")
            self.selected_order = None

    def create_action_widget(self, items, callback, initial_value="Action"):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        combo = QComboBox()
        combo.addItems(items)
        if initial_value != "Action":
            index = combo.findText(initial_value)
            if index >= 0:
                combo.setCurrentIndex(index)
        combo.currentTextChanged.connect(callback)
        layout.addWidget(combo)
        layout.setContentsMargins(5, 0, 5, 0)
        return widget

    def actionItems(self, product, action):
        if action == "Supprimer":
            print(f"Suppression du produit: {product.name}")
            self.productManager.delete_product(product.name)
            self.view_products(self.productManager.load_products(self.Users.username))

    def actionOrder(self, order, action):
        productExit = self.productManager.get_product_exist(order.name, order.stock)

        if (productExit):
            self.productManager.change_status_order(action, order)
            self.view_order(self.productManager.load_)
        else:
            console.debug("You can't")
            QMessageBox.warning(self, "Attention", "You can't because this product has not any more in the stock.")

    def exitCb(self):
        console.success("Thank you for your visiting. See you soon !")
        self.close()
        sys.exit()

    def logout(self):
        console.debug(f"{self.Users.username} has been logout.")
        self.HomeWindow.show()
        self.hide()
        self.Users = None
        
    def addProducts(self):
        self.add_window = AddWindows(self.Users, self.productManager, self.view_products)
        self.add_window.show()

    def sort(self, sortType):
        if (sortType == "Sort stock"): return
        self.productManager.sort_products(sortType)

        self.view_products(self.productManager.load_products(self.Users.username))
    
    def search(self):
        searchTarget = self.ui.searchLine.text()
        
        results = [product for product in self.productManager.load_products(self.Users.username) if product.name.lower().startswith(searchTarget.lower())]
        self.view_products(results)