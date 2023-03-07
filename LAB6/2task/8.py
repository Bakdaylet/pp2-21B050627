import os
f = open('Z.txt')
line = f.readline()
while line:
    print (line),
    line = f.readline()
f.close()
path = "C:\\Users\\Admin\\Desktop\\LAB6\\2task\\Z.txt"
os.remove(path)