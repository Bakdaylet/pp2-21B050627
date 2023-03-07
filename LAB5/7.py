import re
list1 = []
def find_reg_snake_to_camel(txt):
    result = re.split("_", txt)
    for i in result:
        list1.append(i.capitalize())
    result2_list1 = "".join(list1)
    print(result2_list1)
x = input()
find_reg_snake_to_camel(x)