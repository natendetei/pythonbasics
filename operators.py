# Arithmetic operators
x = 30
y = 69
sum = x + y
print("The sum of",x,"and",y,"is:", sum)
print(f"the sum of {x} and {y} is {sum}")

# Subtraction 
print(f"The difference of {x} and {y} is {x-y}")

# Multiplication
print(f"The product of {x} and {y} is {x*y}")

# Division
print(x/y)

# Modulus
print(y%x)

# Exponent
print(x**2)

# Comparison operators.
# >,<,==,>=,<=,!=.

# Equal to.
a = 70
b = 30
print(a==b)

# Greater than >.
print(a>b)

# Less than <.
print(a<b)

# Greater than or equal to >=.
print(f"is {a} greater than or equal to {b}? {a>=b}")

# Less than or equal to <=.
print(f"is {a} less than or equal to {b}? {a<=b}")

# Not equal to !=
print(a!=b)

# Assignment operators
#=, +=, -=, *=, /=, %=, **=, //=

z = 45
print(z)

# +=
z+=3 #z=z+3
print(z)

# -=
z-=1
print(z)

# Logical operators
# AND,OR,NOT

# AND-returns True if both statements are true
c=3
print(c<5 and c>1)
print(c<5 and c>10)

# OR-returns True if one of the statements is true
print(c<5 or c>10)

# NOT-reverses the result, returns FALSE if the result is true
print(not(c>5))