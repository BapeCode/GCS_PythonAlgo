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
        print("Sort by:")
        print("1. Name")
        print("2. Price")
        print("3. Stock")
        print("4. Date")

        choice = input("Enter your choice (1-4): ")
        sort_type = None

        if choice == "1":
            sort_type = "Name"
        elif choice == "2":
            sort_type = "Price"
        elif choice == "3":
            sort_type = "Stock"
        elif choice == "4":
            search_csort_typeolumn = "Date"
        else:
            print("Invalid choice.")
            return
        
        valid_columns = {"Name": "Name", "Price": "Price", "Stock": "Stock", "Date": "Date"}
        
        if sort_type not in valid_columns:
            print("Invalid sort type")
            return
        
        try: 
            
            df = pd.DataFrame([{
            "Name": product.name,
            "Price": product.price,
            "Stock": product.stock,
            "Owner": product.owner,
            "Date": product.date
                } for product in self.products])

            if df.empty:
                print("No products to sort.")
                return
            
            # Handle sorting logic
            if sort_type in valid_columns:
                # Ask for ascending or descending order
                order = input("Ascending or descending order ? (asc/desc) : ").lower()
                if order == "asc":
                    ascending = True
                elif order == "desc": 
                    ascending = False
                else: 
                    print("Invalid order. Defaulting to ascending.")
                    ascending = True

                # Sort the DataFrame
                sorted_products = df.sort_values(by=valid_columns[sort_type], ascending=ascending)

                # Print the sorted DataFrame
                print(termcolor.colored(f"{'Name':<20} {'Price':<15} {'Stock':<15} {'Owner':<15} {'Date':<15}", "blue"))
                print(termcolor.colored("-" * 70, "light_blue"))
                for _, row in sorted_products.iterrows():
                    print(f"{row['Name']:<20} {row['Price']:<15} {row['Stock']:<15} {row['Owner']:<15} {row['Date']:<15}")

        except Exception as e:
            print(f"An error occurred while sorting products: {e}")


    
    def search_product(self):
        print("Search by:")
        print("1. Name")
        print("2. Price")
        print("3. Stock")
        print("4. Date")
        
        choice = input("Enter your choice (1-4): ")
        search_column = None

        if choice == "1":
            search_column = "Name"
        elif choice == "2":
            search_column = "Price"
        elif choice == "3":
            search_column = "Stock"
        elif choice == "4":
            search_column = "Date"
        else:
            print("Invalid choice.")
            return
        
        search_query = input(f"Enter the value to search in {search_column}: ").strip()
        
        try:
            
            df = pd.DataFrame([{
                "Name": product.name,
                "Price": product.price,
                "Stock": product.stock,
                "Owner": product.owner,
                "Date": product.date
            } for product in self.products])

            if df.empty:
                print("No products available to search.")
                return
            
            
            if search_column in ["Name", "Date"]:
                
                matches = df[df[search_column].str.contains(search_query, case=False, na=False)]
            elif search_column in ["Price", "Stock"]:
                
                try:
                    search_value = float(search_query)
                    matches = df[df[search_column] == search_value]
                except ValueError:
                    print(f"Invalid input for {search_column}. Please enter a number.")
                    return
            else:
                print("Invalid search column.")
                return
            
            
            if matches.empty:
                print("No matching products found.")
            else:
                print(termcolor.colored(f"{'Name':<20} {'Price':<15} {'Stock':<15} {'Owner':<15} {'Date':<15}", "blue"))
                print(termcolor.colored("-" * 70, "light_blue"))
                for _, row in matches.iterrows():
                    print(f"{row['Name']:<20} {row['Price']:<15} {row['Stock']:<15} {row['Owner']:<15} {row['Date']:<15}")

        except Exception as e:
            print(f"An error occurred while searching for the product: {e}")
