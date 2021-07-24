class Bike(object):
    def __init__(self, user_description, user_condition, user_sale_price, user_cost=0): ## create __init__ method. We can start setting properities on bike object. Self is instance of that object
        self.description = user_description
        self.condition = user_condition
        self.sale_price = user_sale_price
        self.cost = user_cost

        self.sold = False

        print("Create new bike")

    def update_sale_price(self):
        pass

    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self):
        pass

## This is basically saying that when you run this file directly then do this stuff
## But if you are going to import it into another file then don't do this stuff
if __name__ == "__main__":
    my_bike = Bike(user_description="Orange Univega", user_condition="Okay", user_sale_price=200, user_cost=50)  ## we could also write Bike.__init__() but its ugly.
    print(my_bike)

    print(my_bike.sold)
    profit = my_bike.sell() ## self above is going to be referencing my_bike
    print(profit)
    print(my_bike.sold)

    my_bike.update_sale_price()
    my_bike.service()

    ## Ok


