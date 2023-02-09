def agent_007(list):
    for i in range(len(list)-1):
        item = 0
        item1 = 7
        index1 = list.index(0)
        if list.index(item) < list.index(item1) and list.index(item, index1) < list.index(item1):
           return True 
    return False
x = list(map(int, input().split()))
agent_007(x)
print(agent_007(x))

