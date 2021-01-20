from Examples.example_5_methods import Bike, Condition

my_bike = Bike(description='Univega Alpina, orange',
               condition=Condition.OKAY,
               sale_price=500,
               cost=100)

my_bike.service(cost=30, new_sale_price=600)  # cost=$130, sale_price=$600

print(my_bike.sale_price)                  # 600

print(my_bike.sell())                      # sold=True
