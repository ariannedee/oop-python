from datetime import datetime


def lookup_msrp_value(make, model):
    """
    Determine original sale price of a bike when new
    """
    return 1000


def set_sale_price(bike):
    original_value = lookup_msrp_value(bike['make'], bike['model'])
    current_year = datetime.now().year
    current_value = original_value * (1 - (current_year - bike['year']) * 0.015)
    current_value = current_value * bike['condition']
    bike['sale_price'] = current_value


def create_bike(cost, make, model, year, condition):
    return {
        'cost': cost,
        'make': make,
        'model': model,
        'year': year,
        'condition': condition,
        'sold': False,
    }


def sell(bike):
    bike['sold'] = True
    profit = bike['sale_price'] - bike['cost']
    return profit


bike1 = create_bike(100, 'Univega', 'Alpina', 1999, 0.5)
# bike1 = {
#         'cost': 100,
#         'make': 'Univega',
#         'model': 'Alpina',
#         'year': 1999,
#         'condition': 0.5,
#         'sold': False,
#     }

set_sale_price(bike1)
# bike1['sale_price'] = 350.00

sell(bike1)
# bike1['sold'] = True
