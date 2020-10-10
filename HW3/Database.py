##https://docs.python.org/3/library/sqlite3.html

import sqlite3

conn = sqlite3.connect('Users.db')

c = conn.cursor()



def addUserData(self, username, password, creditCard, address):
    
    userData = (username, password, creditCard, address)                #place holders for variable substitution. reference sqlite api
    c.execute("INSERT INTO Users (username, password, credit, address) VALUES (?, ?, ?, ?)", userData)
    
    # Save (commit) the changes
    conn.commit()
    print("successfully added to database")
    conn.close()


def searchUser(self, username, password):
    userData = (username, password)
    ##check if data exists
    c.execute("SELECT Username, Password FROM Users WHERE Username=? and Password=?", userData)

    
    exists = c.fetchone() ##returns none if no match
    #for row in c:
       # print(row)
    
    if exists:
        return True
    else:
        return False



def allItems():
     c.execute("SELECT Name, Description, Price FROM Inventory")
     for row in c:
         print(row)
     return 0


#def queuePrice(item):
#    items = (item,)
#    c.execute("SELECT Price FROM Inventory WHERE Name=?", items)
#    cost = c.fetchone()
#    int(cost[0])
#    return cost[0]


##def removeItem(item):
