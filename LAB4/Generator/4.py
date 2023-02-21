def square_from_to(a, b):
    for i in range(a, b):
        yield i**2 
x, y = map(int, input().split())
square_from_to(x, y)
for item in square_from_to(x, y):
    print(item)