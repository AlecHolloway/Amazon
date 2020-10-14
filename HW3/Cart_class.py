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

    def removeFromCart():
        pass

    def addToCart(self, item, amount):
        ##total_item_count += amount
        self.unique_item_count += 1

        self.items[self.unique_item_count] = item
        self.items["%d.qty" % self.unique_item_count] = int(amount)

        print("Successfully added %s %ss to cart!" % (amount, item))

        self.showContents()
        return 0
    
    #def addToCart(self):
    #    b = 1
    #    cost = 0
    #    current_item = None
    #    while(b==1):
    #       current_item = input("Select: ")
    #       qty = int(input("How many?"))
    #       items = {current_item, qty}
    #       cost = queuePrice(current_item)
    #       total_cost += qty * cost
    #       b = input("Continue. 1 or 0")
           

    
       # return 0

    def showContents(self):
        for item in self.items.items():
            print(item)


    def confirmPurchase():
        pass

    def checkOut():
        pass

    def updateCost():
        pass
