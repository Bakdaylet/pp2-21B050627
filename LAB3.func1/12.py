def histogramm(list):
    a = [['*'] * list[i] for i in range(len(list))]
    for row in a:
        print(''.join([str(elem) for elem in row]))
x = list(map(int, input().split()))
histogramm(x)