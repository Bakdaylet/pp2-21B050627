file = open("input.txt","r")
counter = 0  
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        counter += 1
print("The number of lines in the file is")
print(counter)