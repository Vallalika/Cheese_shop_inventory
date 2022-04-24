from curses import start_color


class Cheese():
    
    def __init__ (self, name, origin, type, description, stock, buying_cost, selling_cost, providers = None, id = None):
        self.name = name
        self.origin = origin
        self.type = type
        self.description = description
        self.stock = stock
        self.buying_cost = buying_cost
        self.selling_price = selling_cost
        self.providers = providers
        self.id = id