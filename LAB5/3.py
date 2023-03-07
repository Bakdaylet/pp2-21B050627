import re
def find_reg_b(txt):
    patterns = '(^[a-z]{1}(_){1})*$'
    if re.search(patterns, txt):
       print("Ok")
    else:
       print("No")
x = input()
find_reg_b(x)