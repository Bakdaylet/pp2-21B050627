def reversed_string(sentences):
    sentences = sentences[::-1]
    for i in sentences:
        print(i,end = ' ')
list = list(map(str, input().split()))
reversed_string(list)