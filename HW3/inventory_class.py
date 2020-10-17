import sqlite3

conn = sqlite3.connect('Users.db')

c = conn.cursor()

class Inventory():

    def displayItems(self):
        c.execute("SELECT Name, Description, Price FROM Inventory")
        for row in c:
            print(row)
        return 0

    def addItems():
        pass

    def removeItems():
        pass

    def VerifyItemIsInDatabase(self, string):
        c.execute("SELECT Name FROM Inventory WHERE Name = '%s'" % string)
        item = c.fetchone()
        if item:
            return True

        else:
            print("ERROR: Item not found in database")
            return False

    #probably should go in the user class but I had to change a lot of code to do that
    ## this was easier
    def viewPastPurchases(self, username):
        c.execute("SELECT * FROM PurchaseHistory WHERE User = '%s'" % username)
        item = c.fetchall()
        print(item)
        




