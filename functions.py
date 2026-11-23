# Functions are reusable blocks of code
# That does a specific task.
# def functionname():
     # Body of the function.
# Function only runs when you call it or when called.
# Functionname()
def hello():
    print("This is a function")
# Calling the function.
hello()
hello()

def greet():
    print("Hello goodmorning")
# Calling the function.
greet()

# Parameters are used to store the value passed to a function.
def greetings(name):
    print("Hi", name)
# Calling the function.
greetings("Kamau")
greetings("Mary")

def display_details(first_name,age = 20):
    print(f"My name is {first_name} and i am {age} years old.")
# Calling the function.
display_details("Nathan",16)
display_details("Tom",19)
display_details("Eric")

# A function that adds two numbers.
# return keyword returns a value when you call the function.
def addTwoNumbers(a,b):
    return a + b
# Calling the function.
# Print the returned value.
print(addTwoNumbers(70,29))
# Store the returned value in a variable.
result = addTwoNumbers(20,40)
print(result)

# Function that calculates the area of a rectangle a = l * w.
def area(l,w):
    print(f"The area of rectangle with length {l} and width {w} is {l * w}")
# Calling the function.
area(40,20)
area(25,17)

 # Function that calculates area of a circle a = 3.142 * r * r.
def areaOfCircle(r):
    print(f"The area of a circle with raidus {r} is {3.142 * r * r}")
# Calling the function.
areaOfCircle(7)

# A function welcome that displays student name and course.
def welcome(student_name,course):
    print(f"Welcome {student_name}, your course is {course}")
# Calling the function.
welcome("John","Python")