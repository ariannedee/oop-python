from Examples.example_5_methods import Bike, Condition

bike = Bike('Univega Alpina, orange', Condition.OKAY, sale_price=500, cost=100)

bike.service(spent=30, sale_price=600)  # cost=$130, sale_price=$600

print(bike.sale_price)                  # 600

print(bike.sell())                             # sold=True
