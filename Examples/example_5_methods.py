from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OKAY = 0.5
    BAD = 0.2


class MethodNotAllowed(Exception):
    pass


class Bike(object):
    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost

        self.sold = False

    def update_sale_price(self, sale_price):
        if self.sold:
            raise MethodNotAllowed('Bike has already been sold')
        self.sale_price = sale_price

    def sell(self):
        """
        Mark as sold and determine the profit received from selling the bike
        """
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, spent, sale_price=None, condition=None):
        """
        Service the bike and update attributes
        """
        self.cost += spent
        if sale_price:
            self.update_sale_price(sale_price)
        if self.condition:
            self.condition = condition
