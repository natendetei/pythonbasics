# Data structures are used for storing data.
# Lists, tuples, sets, and dictionaries.

# Lists - used to store multiple items in a single variable.
# Lists are ordered, allow duplicates and can be modified(mutable)
subjects = ["math","english","science","kiswahili"]
print(subjects)

# Accessing list item use index[index]
print(subjects[0])
print(subjects[2])
print(type(subjects))

# Change list item
subjects[0] = "Geography"
print(subjects)

# List methods .append(), insert(), remove(), sort()

# append() - adds and item to the end of the list.
subjects.append("History")
print(subjects)

# insert() - adds an item at specific position.
subjects.insert(2,"math")
print(subjects)

# remove() - removes an item 
subjects.remove("kiswahili")

# pop()
subjects.pop(3)
print(subjects)

# len() - counts how many items in a list.
print(len(subjects))

# sort - 
subjects.sort()
print(subjects)

# Another list.
mynum = [6,9,34,1,98]

# Loop through a list.
for subject in subjects:
    print(subject)