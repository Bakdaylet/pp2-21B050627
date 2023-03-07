with open('input.txt',"r") as file:
     with open('B.txt',"w") as file1:
          for i in file:
              file1.write("%s" % i)
content = open("B.txt")
print(content.read())