from utils.fileManager import FileManager
from .products import Product
import time

class ProductsManager: 
    PRODUCT_FILE = "./data/products.csv"

    def __init__(self):
        self.products = self.load_products()

    def load_products(self):
        try:
            file = FileManager().load_file(self.PRODUCT_FILE)
            products = [line.strip().split(",") for line in file[1:]]
            Object = [Product(product[0], product[1], product[2], product[3]) for product in products]
            return Object
        except FileNotFoundError:
            return []
        
    def save_products(self):
        data = [
            ['Name', "Price", "Stock", "Date"],
            *[[product.name, product.price, product.stock, product.date] for product in self.products]
        ]

        FileManager().save_file(self.PRODUCT_FILE, data)

    def add_product(self):
        current_time = time.localtime()
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        stock = input("Enter product stock: ")
        date = f"{current_time.tm_mday}-{current_time.tm_mon}-{current_time.tm_year}-{current_time.tm_hour}-{current_time.tm_min}-{current_time.tm_sec}"

        product = Product(name, price, stock, date)

        self.products.append(product)
        self.save_products()
        print(f"Product '{name}' added successfully.")
    
    def view_products(self):
        if not self.products:
            print("No products found.")
        else:
            print(f"{"Name":<20} {"Price":<10} {"Stock":<10} {"Date":<10}")
            print("-" * 50)
            for product in self.products:
                print(product)

    def delete_product(self, name):
        name = input("Enter product name: ")
        self.products = [product for product in self.products if product.name != name]
        self.save_products()
        print(f"Product '{name}' deleted successfully.")

    def sort_products(self):
        sort_type = input("Trier par : (Name, Price, Stock, Date) : ")

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
        print("Products sorted successfully.")
    
    def search_product(self):
        target = input("Enter the name of the product you want to search: ")
        low = 0
        hight = len(self.products) - 1

        while low <= hight:
            mid = (low + hight) // 2
            mid_product = self.products[mid]
            

            if mid_product.name == target:
                print(f"{"Name":<20} {"Price":<10} {"Stock":<10} {"Date":<10}")
                print("-" * 50)
                return print(f"{mid_product}")
            elif mid_product.name.lower().startswith(target.lower()):
                print(f"{"Name":<20} {"Price":<10} {"Stock":<10} {"Date":<10}")
                print("-" * 50)
                results = [product for product in self.products if product.name.lower().startswith(target.lower())]
                for result in results:
                    print(f"{result}")

                return
            elif target < mid_product.name:
                hight = mid - 1
            else: 
                low = mid + 1

        return None