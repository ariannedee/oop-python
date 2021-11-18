from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNotAllowed(Exception):
    pass


class Bike(object):
    min_profit = 10

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
    def get_default_bike(cls):
        return cls(
            description="A default bike",
            condition=Condition.GOOD,
            sale_price=100
        )


if __name__ == '__main__':
    bike = Bike.get_default_bike()  # Class method

    print(bike.sale_price)  # 100

    bike.sale_price = 300
    print(bike.sale_price)  # 300

    bike.sell()
    bike.sale_price = 200   # Exception raised

