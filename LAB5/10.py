import re
list1 = []
def convert_reg_camel_to_snake(txt):
    k  =  re.split("([A-Z][^A-Z]*)", txt)
    res = k[0]
    for i in range(1, len(k)):
        if k[i] != '':
           res += "_" +  k[i][0].lower() + k[i][1::]
    list1 = list(res)
    list1.remove("_")
    print(''.join(list1))
x = input()
convert_reg_camel_to_snake(x)
