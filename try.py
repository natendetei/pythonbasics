# Try..except is used for exception handling.
# try:
     # Block of code than can cause an error
"""
try:
     block of code that can cause an error
except:
     code that runs in case of an error
"""
try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("You cannot divide an number by zero.")

# Name error.
try:
    print(x)
except NameError:
    print("The variable is not defined")

# try..except...else..finally
# else - runs if no exception occurs.
# finally - always runs exception or not.

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Enter a valid number")
else:
    print(f"Your are {age} years old")
finally:
    print("This always executes")