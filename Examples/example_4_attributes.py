class Bike(object):
    def __init__(self, cost, make, model, year, condition):
        # Different initial values for every new instance
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition

        # Same initial values for every new instance
        self.sale_price = None
        self.sold = False

    def update_sale_price(self):
        pass

    def sell(self):
        pass

    def service(self, cost, new_condition):
        pass
