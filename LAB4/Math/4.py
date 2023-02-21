from math import*
def find_area_of_a_parallelogram(l, h):
    print('Length of base:', l)
    print('Height of parallelogram:', h)
    S = l * h
    print('Expected Output:', float(S))
x, y = map(int, input().split())
find_area_of_a_parallelogram(x, y)