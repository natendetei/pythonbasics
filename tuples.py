# Tuples - used to store multiple items in a single variable.
# Ordered and cannot be changed(immutable)

hobbies = ("swimming","hiking","reading","eating",)
print(hobbies)
print(type(hobbies))

# Accesing item using index.
print(hobbies[0])

# len()
print(len(hobbies))

# loop
for hobby in hobbies:
    print(hobby)