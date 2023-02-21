from math import*
def get_radian():
    k = int(input())
    print('Input degree:',  k)
    rad = (k * round(pi, 3))/180
    print("Output radian:", round(rad, 6))
get_radian()