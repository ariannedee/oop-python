def update_sale_price(bike : dict, sale_price: float):
    if bike['sold'] is True:
        raise Exception("Action not allowed. Bike has already been sold")
    bike['sale_price'] = sale_price


def create_bike(description, cost, sale_price, condition):
    return {
        'description': description,
        'cost': cost,
        'sale_price': sale_price,
        'condition': condition,
        'sold': False,
    }


def sell(bike, sold_for=None):
    if sold_for:
        update_sale_price(bike, sold_for)
    bike['sold'] = True
    profit = bike['sale_price'] - bike['cost']
    return profit


bike1 = create_bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
# bike1 = {
#         'cost': 100,
#         'condition': 0.5,
#         'description': 'Univega Alpina, orange',
#         'sale_price': 500,
#         'sold': False,
#     }

update_sale_price(bike1, 350)
# bike1['sale_price'] = 350.00

print(sell(bike1))
# bike1['sold'] = True