from classes.Products.productsManager import ProductsManager
from classes.Products.products import Product
from classes.Auth.usersManager import UsersManager
import os
import termcolor

class GestionixApp:

    def __init__(self):
        self.products_manager = ProductsManager()
        self.users_manager = UsersManager()
        self.connected = False
        self.user_connected = None

    def display_menu(self):
        if self.connected:
            title = termcolor.colored(f"\n===== Gestionix App : Connected as {self.user_connected.username} =====", "blue")

            print(title)
            print(termcolor.colored("1.", "red"), "Add Product")
            print(termcolor.colored("2.", "red"), "View Products")
            print(termcolor.colored("3.", "red"), "Delete Product")
            print(termcolor.colored("4.", "red"), "Sort the data base")
            print(termcolor.colored("5.", "red"), "Research a product")
            print(termcolor.colored("6.", "red"), "Exit")

            if self.user_connected.group == "admin":
                print(termcolor.colored("7.", "red"), "View Users")
                print(termcolor.colored("8.", "red"), "Modify user group")
                print(termcolor.colored("9.", "red"), "Delete User")

            return input("Enter your choice :")
        else:
            print(termcolor.colored("\n===== Gestionix App =====", "blue"))
            print(termcolor.colored("1.", "red"), "Login")
            print(termcolor.colored("2.", "red"), "Register")
            print(termcolor.colored("3.", "red"), "Exit")

            return input("Enter your choice :")


    def run(self):
        os.system('clear')
        while True:
            choise = self.display_menu()

            if self.connected:
                if choise == "1":
                    os.system('clear')
                    self.products_manager.add_product()
                elif choise == "2":
                    os.system('clear')
                    self.products_manager.view_products()
                elif choise == "3":
                    os.system('clear')
                    self.products_manager.delete_product()
                elif choise == "4":
                    os.system('clear')
                    self.products_manager.sort_products()
                elif choise == "5":
                    os.system('clear')
                    self.products_manager.search_product()
                elif choise == "6":
                    print("Exiting...")
                    break

                if self.user_connected.group == "admin":
                    if choise == "7":
                        os.system('clear')
                        self.users_manager.view_users()
                    elif choise == "8":
                        os.system('clear')
                        self.users_manager.modify_user_group()
                    elif choise == "9":
                        os.system('clear')
                        self.users_manager.delete_user()
            else:
                if choise == "1":
                    self.user_connected= self.users_manager.login()
                    if (self.user_connected):
                        os.system('clear')
                        self.connected = True
                        self.products_manager.load_products(self.user_connected.products)
                elif choise == "2":
                    os.system('clear')
                    self.users_manager.register()
                elif choise == "3":
                    print("Exiting...")
                    break

if __name__ == "__main__":
    GestionixApp().run()