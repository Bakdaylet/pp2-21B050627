def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(arr):
    new = []
    for i in arr:
        if isPrime(i) == True:
            new.append(i)
    return new
arr = list(map(int, input().split()))
print(sorted(filter_prime(arr)))