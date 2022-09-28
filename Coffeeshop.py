class Coffeeshop:

    def __init__(self):
        self.menu = ("\n\nMENU\n 1. Black coffee : $1.5(S), $2(M), $2.5(L)\n 2. Expresso     : $2.5(S), $3(M), $3.5(L)\n 3. Latte        : $3.5(S), $4(M), $4.5(L)\n 4. Special Mocha: $4(S), $4.5(M), $5(L)")
        self.blackcoffee = 2
        self.expresso = 3
        self.latte = 4
        self.specialmocha = 4.5
        self.size = ("\nSIZE\n 1. S(small)\n 2. M(medium)\n 3. L(large)")
        self.S = -0.5
        self.M = 0
        self.L = 0.5
        self.stingyCustomer = 0
        self.normalCustomer = 0.3
        self.kindCustomer = 0.5
        self.VIP = 1
        self.God = 100
        
    def action(self, action):
        if action == "1":
            return self.menu
        elif action == "3":
            return "\nAdwaya's coffee shop was made by Adwaya Bage in 2018.\nThe shop is open from 9am to 6pm, from Monday through Saturday.\nThe adress is 827 N Tacoma Ave, Tacoma, WA 98403"+ self.menu
        elif action =="4":
            return "\nThe owner of this shop is Adwaya Bage.\nYou can call him anytime! His phone number is (253)272-2216.\n"+ self.menu

    def calculatePrice(self, order):
        if order == "1":
            return self.blackcoffee
        elif order == "2":
            return self.expresso
        elif order == "3":
            return self.latte
        elif order == "4":
            return self.specialmocha
        
    def calculateSize(self, size):
        if size == "1":
            return self.S
        elif size == "2":
            return self.M
        elif size == "3":
            return self.L
        
    def calculateTip(self, tip):
        if tip == "1":
            return self.stingyCustomer
        elif tip == "2":
            return self.normalCustomer
        elif tip == "3":
            return self.kindCustomer
        elif tip == "4":
            return self.VIP
        elif tip == "5":
            return self.God
    def payment(self, pay):
        if pay == "1":
            return "Apple Pay"
        elif pay == "2":
            return "PayPal"
        elif pay == "3":
            return "Credit card"
        elif pay == "4":
            return "Debit card"


def main():

    C = Coffeeshop()
    finalprice = 0
    finalorder = ""
    
    myProcedure = "clear"
    
    while myProcedure == "clear":
        print("\nHi, welcome to Adwaya's coffee shop! What would you like to do first?\n")
        print("1. Order now")
        print("2. Pay now")
        print("3. Learn more about the store")
        print("4. Have a contact with the shop owner\n")

        myAction=input("Please type the number here(choose your action): ")
        while (not myAction == "1") and (not myAction == "2") and (not myAction == "3") and (not myAction == "4"):
            print("Please choose the number from the list above.")
            myAction=input("Please type the number here(choose your action): ")
        else:
            while (not myAction == "2"):
                print(C.action(myAction))
                print("\nWhat would you like to buy?")
                myOrder = input("Please type the number here(choose your coffee): ")
                while (not myOrder == "1") and (not myOrder == "2") and (not myOrder == "3") and (not myOrder == "4"):
                    print("\nI am sorry. We don't have that here.")
                    print("Please choose the number from the list above.")
                    myOrder = input("Please type the number here(choose your coffee): ")
                else:
                    if myOrder == "1":
                        myChoice = ("black  coffee")
                    elif myOrder == "2":
                        myChoice = ("expresso")
                    elif myOrder == "3":
                        myChoice = ("latte")
                    else:
                        myChoice = ("special mocha")
                    print("\nSIZE\n 1. S(small)\n 2. M(medium)\n 3. L(large)")
                    print("\nWhich size would you like?")
                    mySize = input("Please type the number here(choose your size): ")
                    while (not mySize == "1") and (not mySize == "2") and (not mySize == "3"):
                        print("\nI am sorry. We only have Small, Medium, and Large size.")
                        print("Please choose the number from the list above.")
                        mySize = input("Please type the number here(choose your size): ")
                    else:
                        if mySize == "1":
                            mySML = ("small")
                        elif mySize == "2":
                            mySML = ("medium")
                        else:
                            mySML = ("large")
                        print("\nWould you like Hot, or Cold?")
                        myDrink = input("Please type 'hot' or 'cold': ")
                        while (not myDrink == "hot") and (not myDrink == "cold"):
                            myDrink = input("Please type 'hot' or 'cold': ")
                        else:
                            print("\nHow many cups would you like?")
                            myNumber = input("Please type the number here(choose your number): ")
                            it_is = True
                            while it_is == True:
                                print("The number is invalid.")
                                myNumber = input("Please type the number here(choose your number): ")
                                it_is = isinstance(myNumber, float)
                            else:
                                while (not int(myNumber)>=0):
                                    print("The number is invalid.")
                                    myNumber = input("Please type the number here(choose your number): ")
                                else:
                                    print("=============================================================")
                                    print("Confirmation: Your order is " + myNumber +"　cup(s) of "+ myChoice + "(" + (mySML) + "," + (myDrink)+ ")")
                                    print("              This costs $" + str(int(myNumber)*((C.calculatePrice(myOrder))+(C.calculateSize(mySize)))))
                                    print("=============================================================")
                                    finalorder = finalorder +"\n   "+ (myNumber +" cup(s) of "+ myChoice + " (" + mySML + "," + (myDrink)+ ") /$" + str(int(myNumber)*((C.calculatePrice(myOrder))+(C.calculateSize(mySize)))) )
                                    finalprice = finalprice + (int(myNumber))*((C.calculatePrice(myOrder))+(C.calculateSize(mySize)))
                                    print("Would you like to confirm or refresh your order?")
                                    myDecision = input("Pease type 'confirm' or 'refresh': ")
                                    while (not myDecision == "confirm") and (not myDecision == "refresh"):
                                        myDecision = input("Pease type 'confirm' or 'refresh': ")
                                    else:
                                        if myDecision == "refresh":
                                            finalprice = 0
                                            finalorder = ""
                                        else:
                                            print("Okay!")
                                            print("1. Order now")
                                            print("2. Pay now")
                                            print("3. Learn more about the store")
                                            print("4. Have a contact with the shop owner\n")
    
                                            myAction=input("Please type number here(choose your action): ")
                            
                            
            else:
                print("=============================================================")
                print("Confirmation: Your final order would be" + finalorder)
                print("=============================================================")
                print("Would you like to clear all your order or continue to pay?")
                myProcedure = input("Pease type 'clear' or 'continue': ")
                while (not myProcedure == "clear") and (not myProcedure == "continue"):
                    myProcedure = input("Please type 'clear' or 'continue': ")
                    if myProcedure == "clear":
                        finalprice = 0
                        finalorder = ""
    else:
        print("Okay!")
                    
    print("\n -How much for Tip?-\n")
    print("1.    0$")
    print("2.  0.3$")
    print("3.  0.5$")
    print("4.    1$")
    print("5.  100$")

    myTip = input("\nPlease type number here(choose your tip): ")
    while (not myTip == "1") and (not myTip == "2") and (not myTip == "3") and (not myTip == "4") and (not myTip == "5"):
        myTip = input("\nPlease type number here(choose your tip): ")
    else:
        if myTip == "5":
            print("\nThank you very very very much! You are such a nice person!!")
    print("Your total amount is $"+ str((finalprice) + (C.calculateTip(myTip))))
    print("What would you pay with?(※cash is not available)\n")
    print("1. Apple Pay")
    print("2. PayPal")
    print("3. Credit card")
    print("4. Debit card")
    print("5. other\n")
    myPay = input("Please type the number here(choose your payment method): ")
    while (not myPay == "1") and (not myPay == "2") and (not myPay == "3") and (not myPay == "4") and (not myPay == "5"):
        print("Please choose the payment from the list above.")
        myPay = input("Please type the number here(choose your payment method): ")
    else:
        if myPay == "5":
            payment = input("Please type the payment method: ")
        else:
            payment = C.payment(myPay)
    customerName = input("May I have your name?: ")
    print("Do you need the receipt?")
    receipt = input("Please type 'yes' or 'no': ")
    while (not receipt == "yes") and (not receipt == "no"):
        receipt = input("Please type 'yes' or 'no': ")
    else:
        if receipt == "no":
            print("Thank you, "+customerName+"! Your order has been recieved.\nCoffee will arrive in about ten minutes. Have a nice day!!")
        elif receipt == "yes":
            print("Thank you, "+customerName+"! Your order has been recieved.\nDrinks will arrive in about three minutes. Have a nice day!!\n\n")
            print(" =============================================================\n")
            print("      -Adwaya's Coffee Shop-\n\n  customer name:"+customerName+"\n  staff    name:Shu\n")
            print("  order        :"+finalorder+"\n  tip          :+$"+str(C.calculateTip(myTip)))
            print("  total  amount:$"+str((finalprice) + (C.calculateTip(myTip))))
            print("  payment type :"+payment+"\n")
            print("      Have a great day, "+customerName+"!!")
            print("\n =============================================================")
    



if __name__ == "__main__":
    main()
