from math import*
def find_regular_polygon(n, a):
    print('Input number of sides:', n)
    print('Input the length of a side:', a)
    S = int(n*(pow(a, 2))/(4*floor(tan(180/n))))
    print('Expected Output:', abs(S))
x, y = map(int, input().split())
find_regular_polygon(x, y)