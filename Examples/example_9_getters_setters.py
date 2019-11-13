from datetime import datetime
from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OKAY = 0.5
    BAD = 0.2


class Bike(object):
    min_profit = 10

    def __init__(self, cost, make, model, year, condition):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition

        self._sale_price = None
        self.sold = False

    @property
    def sale_price(self):
        if self._sale_price is None:
            self.update_sale_price()
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        if value < 0:
            default_sale_price = self.cost + self.min_profit
            print(f'Cannot set sale price to ${value}. Setting to default: ${default_sale_price}')
            self._sale_price = default_sale_price
        else:
            self._sale_price = value

    def update_sale_price(self):
        """
        Set the current sale price based on the make, model, age, and condition
        """
        original_value = self.lookup_msrp_value(self.make, self.model)
        current_year = datetime.now().year
        current_value = original_value * (1 - (current_year - self.year) * 0.015)
        current_value = current_value * self.condition.value

        self.sale_price = current_value   # Calls sale_price.setter
        return self.sale_price

    def sell(self):
        """
        Mark as sold and determine the profit received from selling the bike
        """
        self.sold = True
        return self.profit

    def service(self, cost, new_condition):
        """
        Service the bike and update sale price
        """
        self.cost += cost
        self.condition = new_condition
        self.update_sale_price()
        return self.sale_price

    @property
    def profit(self):
        if not self.sold:
            return None
        return self.sale_price - self.cost

    @staticmethod
    def lookup_msrp_value(make, model):
        """
        Determine original sale price of a bike when new
        """
        return 1000

    @classmethod
    def get_default_bike(cls):
        return cls(
            cost=0,
            make='A make',
            model='A model',
            year=2010,
            condition=Condition.GOOD
        )


if __name__ == '__main__':
    bike = Bike.get_default_bike()  # Class method

    bike.sell()
    print(bike.profit)  # Call property

    # Call static methods
    bike.lookup_msrp_value('Raleigh', 'Talus 2')
    Bike.lookup_msrp_value('Brodie', 'Energy')

