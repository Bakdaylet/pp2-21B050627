def check_tuple(items):
    result = all(items)
    print(result)
tuple1 = tuple(map(int, input().split()))
check_tuple(tuple1)