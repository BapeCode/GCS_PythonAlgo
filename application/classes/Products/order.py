import termcolor

class Order:
    def __init__(self, customer, name, price, stock, date, status, commercial):
        self.name = name 
        self.price = price
        self.stock = stock
        self.date = date
        self.customer = customer
        self.status = status
        self.commercial = commercial
