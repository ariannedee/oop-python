from enum import Enum

class MethodNotAllowed(Exception):
    pass

class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3

class Bike(object):
    num_wheels = 2
    counter = 0

    def __init__(self, user_description, user_condition, user_sale_price, user_cost=0): ## create __init__ method. We can start setting properities on bike object. Self is instance of that object
        self.description = user_description
        self.condition =  user_condition
        self.sale_price = user_sale_price
        self.cost = user_cost

        self.sold = False ## All the attributes must be defined in __init__ otherwise it will give warning
        #print("Create new bike")
        Bike.counter += 1
        print(f"{self} created")

    def __del__(self): ## Run the program and see that even if you don't call del in the __main__ the Bike object automatically gets deleted. Its because in Python, when an object runs out of its usefulness its automatically deleted.
        self.counter -= 1
        print(f"{self} deleted") ## Alternatively you can also write [del my_bike] in main it will be deleted

    def update_sale_price(self, new_sale_price):
        if self.sold:
            raise MethodNotAllowed("Can't update sale price if the bike has been sold")
        self.sale_price = new_sale_price

    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, new_sale_price= None, new_condition= None):
        if new_condition:
            self.condition = new_condition
        if new_sale_price:
            self.update_sale_price(new_sale_price)

    @property ## this is a property function
    def profit(self, x):
        if self.sold:
            return self.sale_price - self.cost
        else:
            return None

    @staticmethod
    def some_method(self, x, y):
        return x + y


    def __add__(self, other):
        if isinstance(other, Bike):
             return "Two bikes"
        return other

    def __len__(self):
        return 12

    def __str__(self): ## Add this to see the description of my_bike object
        return f"{self.description} - {self.condition.name} condition"

    def __repr__(self):
        sold = " (sold)" if self.sold else "" ## This says if self.sold then set it to (sold) else ""
        return f"Bike: {self.description}, {self.condition.name}, {self.sale_price}, {self.cost}"


if __name__ == "__main__":
    my_bike = Bike(user_description="Orange Univega", user_condition=Condition.GOOD, user_sale_price=200, user_cost=50)
    my_bike.service(new_sale_price=30000)
    my_bike.sell()
    #print("Normal Profit is",my_bike.profit())
    print("Decorator Profit is",my_bike.profit) ## because of decorator now you can call the function as method.. so you dont need to write profit() instead just .profit
    print(my_bike.sold)

    my_bike.some_method(1,2)
    Bike.some_method(3,4)



