class Account:  
    pass
    def __init__(self,  owner_attributes, balance):
          self.owner_attributes = owner_attributes
          self.balance = int(balance)
    def deposit(self, deposit):
         return self.balance + deposit   
    def withdraw(self, sum):      
         if self.balance >= sum:
            print("Yes, you can  withdraw this sum")
         else:
            print("Account was overdrawn")
Name, Balan =  input().split()
dep = Account(Name, Balan)

depos = int(input())
print(dep.deposit(depos))

sum = int(input())
print(dep.withdraw(sum))