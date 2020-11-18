"""
Bike class for use in a retail shop
"""
from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 2
    OKAY = 3
    BAD = 4


class MethodNotAllowed(Exception):
    pass


class Bike(object):
    def __init__(self, description, condition, sale_price, cost=0):
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.description = description

        self.sold = False

    def update_sale_price(self, new_sale_price):
        if self.sold:
            raise MethodNotAllowed("You cannot update the price of a sold bike")
        self.sale_price = new_sale_price

    def sell(self):
        self.sold = True
        return self.sale_price - self.cost

    def service(self, cost, new_sale_price):
        self.cost += cost
        self.update_sale_price(new_sale_price)

    def __str__(self):
        return f"{self.description}{' (sold)' if self.sold else ''}"

    def __repr__(self):
        return f"Bike: {self} {self.condition.name}"


if __name__ == '__main__':
    my_bike = Bike("2004 Raleigh Cruiser", Condition.GOOD, sale_price=350, cost=50)

    # Update sale price
    my_bike.update_sale_price(300)

    # Sell bike
    profit = my_bike.sell()

    # Determine profit
    print(profit)

