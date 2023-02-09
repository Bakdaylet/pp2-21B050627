def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] and nums[i] == 3:
           return True 
    return False
x = list(map(int, input().split()))
has_33(x)
print(has_33(x))
