import re
def find_reg_upper(txt):
    patterns = '^[A-Z]{1}[a-z]*$'
    if re.search(patterns, txt):
       print("Ok")
    else:
       print("No")
x = input()
find_reg_upper(x)