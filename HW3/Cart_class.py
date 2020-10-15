import sqlite3

conn = sqlite3.connect('Users.db')

c = conn.cursor()

class Cart():
    def __init__(self, total_cost = 0, total_item_count = 0,unique_item_count = 0, items = {} ):
        self.total_cost = total_cost
        self.total_item_count = total_item_count
        self.unique_item_count = unique_item_count
        self.items = items

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

    def addToCart(self, item, qty):
        ##total_item_count += amount
        if not self.items.__contains__(item):
            self.items[item] = int(qty)
            self.unique_item_count += 1  
            
            #updateCost(item, qty, price)
            #print(total_cost)
            

        else:
            current = self.items.get(item)
            self.items[item] = current + int(qty)
            #print(total_cost)
            #total_cost = updateCost(item, qty)
            

        print("Successfully added %s %ss to cart!" % (qty, item))

        self.showContents()
        return 0
           
    def showContents(self):
        for item in self.items.items():
            print(item)

    def confirmPurchase():
        pass

    def checkOut():
        pass

    def updateCost(self, item, qty, option):
        #1 is for adding items from total
        #0 is for removing items from total
        c.execute("SELECT Price FROM Inventory WHERE Name='%s'" % item)
        price = c.fetchone()
        price = float(price[0])
        if option == 1:
            self.total_cost += price * int(qty)
        elif option == 0:
            self.total_cost -= price * int(qty)
        return self.total_cost

            
    def isInCart(self, item, qty):
        key,value = item, int(qty)
        if key in self.items and value <= self.items[key]:
            return True
        else:
            return False

