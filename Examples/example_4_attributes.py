class Bike(object):
    def __init__(self, description, condition, sale_price, cost=0):
        # Different initial values for every new instance
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost

        # Same initial value for every new instance
        self.sold = False

    def update_sale_price(self):
        pass

    def sell(self):
        pass

    def service(self):
        pass
