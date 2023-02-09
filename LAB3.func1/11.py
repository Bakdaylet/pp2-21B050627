def palindrome(words):
    dict = words
    words = words[::-1]
    if dict == words:
        print('Palindrome!')
    else:
        print("Not a palindrome")
x = input()
palindrome(x)