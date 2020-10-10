from user import User
from Database import *
from inventory_class import *
from Cart_class import *

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
        
        allItems() ##from database file. Part d of assignment
        print("\n")
        print("\n")
        print("Creating cart. Type one item at a time to add to cart")
        #newCart = Cart()
        #newCart.addToCart()

        
      




                
       

    if choice == "2":
        print("Create new account\n")
        userName = input("Enter username: ")
        password = input("Enter password: ")
        creditCard = input("Enter Credit Card Number: ")
        address = input("Enter address: ")

        newUser = User(userName, password)
        newUser.addUsertoDatabase(userName, password, creditCard, address)
        


main()