class Order:
    def __init__(self,name,address,order_id,price):
        self.name=name
        self.address=address
        self.order_id=order_id
        self.price=price

    def details(self):
        print("Name is {}\nAddress {}\nOrder id {}\nprice {}".format(self.name,self.address,self.order_id,self.price))
od=Order("Jatin","Bangalore",981561654,2000)

od.details()