def all_perms(somestring):
   from itertools import permutations 
   lst = [''.join(p) for p in permutations(somestring)]
   for i in lst:
       print(i)
somestring = input()
all_perms(somestring)