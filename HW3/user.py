##https://docs.python.org/3/library/sqlite3.html
import sqlite3

conn = sqlite3.connect('Users.db')

c = conn.cursor()

class User:

    username = None
    password = None
    creditCard = None
    address = None

    # default constructor 
    def __init__(self, username, password): 
        self.username = username
        self.password = password
        
    # a method for getting and setting data members 
    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getCreditCard(self):
        return self.creditCard

    def getAddress(self):
        return self.address

    def setUsername(self, userName):
        self.username = username
        return 0

    def setPassword(self, password):
        self.password = password

    def setCreditCard(self, creditCard):
        self.userCreditCard = creditCard

    def setAddress(self, address):
        self.address = address

    def addUsertoDatabase(self, userName, password, creditCard, address):
        userData = (userName, password, creditCard, address)                #place holders for variable substitution. reference sqlite api
        c.execute("INSERT INTO Users (username, password, credit, address) VALUES (?, ?, ?, ?)", userData)
    
        # Save (commit) the changes
        conn.commit()
        print("successfully added to database")
        conn.close()
        return 0


    def login():
        pass

    def logout():
        exit()

    def verify(self, userName, password):
        userData = (userName, password)
        ##check if data exists
        c.execute("SELECT Username, Password FROM Users WHERE Username=? and Password=?", userData)

    
        exists = c.fetchone() ##returns none if no match
        #for row in c:
           # print(row)
    
        if exists:
            return True
        else:
            return False
