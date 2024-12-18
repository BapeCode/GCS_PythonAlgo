from utils.fileManager import FileManager
from .products import Product
import time
import termcolor
import hashlib
import pandas as pd

class ProductsManager: 
    def __init__(self):
        self.products = []
        self.PRODUCT_FILE = None

    def load_products(self, username):
        self.PRODUCT_FILE = "./data/products.csv"
        try:
            
            df = pd.read_csv(self.PRODUCT_FILE)
        
            filtered_df = df[df['Owner'] == username]

            self.products = [
            Product(row['Name'], row['Price'], row['Stock'], row['Owner'], row['Date']) 
            for _, row in filtered_df.iterrows()
            ]
            return self.products

        except FileNotFoundError:

            return []
        
    def save_products(self):
        try:
            
            try:
                file = FileManager().load_file(self.PRODUCT_FILE)
                existing_products = [line.strip().split(",") for line in file[1:]]  
            except FileNotFoundError:
                existing_products = []

            new_products = [
                [product.name, product.price, product.stock, product.owner, product.date] for product in self.products
            ]
            combined_products = [
                product for product in existing_products if product[3] != self.products[0].owner  
            ]

            combined_products.extend(new_products)  
           
            final_data = [["Name", "Price", "Stock", "Owner", "Date"]]
            final_data.extend(combined_products)

            FileManager().save_file(self.PRODUCT_FILE, final_data)
            print("Products saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving products: {e}")

    def add_product(self, users):
        current_time = time.localtime()
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        stock = input("Enter product stock: ")
        owner = users.username
        date = f"{current_time.tm_mday}-{current_time.tm_mon}-{current_time.tm_year}-{current_time.tm_hour}-{current_time.tm_min}-{current_time.tm_sec}"

        product = Product(name, price, stock, owner, date)

        self.products.append(product)
        self.save_products()
        print(f"Product '{name}' added successfully.")
    
    def view_products(self):
        if not self.products:
            print("No products found.")
        else:
            text = termcolor.colored(f"{'Name':<20} {'Price':<15} {'Stock':<15} {'Owner':<15} {'Date':<15}", "blue")
            line = termcolor.colored("-" * 70, "light_blue")
            print(text)
            print(line)
            for product in self.products:
                print(product)

    def delete_product(self):
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