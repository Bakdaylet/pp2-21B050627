import re
def find_reg_split_upper(txt):
    result  =  re.split(r"[A-Z]", txt)
    for  i in result:
        print(i, end = " ")
x = input()
find_reg_split_upper(x)