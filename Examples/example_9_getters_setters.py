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
    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self._sale_price = sale_price
        self.cost = cost

        self.sold = False

    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price):
        if self.sold:
            raise MethodNotAllowed('Bike has already been sold')
        if sale_price < 0:
            raise ValueError("Sale price must be non-negative")
        else:
            self._sale_price = sale_price

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
            self.sale_price = sale_price
        if self.condition:
            self.condition = condition

    @classmethod
    def get_test_object(cls):
        return cls(
            description=f"A test {cls.__name__}",
            condition=random.choice(list(Condition)),
            sale_price=random.randrange(100, 500, 25),
            cost=random.randrange(0, 100, 10)
        )


if __name__ == '__main__':
    bike = Bike.get_test_object()  # Class method

    print(bike.sale_price)

    bike.sale_price = 1000  # Calls setter
    print(bike.sale_price)  # 1000

    bike.sell()
    bike.sale_price = 999  # Exception raised

