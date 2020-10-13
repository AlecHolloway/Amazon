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






