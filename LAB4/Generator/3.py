def print_divisible(N):
    for i in range(1,N):
        if i % 3 == 0 and i % 4 == 0:
           yield i 
N = int(input())
print_divisible(N)
for item in print_divisible(N):
    print(item, end = " ")