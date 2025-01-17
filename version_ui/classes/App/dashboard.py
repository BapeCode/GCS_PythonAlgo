from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from version_ui.classes.UI.dashboard_ui import Ui_Dashboard
from ..Products.productsManager import ProductsManager

class DashBoard_Windows(QMainWindow):
    def __init__(self, Users, ProductManager):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        self.productManager = ProductManager
        self.Users = Users
        self.ui.title.setText(f"GESTIONIX : Connected as ({self.Users.username})")

        self.view()
   
        # Connect Buttons
        self.ui.logoutButton.clicked.connect(self.logout)

    def logout(self):
        self.close()

    def view(self):
        if self.ui.scrollAreaWidgetContents.layout():
            QWidget().setLayout(self.ui.scrollAreaWidgetContents.layout())
    
        # Create new vertical layout for scroll area
        layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        layout.setSpacing(5)
        layout.setContentsMargins(5, 3, 5, 3)
        allProduct = self.productManager.load_products()

        print(allProduct)
        
        # Create multiple container items
        for i in range(10):  # Create 10 items as example
            containerItem = QWidget(self.ui.scrollAreaWidgetContents)
            containerItem.setObjectName(f"containerItems_{i}")
            containerItem.setMinimumSize(QSize(0, 50))
            containerItem.setMaximumSize(QSize(16777215, 50))
            
            # Create horizontal layout for the container
            horizontalLayout = QHBoxLayout(containerItem)
            horizontalLayout.setObjectName(f"horizontalLayout_{i}")
            horizontalLayout.setContentsMargins(5, 3, 5, 3)
            
            # Name label
            nameLabel = QLabel(containerItem)
            nameLabel.setText(f"Product {i}")
            horizontalLayout.addWidget(nameLabel)
            
            # Price label
            priceLabel = QLabel(containerItem)
            priceLabel.setText(f"{i+1}.99€")
            horizontalLayout.addWidget(priceLabel)
            
            # Stock label
            stockLabel = QLabel(containerItem)
            stockLabel.setText(f"x{i*10}")
            horizontalLayout.addWidget(stockLabel)
            
            # Date label
            dateLabel = QLabel(containerItem)
            dateLabel.setText("03/01/2024 - 09:20")
            horizontalLayout.addWidget(dateLabel)
            
            # Action combo box
            actionCombo = QComboBox(containerItem)
            actionCombo.addItem("Supprimer")
            actionCombo.addItem("Modifier")
            horizontalLayout.addWidget(actionCombo)
            
            # Add the container to the main layout
            layout.addWidget(containerItem)
        
        # Add stretch at the end to push items to the top
        layout.addStretch()
