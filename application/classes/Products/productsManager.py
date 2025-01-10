from ..tools.fileManager import FileManager
from .products import Product
from .order import Order
import time
import termcolor
import json
from ..tools.console import console

class ProductsManager: 
    def __init__(self):
        self.products = []
        self.order = []
        self.PRODUCT_FILE = "./data/products.csv"
        self.ORDER_FILE = "./data/order.json"

        console.debug("Products Manager Loaded")

    def load_products(self, user):
        try:
            file = FileManager().load_file(self.PRODUCT_FILE)
            products = [line.strip().split(",") for line in file[1:]]
            user_products = [product for product in products if product[4] == user]
            all_products = [Product(product[0], product[1], product[2], product[3], product[4]) for product in products]
            user_objects = [Product(product[0], product[1], product[2], product[3], product[4]) for product in user_products]
            self.products = all_products 
            return user_objects
        except FileNotFoundError:
            console.error("An error has been arrived : File not found")
            return []
             
    def save_products(self):
        data = [
            ['Name', "Price", "Stock", "Date", "User"],
            *[[product.name, product.price, product.stock, product.date, product.user] for product in self.products]
        ]
        FileManager().save_file(self.PRODUCT_FILE, data)

    def add_product(self, name, price, stock, user):
        current_time = time.localtime()
        date = f"{current_time.tm_mday}/{current_time.tm_mon}/{current_time.tm_year} - {current_time.tm_hour}:{current_time.tm_min}"

        # Vérifier si le produit existe déjà
        for existing_product in self.products:
            if existing_product.name == name:
                existing_product.stock = int(existing_product.stock)
                existing_product.stock += int(stock)
                self.save_products()
                console.success(f"Added {stock} units to existing product '{name}'.")
                return  # Important: sortir de la fonction si le produit est trouvé
        
        # Si le produit n'existe pas, en créer un nouveau
        new_product = Product(name, price, stock, date, user)
        self.products.append(new_product)
        self.save_products()
        console.success(f"Product '{name}' added successfully.")

    def delete_product(self, name):
        self.products = [product for product in self.products if product.name != name]
        self.save_products()
        console.success(f"Product {name} deleted successfully.")

    def sort_products(self, sort_type):
        if sort_type == "Name":
            self.products.sort(key=lambda product: product.name)
        elif sort_type == "Price":
            self.products.sort(key=lambda product: product.price)
        elif sort_type == "Stock":
            self.products.sort(key=lambda product: product.stock)
        elif sort_type == "Date":
            self.products.sort(key=lambda product: product.date)
        else:
            print("Invalid sort type")
            return

        self.save_products()

    # Order method

    def save_order(self):
        with open(self.ORDER_FILE, "r") as file:
            orders = json.load(file)
        updated_orders = []
        for order in orders:

            updated_order = order  

            for new_order in self.order:

                if (order['customer'] == new_order.customer and 
                    order['productName'] == new_order.name and 
                    order['date'] == new_order.date):

                    updated_order = {
                        "customer": new_order.customer,
                        "productName": new_order.name,
                        "productQuantity": new_order.stock,
                        "productPrice": new_order.price,
                        "date": new_order.date,
                        "status": new_order.status,
                        "commercial": new_order.commercial
                    }
            updated_orders.append(updated_order)
        with open(self.ORDER_FILE, "w") as file:
            json.dump(updated_orders, file, indent=2)

    def load_order(self, user):
        try:
            with open(self.ORDER_FILE, "r") as file:
                data = json.load(file)
                orders = [Order(order['customer'], order['productName'], order['productPrice'], order['productQuantity'], order['date'], order['status'], order['commercial']) for order in data if user == order['commercial']]
                self.order = orders
                return self.order
                    
                
        except FileNotFoundError:
            console.error(f"Le fichier {self.ORDER_FILE} n'existe pas")
            return []
        except json.JSONDecodeError:
            console.error("Erreur de décodage JSON")
            return []
       
    def get_product_exist(self, product, quantity):
        for data in self.products:
            if (data.name == product):
                if (int(data.stock) >= int(quantity)):
                    return True
                
        return False

    def change_status_order(self, status, order):
        for data in self.order:
            if (status == "Processed"):
                if data.name == order.name:
                    data.status = "Processed"
                    self.save_order()
            
            elif status == "Cancel":
                if data.name == order.name:
                    data = {}
                    self.save_order()