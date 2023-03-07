from time import sleep
import math
t = int(input())
n = int(input())
def invoke_sleeping(num, ms, *args):
    sleep(ms/1000)
    return num(*args)
print("Square root of", n , "after", t ,"specific miliseconds is", invoke_sleeping(lambda x: math.sqrt(x), t, n)) 