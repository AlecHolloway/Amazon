import sqlite3

conn = sqlite3.connect('Users.db')

c = conn.cursor()

class Cart():
    
    def __init__(self): 
        self.cart = "Cart"
        self.total_cost = 0
        self.total_item_count = 0
        self.unique_item_count = 0
        self.items = {} #dictionary used to store item and qty

    def removeFromCart(self, item, amount):
        if self.items.__contains__(item):
            current = self.items.get(item)
            updated = current - int(amount)
            if updated <= 0:
                self.items.pop(item)
            else:
                self.items[item] = updated

            print("Successfully removed %s %ss from cart!" % (amount, item))
            self.showContents()

        else:
            print("Could not remove %s %ss from cart!" % (amount, item))
        return 0

    def addToCart(self, item, amount):
        ##total_item_count += amount
        if not self.items.__contains__(item):
            self.items[item] = int(amount)
            self.unique_item_count += 1

        else:
            current = self.items.get(item)
            self.items[item] = current + int(amount)

        print("Successfully added %s %ss to cart!" % (amount, item))

        self.showContents()
        return 0
           
    def showContents(self):
        for item in self.items.items():
            print(item)

    def confirmPurchase():
        pass

    def checkOut():
        pass

    def updateCost():
        pass
