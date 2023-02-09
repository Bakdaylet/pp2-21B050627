from random import randint
n = randint(1, 20)
def Guess_the_number():
    print('Hello! What is your name?')
    name  = input()
    cnt = 0
    print("Well,",name,', I am thinking of a number between 1 and 20.')
    print("Take a guess.")
    print(n)
    c = randint(1, 20)
    if n == c:
         print("Good job,",name,"!" "You guessed my number in  1 guesses!")
         return 
    else :
        for i in range(20):
            c = randint(1, 20)
            if n != c:
               print("Your guess is too low.")
               print("Take a guess.")
               print(c)
            elif n == c:
                cnt = i+1
                print("Good job,",name,"!" "You guessed my number in", cnt , "guesses!")
                break
            else:
                continue
Guess_the_number()
