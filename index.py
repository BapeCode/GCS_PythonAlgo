from classes.Products.productsManager import ProductsManager
from classes.Products.products import Product
from classes.Auth.usersManager import UsersManager
import os
import time

class GestionixApp:

    def __init__(self):
        self.products_manager = ProductsManager()
        self.users_manager = UsersManager()
        self.connected = False
        self.user_connected = None

    def display_menu(self):
        if self.connected:
            print("\n===== Gestionix App =====")
            print("1. Add Product")
            print("2. View Products")
            print("3. Delete Product")
            print("4. Sort the data base")
            print("5. Research a product")
            print("6. Exit")

            return input("Enter your choice :")
        else:
            print("\n===== Gestionix App =====")
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            return input("Enter your choice :")


    def run(self):
        os.system('clear')
        while True:
            choise = self.display_menu()

            if self.connected:
                if choise == "1":
                    self.products_manager.add_product()
                elif choise == "2":
                    self.products_manager.view_products()
                elif choise == "3":
                    self.products_manager.delete_product()
                elif choise == "4":
                    self.products_manager.sort_products()
                elif choise == "5":
                    self.products_manager.search_product()
                elif choise == "6":
                    print("Exiting...")
                    break
            else:
                if choise == "1":
                    self.connected, self.user_connected = self.users_manager.login()
                    print(self.user_connected)
                elif choise == "2":
                    self.users_manager.register()
                elif choise == "3":
                    print("Exiting...")
                    break

if __name__ == "__main__":
    GestionixApp().run()