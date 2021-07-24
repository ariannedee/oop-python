"""
Bike class for use in a retail shop
"""
from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNotAllowed(Exception):
    pass


class Bike:
    def __init__(self, description, condition, sale_price, cost=0):
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.description = description

        self.sold = False

    def update_sale_price(self, new_sale_price):
        if self.sold:
            raise MethodNotAllowed("You can't update the sale price of a bike that's been sold")
        self.sale_price = new_sale_price

    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, cost, new_sale_price=None, new_condition=None):
        self.cost += cost
        if new_sale_price:
            self.update_sale_price(new_sale_price)
        if new_condition:
            self.condition = new_condition


if __name__ == '__main__':
    my_bike = Bike("Red Releigh cruiser", Condition.GOOD, 450, 50)
    print(my_bike)

    my_bike.update_sale_price(400)

    profit = my_bike.sell()

    print(profit)

    #my_bike.update_sale_price(1000)
    my_bike.hello = 'world'
    print(my_bike.hello)
