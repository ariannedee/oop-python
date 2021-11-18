from enum import Enum


class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNotAllowed(Exception):
    pass


class Bike(object):
    count = 0
    num_wheels = 2

    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost

        self.sold = False
        Bike.count += 1

    def __del__(self):
        Bike.count -= 1

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


if __name__ == '__main__':
    bike1 = Bike('Univega Alpina, orange', Condition.OKAY, sale_price=500, cost=100)
    bike2 = Bike('Raleigh Talus 2', Condition.BAD, sale_price=20)

    # All print 2
    print(bike2.num_wheels)
    print(bike1.num_wheels)
    print(Bike.num_wheels)

    print(Bike.count)  # 2

    del bike1
    print(Bike.count)  # 1
