
class Bill:
    def __init__(self, name, amount, dua_date):
        self.name = name
        self.amount = amount
        self.dua_date = dua_date

    
    def __str__(self):
        return f"{self.name:<20} {self.amount:<10} {self.dua_date}"

class BillManager:
    BILL_FILE = 'bills.json'

    def __init__(self):
        self.bills = self.load_bills()

    
    def load_bills(self):

        try:
            with open(self.BILL_FILE, 'r')  as file:
                bills = file

                return [Bill(bill['name'], bill['amount'], bill['due_date']) for bill in bills]
        except FileNotFoundError:
            return []
        
    
    def save_bills(self):
        bill_data = [{
            'name': bill.name,
            'amount': bill.amount,
            'due_date': bill.dua_date
        } for bill in self.bills]

        with open(self.BILL_FILE, "w") as file:
            file.write(str(bill_data))
        
    def add_bill(self, bill):
        self.bills.append(bill)
        self.save_bills()


    def view_bills(self):
        if not self.bills:
            print("No bills found.")

        else:
            print(f"{"Name":<20} {"Amount":<10} {"Due Date":<10}")
            print("-" * 40)
            for bill in self.bills:
                print(bill)
    
    def delete_bill(self, name):
        self.bills = [bill for bill in self.bills if bill.name != name]

        self.save_bills()


class BillManagerApp:

    def __init__(self):
        self.bill_manager = BillManager()

    def display_menu(self):
        print("\n=== Bill Manager ===")
        print("1. Add Bill")
        print("2. View Bills")
        print("3. Delete Bill")
        print("4. Exit")

        choise = input("Enter your choice :")

        return choise
    
    def add_bill(self):
        name = input("Enter bill name: ")
        amount = input("Enter bill amount: ")
        due_date = input("Enter bill due date: ")

        bill = Bill(name, amount, due_date)
        self.bill_manager.add_bill(bill)

        print(f"Bill '{name}' added successfully.")

    def delete_bill(self):
        name = input("Enter bill name: ")
        self.bill_manager.delete_bill(name)

        print(f"Bill '{name}' deleted successfully.")

    def run(self):
        while True:

            choise = self.display_menu()

            if choise == '1':
                self.add_bill()
            elif choise == '2':
                self.bill_manager.view_bills()
            elif choise == '3':
                self.delete_bill()
            elif choise == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")
