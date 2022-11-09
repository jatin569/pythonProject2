class Father:
    def fname(self):
        print("father")
class Child(Father):
    def cname(self):
        print("child")
        pass
ob=Child()
ob.fname()
#other method
class Bank:
    cash=800000000
    @classmethod
    def available_cash(cls):
        print(cls.cash)

class AndhraBank(Bank):
    pass
class StateBank(Bank):
    cash=900000000
    @classmethod
    def available_cash(cls):
        print(cls.cash+Bank.cash)

a=AndhraBank()
a.available_cash()

s=StateBank()
s.available_cash()