# open(filename,mode)
# modes - read(r), write(w), append(a), create a new file(x).

# write(w)
file = open('demo.txt','w')
file.write("this is python")
file.close()

# read(r)
# read().to read the contents
x = open('demo.txt','r')
print(x.read())
x.close()

# append(a)
y = open('demo.txt','a')
y.write("\n hello good morning!")
y.close()

# read,readlines(),readline()
z = open('demo.txt','r')
print(z.read())
z.close()