def print_square(N):
    for i in range(1,N):
        yield i**2 
N = int(input())
print_square(N)
for item in print_square(N):
    print(item)