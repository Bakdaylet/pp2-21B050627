def calculate_upper_and_lower(word):
    count_upp = 0
    count_low = 0
    for i in word:
        if i >= 'A' and i <= 'Z':
              count_upp += 1
        else:
            count_low += 1
    print(count_upp)
    print(count_low)
x = input()
calculate_upper_and_lower(x)
