from math import*
def find_area_of_trapezoid(h, base1, base2):
    print("Height:",h)
    print("Base, first value:",base1)
    print("Base, second value:",base2)
    S = ((base1+base2)*h)/2
    print('Expected Output:', S)
x, y, z = map(int, input().split())
find_area_of_trapezoid(x, y, z)