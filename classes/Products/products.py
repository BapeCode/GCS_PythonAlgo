class Product:
    def __init__(self, name, price, stock, date):
        self.name = name
        self.price = price
        self.stock = stock
        self.date = date
    
    def __str__(self):
        return f"{self.name:<20} {self.price:<10} {self.stock:<10} {self.date:<10}"
