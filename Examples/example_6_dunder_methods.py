from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OKAY = 0.5
    BAD = 0.2


class Bike(object):
    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost

        self.sold = False
        print(f'New bike: {self}')

    def __del__(self):
        print(f'Deleting bike: {self}')

    def update_sale_price(self, sale_price):
        if self.sold:
            return Exception('Action not allowed. Bike has already been sold')
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

    def __repr__(self):
        sold_or_price = "sold" if self.sold else f"${self.sale_price}"
        return f'Bike: {self.description} ({sold_or_price})'

    def __str__(self):
        return self.description


if __name__ == '__main__':
    bike = Bike('Univega Alpina, orange', Condition.OKAY, sale_price=500, cost=100)

    print(bike)        # __str__ called
    print(str(bike))   # __str__ called

    print([bike])      # __repr__ called
    print(repr(bike))  # __repr__ called

    del bike           # __del__ called

    bike = Bike('Raleigh Talus 2', Condition.BAD, sale_price=20)  # __init__ and __del__ called
