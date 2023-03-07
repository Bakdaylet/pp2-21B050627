import re
def find_reg_any_symbol_after_a(txt):
    patterns = '^[a]{1}(.)*b$'
    if re.search(patterns, txt):
       print("Ok")
    else:
       print("No")
x = input()
find_reg_any_symbol_after_a(x)