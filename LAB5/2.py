import re
def find_reg_a(txt):
    patterns = '^a(b){1 || 2  || 3}$'
    if re.search(patterns, txt):
       print("Ok")
    else:
       print("No")
x = input()
find_reg_a(x)