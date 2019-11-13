from Examples.example_5_methods import Bike, Condition

bike = Bike(100, 'Univega', 'Alpina', 1999, Condition.OKAY)

bike.update_sale_price()          # sale price = $350

bike.service(30, Condition.GOOD)  # cost = $130

print(bike.sale_price)            # sale price = $560

bike.sell()                       # profit = $430
