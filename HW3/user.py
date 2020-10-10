from Database import *

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
        addUserData(self,userName, password, creditCard, address)

    def login():
        pass

    def logout():
        pass

    def viewPastPurchases():
        pass

    def verify(self, userName, password):
        ##uses the searchUser function from database file to encapsulate better. Probably redundant but idk
        a = searchUser(self, userName, password)
        if a == True:
            return True
        else:
            return False
    