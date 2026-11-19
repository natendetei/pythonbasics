# Stores data in key:value pairs.
student = {
    "name":"kamau",
    "age":16,
    "course":"python"

}
print(student)
print(type(student))

# Accessing values .dictionary[key]
print(student["name"])
print(student["course"])

# Add key:value pair.
student["city"] = "nairobi"
print(student)

# Change value.
student["name"] = "Lucy"
print(student)