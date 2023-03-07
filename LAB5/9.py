import re
def find_reg_insert_spaces(txt):
    result  =  re.split("([A-Z][^A-Z]*)", txt)
    for i in result:
        print(i, end = " ")
x = input()
find_reg_insert_spaces(x)
