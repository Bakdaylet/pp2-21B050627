def check_palindrome(sequence):
    ok = True
    for n, m in zip(sequence, reversed(sequence)):
        if n != m:
           ok  =  False
        else:
            ok = True
    if ok:
        print('Ok')
    else:
        print('Nope')
x = input()
check_palindrome(x)