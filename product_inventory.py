class Product(object):

    def __init__(self,id,price,quantity):
        self.id = id
        self.price = price
        self.quantity = quantity


class Inventory(Product)
    def add_to_inventory(self,id,price,quantity):
        self.id = id
        self.price = price
        self.quantity=quantity

    def remove(self,n):
        if self.quantity > n:
            print("id="+self.id + " " + "price="+ self.price+" "+"quantity"+self.quantity)
        else:
            print("item not available")


