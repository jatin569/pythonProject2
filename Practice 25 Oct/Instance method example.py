# write a python program to create a Bank class where deposits and withdrawals can be handled by using instance method
class Bank(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance=self.balance-amount
            return self.balance
name = input("Enter name: ")
b = Bank(name,3000)
b.deposit(5000)

