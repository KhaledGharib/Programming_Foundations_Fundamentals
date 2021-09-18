#withdraw
import sys
def bank(balance):
    print("Your balance is $",balance)
    amount1=float(input("Enter the amount $"))
    if amount1>balance:
        sys.exit("💸 We sorry your balance not enough 💸") #end code
    elif (amount1 <= balance):
        balance=balance - amount1
        print("--------------------------------")

        return balance
 

balance = bank(100)
 
if balance <= 10:
    print("Your balance now is $",balance," make a deposit")
else:
    print ("Your balance now is $",balance)
print("Thanks for being our customer😍")
