# Strings are a sequence of characters.
# You can create a string using single quotes or double quotes.
course = 'python'
print(course)

text = "python programming"
print(text)

# String methods.

# upper(), capitalises the whole string.
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("python", "kotlin"))
print(text.capitalize())
print(len(text))

# String concatenation +
first_name = "Brian"
last_name = "otieno"
print(first_name + " " + last_name)

age = 18
print(f"My name is {first_name} and I am {age} years old." ) # f string
print(f"My name is {first_name} {last_name}")

# String slicing.
school = "emobilis"
# [Start index:stop index]
print(school)
print(school[0:4])
print(school[2:6])
print(school[1:])
print(school[:5])
print(school[0:6:])

my_text = "programming"
# Slice until prog
# gramming
# gram
# ogram
print(my_text[:4])
print(my_text[3:])
print(my_text[3:7])
print(my_text[2:7])

# Escape characters.
# \n - inserts a new line.
print('Hello, goodmorning \nthis goes in a new line')

# \t - adds a tab space.
print('name: \tcourse')
print("She says,\"Hi\"") # \" to print a quote
print('She says, "Hi"')
print('It\'s a good day')
print("He said \"I love programming\"")
print('"Education is the key to success" -Barak Obama')