from dataclasses import dataclass
from example_5_methods import Condition


@dataclass
class Bike:
    description: str
    condition: Condition
    sale_price: int
    cost: int = 0


if __name__ == '__main__':
    bike_1 = Bike("Red Raleigh cruiser", Condition.GOOD, 650, 50)
    bike_2 = Bike("Red Raleigh cruiser", Condition.GOOD, 650)

    print(bike_1)
    print(bike_2)
    print([bike_1, bike_2])
    print(bike_1 == bike_2)

    bike_2.cost = 50
    print(bike_1 == bike_2)

