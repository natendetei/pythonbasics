# If...elif...else statement.
# If condition1:
     # Block of code to be executed if condition is true.
# elif condition2
     # Block of code to be executed if condition2 is true.
# else:
     # Block of code to be executed if both conditions are false.

# A program that checks students marks and prints their grade and total marks.
# >90=A
# >80=B
# >70=C
# >60=D

marks = int(input("Enter your marks: "))
if marks >=90:
    print("Your grade is:A")
elif marks >=80:
    print("Your grade is:B")
elif marks >=70:
    print("Your grade is:C")
elif marks >=60:
    print("Your grade is:D")
else:
    print("Needs imporvement")

# Logical operators can be used to combine condtitions.
# AND-returns True if both statements are true
# OR-returns True if one of the statements is true
# NOT-reverses the result, returns FALSE if the result is

age = int(input("Enter your age: "))
has_permission = input("Do you have permission?: ")
if age >= 16 and has_permission == "True":
    print("You can enter")
else:
    print("You cannot enter")

# Another example.
temperature = int(input("What is the weather?: "))
if temperature>30 or temperature<10:
    print("The weather is very extreme")                                                                                            
else:
    print("The weather is normal")
