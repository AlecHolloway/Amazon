from user import User
from inventory_class import *
from Cart_class import *

inventory = Inventory()
newCart = Cart()

total = 0
def main():

    print("Welcome to Amazon!\n")
    choice = input("Login or Create Account 1 or 2: ")

    if choice == "1":
        n = 'y'
        while(n == 'y'):
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            a = user.verify(username, password)
            if(a == True):
                print("Sucessfully logged in")
                n = 1
                customerChoice(username, password)
            else:
                print("Error logging in")
                n = input("Try again? y/n") ## iterate until successful attempt
       
    if choice == "2":
        print("Create new account\n")
        userName = input("Enter username: ")
        password = input("Enter password: ")
        creditCard = input("Enter Credit Card Number: ")
        address = input("Enter address: ")

        newUser = User(username, password)
        newUser.addUsertoDatabase(username, password, creditCard, address)

       
def customerChoice(username, password):
    while True:
        print("1: Add items to cart\n2: Remove items from cart\n3: View cart\n4: Checkout \n5: View Pass Purchases \n6: Logout")
        option = int(input("What would you like to do? "))
        if option == 1:
            inventory.displayItems() ## part d of assignment
            print("\n")
            item = input("What item would you like to add to cart? ")
            if inventory.VerifyItemIsInDatabase(item):
                qty = input("How many? ")
                print("Adding %s %ss to cart..." % (qty , item))
                newCart.addToCart(item, qty)

                total_cost = newCart.updateCost(item, qty, 1)
                print("Total: ", total_cost)
            else:
                print("Could not find item in database!\n")
               
                
                
                
        elif option == 2:
            item = input("Name of item: ")
            qty = input("How many? ")
            if newCart.isInCart(item, qty):
                print("Removing %s %ss from cart..." % (qty , item))
                newCart.removeFromCart(item, qty)

           
                total_cost = newCart.updateCost(item, qty, 0)
                print("Total: ", total_cost)

            else:
                print("Could not find item in Cart!\n")
                WaitForUserToChooseOption()

        elif option == 3:
            newCart.showContents()
        elif option == 4:
            newCart.checkOut(username, password)
        elif option == 5:
            inventory.viewPastPurchases(username)
        elif option == 6:
            User.logout()
        else:
            print("Incorrect input. Please try again\n")
                



main()
