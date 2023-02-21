def returns(n):
    for i in range(n+1):
        yield n - i
n = int(input())
returns(n)
for item in returns(n):
    print(item, end  = " ")