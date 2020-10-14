from user import User
##from Database import *
from inventory_class import *
from Cart_class import *

inventory = Inventory()
newCart = Cart()

def main():
    print("Welcome to our store\n")
    choice = input("Login or Create Account 1 or 2: \n")
    ##print(type(choice))
    #print(choice)
    
    #while choice != "1" or choice != "2":
      ##  choice = input("Please select 1 or 2: \n")

    if choice == "1":
        n = 'y'
        while(n == 'y'):
            print("Enter Credentials\n")
            userName = input("Enter username: \n")
            password = input("Enter password: \n")
            user = User(userName, password)
            a = user.verify(userName, password)
            if(a == True):
                print("Sucessfully logged in")
                n = 1
            else:
                print("Error logging in")
                n = input("Try again? y/n") ## iterate until successful attempt

        print("\n")
        print("Welcome to the Store, our items are listed below:")
        
        ##inventory = Inventory()
        inventory.displayItems() ## part d of assignment
        print("\n")
        print("\n")
        print("Creating cart. Type one item at a time to add to cart")

        WaitForUserToAddItem()





                
       

    if choice == "2":
        print("Create new account\n")
        userName = input("Enter username: ")
        password = input("Enter password: ")
        creditCard = input("Enter Credit Card Number: ")
        address = input("Enter address: ")

        newUser = User(userName, password)
        newUser.addUsertoDatabase(userName, password, creditCard, address)
        

def WaitForUserToAddItem():
        item = input("Name of item: ")
        if inventory.VerifyItemIsInDatabase(item):
            qty = input("How many? ")
            print("Adding %s %ss to cart..." % (qty , item))
            newCart.addToCart(item, qty)

        WaitForUserToAddItem()

main()