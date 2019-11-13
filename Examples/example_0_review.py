# Getting user input
temp = int(input("What's the temperature? "))

# Conditionals
if temp <= 0:
    print("It’s freezing")
elif temp >= 100:
    print("It’s boiling")
else:
    print("It's alright")

# Lists
populous_countries = ["China", "India", "USA", "Indonesia", "Brazil"]

populous_countries[2] = "United States"
populous_countries.append("Pakistan")

# For loop
for i in range(10):
    print(i * i)

# Import from module/library
from time import sleep

# While loop
seconds_left = 3

while seconds_left > 0:
    print(seconds_left)
    sleep(1)
    seconds_left -= 1

print("Lift off!")


# Functions
def square(num):
    return num * num


# Assertions
assert square(10) == 100

# Dictionaries
fruit = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}

print(fruit['a'])  # Retrieve an value
fruit['c'] = 'cherry'  # Modify a value
fruit['d'] = 'dragon fruit'  # Add a new key/value

# Exceptions
user_input = input('Give me a number')

try:
    number = float(user_input)
except ValueError:
    print(f'{user_input} is not a valid number')

