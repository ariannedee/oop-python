from datetime import datetime
from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OKAY = 0.5
    BAD = 0.2


class Bike(object):
    def __init__(self, cost, make, model, year, condition):
        # Different for every new instance
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition

        # Same for every new instance
        self.sale_price = None
        self.sold = False

    def update_sale_price(self):
        original_value = lookup_value(self.make, self.model)
        current_year = datetime.now().year
        current_value = original_value * (1 - (current_year - self.year) * 0.0)
        current_value = current_value * self.condition.value
        self.sale_price = current_value
        return self.sale_price

    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        print(f'Sale price: {self.sale_price}')
        print(f'Cost: {self.cost}')
        print(f'Profit: {profit}')
        return profit

    def service(self, cost, new_condition):
        self.cost += cost
        self.condition = new_condition
        self.update_sale_price()
        return self.sale_price


def lookup_value(make, model):
    return 1000
