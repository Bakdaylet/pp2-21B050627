def print_even(N):
    for i in range(1,N):
        if i % 2 == 0:
           yield i 
N = int(input())
print_even(N)
for item in print_even(N):
    print(item, end = ", ")