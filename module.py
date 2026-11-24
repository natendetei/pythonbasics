# A module is a python file that contains reusable code.
# Built-in modules math, random.

# Math module.
import math 
import random
import os
import datetime

print(math.sqrt(25))
print(math.ceil(4.56))
print(math.floor(4.46))
print(math.pi)
print(math.pow(2,3))

# Random module.
# Random float betwen 0 and 1
print(random.random())
print(random.randint(1,7))

# OS can use module to interact with the operating system.
# Get current working directory.
print(os.getcwd())
# os.mkdir("hello")

# Print current date.
print(datetime.date.today())
# Current date and time.
print(datetime.datetime.now())