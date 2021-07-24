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

    ## Dunder method -> we can use some of these python features
    ## You can't really create your dunder methods. You just use the one that already exists..
    ## Why we need it? Because say you want to compare my_bike == other_bike -> you cant write this. So good way is to create a dunder method for comparison
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

# class Tricycle(Bike):
#     num_wheels = 3


## This is basically saying that when you run this file directly then do this stuff
## But if you are going to import it into another file then don't do this stuff
if __name__ == "__main__":
    #print(Bike.num_wheels)
    print(Bike.counter)

    my_bike = Bike(user_description="Orange Univega", user_condition=Condition.GOOD, user_sale_price=200, user_cost=50)  ## we could also write Bike.__init__() but its ugly.
    # print(my_bike)
    #print(my_bike.num_wheels)
    print(my_bike.counter)

    my_bike2 = Bike(user_description="Orange Univega", user_condition=Condition.GOOD, user_sale_price=200, user_cost=50)
    print(my_bike2.counter)

    # my_trike = Tricycle("", Condition.BAD, 40)
    # print(my_trike.num_wheels)
    # # print(my_bike.service(new_sale_price=300))
    # profit = my_bike.sell() ## self above is going to be referencing my_bike
    # #my_bike.update_sale_price(500)
    #
    # print(profit)
    # print(my_bike.sold)
    # print(repr(my_bike))


    #print(my_bike + 3)
    #print(len(my_bike)) ## Also you cant really write len(my_bike) without implementing above dunder method. if you want this to work, then define it above __len__. You can comment it to see that it does not work
    #my_bike.update_sale_price()
    #my_bike.service()
    ###

    ## How to commit?


