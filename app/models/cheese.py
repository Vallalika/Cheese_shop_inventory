class Cheese():
    
    def __init__ (self, name, origin, type, description, stock, buying_cost, selling_price, inventory_include = True, id = None):
        self.name = name
        self.origin = origin
        self.type = type
        self.description = description
        self.stock = stock
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.inventory_include = inventory_include
        self.id = id