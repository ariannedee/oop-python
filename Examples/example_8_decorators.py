from datetime import datetime
from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


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

    @property
    def profit(self):
        if self.sold is False:
            return None
        return self.sale_price - self.cost

    @staticmethod
    def age(year):
        current_year = datetime.now().year
        age = current_year - year
        if age < 1:
            return "New"
        elif age < 5:
            return "Recent"
        elif age < 40:
            return "Old"
        else:
            return "Vintage"

    @classmethod
    def get_default_bike(cls):
        return cls(
            description="A default bike",
            condition=Condition.GOOD,
            sale_price=100
        )


if __name__ == '__main__':

    bike = Bike.get_default_bike()  # Class method

    bike.sell()
    print(bike.profit)    # Call property

    # Call static methods
    print(bike.age(1975))  # Vintage
    print(Bike.age(2019))  # Recent

