# with ..as
with open('opera.txt','w') as file:
    file.write("its a new day")
    file.write("\n learning python")

# read
with open('opera.txt','r') as x:
    print(x.read())