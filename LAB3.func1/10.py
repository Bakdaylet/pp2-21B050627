def unique(list):
    new = []
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            new.append(list[i])
        else:
            continue
    for i in new:
        print(i, end = ' ')
x = list(map(int, input().split()))
unique(x)