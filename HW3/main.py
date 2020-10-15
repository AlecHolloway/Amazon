from user import User
##from Database import *
from inventory_class import *
from Cart_class import *

inventory = Inventory()
newCart = Cart()

def main():
    print("Welcome to Amazone!\n")
    choice = input("Login or Create Account 1 or 2: ")

    if choice == "1":
        login()
       
    if choice == "2":
        createAccount()

    print("\n")
    print("Welcome to Amazone, our items are listed below:")
        
    inventory.displayItems() ## part d of assignment
    print("\n")

    WaitForUserToChooseOption()

def login():
    n = 'y'
    while(n == 'y'):
        userName = input("Enter username: ")
        password = input("Enter password: ")
        user = User(userName, password)
        a = user.verify(userName, password)
        if(a == True):
            print("Sucessfully logged in")
            n = 1
        else:
            print("Error logging in")
            n = input("Try again? y/n") ## iterate until successful attempt

def createAccount():
    print("Create new account\n")
    userName = input("Enter username: ")
    password = input("Enter password: ")
    creditCard = input("Enter Credit Card Number: ")
    address = input("Enter address: ")

    newUser = User(userName, password)
    newUser.addUsertoDatabase(userName, password, creditCard, address)
        
def WaitForUserToAddOrRemoveItem(choice):
    inventory.displayItems()

    if choice == 1:
        item = input("What item would you like to add to cart? ")
        if inventory.VerifyItemIsInDatabase(item):
            qty = input("How many? ")
            print("Adding %s %ss to cart..." % (qty , item))
            newCart.addToCart(item, qty)

        else:
            print("Could not find item in database!\n")
            WaitForUserToChooseOption()

    elif choice == 2:
        item = input("Name of item: ")
        if inventory.VerifyItemIsInDatabase(item):
            qty = input("How many? ")
            print("Removing %s %ss from cart..." % (qty , item))
            newCart.removeFromCart(item, qty)

        else:
            print("Could not find item in database!\n")
            WaitForUserToChooseOption()

def WaitForUserToChooseOption():
    print("1: Add items to cart\n2: Remove items from cart\n3: View cart\n4: Checkout\n5: Exit")
    try:
        option = int(input("What would you like to do? "))
    except:
        print("Incorrect input. Please try again\n")
        WaitForUserToChooseOption()

    if option == 1 or option == 2:
        WaitForUserToAddOrRemoveItem(option)
        WaitForUserToChooseOption()

    elif option == 3:
        newCart.showContents()
        WaitForUserToChooseOption()

    elif option == 4:
        WaitForUserToChooseOption()

    elif option == 5:
        exit()

    else:
        print("Incorrect input. Please try again\n")
        WaitForUserToChooseOption()

main()