from datetime import datetime
from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OKAY = 0.5
    BAD = 0.2


class Bike(object):

    def __init__(self, cost, make, model, year, condition):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition

        self.sale_price = self.update_sale_price()
        self.sold = False

        print(f'New bike: {self}')

    def __del__(self):
        print(f'Deleting bike: {self}')

    def update_sale_price(self):
        """
        Set the current sale price based on the make, model, age, and condition
        """
        original_value = lookup_msrp_value(self.make, self.model)
        current_year = datetime.now().year
        current_value = original_value * (1 - (current_year - self.year) * 0.015)
        current_value = current_value * self.condition.value
        self.sale_price = current_value
        return self.sale_price

    def sell(self):
        """
        Mark as sold and determine the profit received from selling the bike
        """
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, cost, new_condition):
        """
        Service the bike and update sale price
        """
        self.cost += cost
        self.condition = new_condition
        self.update_sale_price()
        return self.sale_price

    def __repr__(self):
        return f'Bike: {self.year} {self.make} {self.model} ({"sold" if self.sold else self.sale_price})'

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'


def lookup_msrp_value(make, model):
    """
    Determine original sale price of a bike when new
    """
    return 1000


if __name__ == '__main__':
    bike = Bike(100, 'Univega', 'Alpina', 1999, Condition.OKAY)  # __init__ called

    print(bike)     # __str__ called

    print([bike])   # __repr__ called

    del bike        # __del__ called

    Bike(0, 'Raleigh', 'Talus 2', 2013, Condition.BAD)  # __init__ and __del__ called
