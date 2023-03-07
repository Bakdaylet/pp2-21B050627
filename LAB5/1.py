import re
def find_reg_ex(txt):
    patterns = '^a(b*)$'
    if re.search(patterns, txt):
       print("Ok")
    else:
       print("No")
x = input()
find_reg_ex(x)
