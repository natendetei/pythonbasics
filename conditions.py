# If statement
# If condition: 
     # Block of code to be executed if the condition is true
x = 10
if x > 5:
    print(x, "is greater than 5")

print("code outside the if statement")

# If...else statement.
# If condition:
     # Block of code to be executed if condition is true
# else:
     # Block of code to be executed if the condition is false.
age = 16
if age >= 18:
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")

# A program that asks the user to enter their age.
# The program checks whether they are eligible to vote.
user_age = int(input("Enter your age: "))
print("You are", user_age, "years old")
if user_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


    