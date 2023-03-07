def get_list_multiplication(numbers):
    result = 1
    for i in numbers:
        result = result * i
    print(result)
list1 = list(map(int , input().split()))
get_list_multiplication(list1)