import termcolor

class Product:
    def __init__(self, name, price, stock, owner, date):
        self.name = name
        self.price = price
        self.stock = stock
        self.owner = owner
        self.date = date
    
    def __str__(self):
        name = termcolor.colored(f"{self.name:<20}", "red")
        return f"| {name} | {self.price:<10}€ | {self.stock:<10}| {self.owner:<10} | {self.date:<10}"
