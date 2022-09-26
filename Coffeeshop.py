class Coffeeshop:

    
    def action(self, action):
        if action == "1":
            return self.menu
        elif action == "2":
            return "Adwaya's coffee shop was made by Adwaya Bage in 2018.                           The shop is open from 9am to 6pm, from Monday through Saturday."
        elif action =="3":
            return "The owner of this shop is Adwaya Bage.                                          You can call him anytime! His phone number is (253)272-2216."

    def __init__(self):
        self.coffee = 3.5
        self.milk = 1.5
        self.bull = 2.5
        self.stingyCustomer = 0
        self.normalCustomer = 0.3
        self.kindCustomer = 0.5
        self.VIP = 1
        self.god = 100
        self.menu=("MENU\n milk : $1.5\n redbull : $2.5\n coffee : $3.5")
        

    def calculatePrice(self, order):
        if order == "coffee":
            return self.coffee
        elif order == "milk":
            return self.milk
        elif order == "redbull":
            return self.bull
        else:
            return "$10000000000, just joking. I am sorry, we don't have that here"
        
    def addition(self, addition):
        if addition == "coffee":
            return self.coffee
        elif addition == "milk":
            return self.milk
        elif addition == "redbull":
            return self.bull
        elif addition == "no":
            return "$10000000000, just joking. Your final order is 1 myOrder"
        else:
            return "$10000000000, just joking. I am sorry, we don't have that here"
        

        
    def tip(self, tip):
        if tip == "0":
            return self.stingyCustomer
        elif tip == "0.3":
            return self.normalCustomer
        elif tip == "0.5":
            return self.kindCustomer
        elif tip == "1":
            return self.VIP
        elif tip == "100":
            return self.god
        

def main():

    C = Coffeeshop()
    print("Hi, welcome to Adwaya's coffee shop. What would you like to do first?")
    print("1. Order now")
    print("2. Learn more about the store")
    print("3. Have a contact with the shop owner")
    #need to assign a variable name to the input
    myAction=input("Please type here\n")
    print(C.action(myAction))
    
    myOrder = input("What would you like to buy?\n")
    print("This costs " + str(C.calculatePrice(myOrder)))
    myAddition = input("Anything else?\n")
    print("This costs " + str(C.addition(myAddition)))

    print(" -How much for Tip?-")
    print("0$")
    print("0.3$")
    print("0.5$")
    print("1$")
    print("100$")

    myTip = input("Please type number\n")
    print("Your total amount is "+ str((C.calculatePrice(myOrder))+(C.addition(myAddition))+(C.tip(myTip)))+" dollars")
    customerName = input("May I have your name?\n")
    print(customerName +", Thank you. Have a nice day!")
    

if __name__ == "__main__":
    main()
