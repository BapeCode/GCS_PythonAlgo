from classes.Products.productsManager import ProductsManager
from classes.Products.products import Product
import os
import time

class GestionixApp:

    def __init__(self):
        self.products_manager = ProductsManager()

    def display_menu(self):
        print("\n===== Gestionix App =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Delete Product")
        print("4. Sort the data base")
        print("5. Did a search")
        print("6. Exit")

        choise = input("Enter your choice :")

        return choise
    
    def add_product(self):
        current_time = time.localtime()
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        stock = input("Enter product stock: ")
        date = f"{current_time.tm_mday}-{current_time.tm_mon}-{current_time.tm_year}-{current_time.tm_hour}-{current_time.tm_min}-{current_time.tm_sec}"

        product = Product(name, price, stock, date)
        self.products_manager.add_product(product)

        print(f"Product '{name}' added successfully.")

    def delete_product(self):
        name = input("Enter product name: ")
        self.products_manager.delete_product(name)

        print(f"Product '{name}' deleted successfully.")

    def run(self):
        os.system('clear')
        while True:
            choise = self.display_menu()

            if choise == "1":
                self.add_product()
            elif choise == "2":
                self.products_manager.view_products()
            elif choise == "3":
                self.delete_product()
            elif choise == "4":
                self.products_manager.sort_products()
            elif choise == "5":
                self.products_manager.search_product()
            elif choise == "6":
                print("Exiting...")
                break

if __name__ == "__main__":
    GestionixApp().run()