import random
from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNotAllowed(Exception):
    pass


class Bike(object):
    counter = 0

    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost

        self.sold = False
        type(self).counter += 1
        self.id = self.counter

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
    def get_test_bike():
        return Bike(
            description="A test bike",
            condition=random.choice(list(Condition)),
            sale_price=random.randrange(100, 500, 25),
            cost=random.randrange(0, 100, 10)
        )

    @classmethod
    def get_test_object(cls):
        return cls(
            description=f"{cls.__name__} {cls.counter + 1}",
            condition=random.choice(list(Condition)),
            sale_price=random.randrange(100, 500, 25),
            cost=random.randrange(0, 100, 10)
        )

    def __str__(self):
        return f"{self.description}: selling for ${self.sale_price}, cost: ${self.cost} ({self.condition.name.lower()})"

    def __repr__(self):
        return f"{type(self).__name__}({self.description!r}, {self.condition}, {self.sale_price}, {self.cost})"


class Trike(Bike):
    counter = 0


if __name__ == '__main__':

    bike = Bike.get_test_bike()  # Class method
    print(bike)
    bike.sell()
    print(bike.profit)  # Call property

    # Call methods on subclass
    print(Trike.get_test_bike())     # staticmethod
    trike = Trike.get_test_object()  # classmethod
    print(trike)

    print([bike, trike])  # Call repr