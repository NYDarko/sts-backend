"""
ussd program
"""

USSD = "*123#"
BALANCE = 1000
inp = input("Enter the ussd code to access the menu: ")
while True:
    if inp == USSD:
        print("1. Check Balance")
        print("2. Send Money")
        print("3. Buy Airtime")
        print("4. Quit")
        CHOICE = int(input())
        if CHOICE == 1:
            print(f"Your balance is {BALANCE}Ghs")
        elif CHOICE == 2:
            try:
                AMT = float(input("Enter amount in Ghs: "))
                recipient_no1 = input("Enter the recipient number")

            except ValueError:
                print("Please enter valid amount and phone number")
            else:
                if AMT <= BALANCE:
                    BALANCE -= AMT
                    print(f"You have sent {AMT} Ghs to {recipient_no1}, your new balance is {BALANCE}")
                else:
                    print("You do not have enough funds to perform this transaction")
        elif CHOICE == 3:
            try:
                BUY_CREDIT = float(input("Amount: "))
                recipient_no2 = input("Enter the recipient number: ")
            except ValueError:
                print("Please enter a valid amount and phone number")
            else:
                if BUY_CREDIT <= BALANCE:
                    AIRTIME = BUY_CREDIT / 2
                    BALANCE -= AIRTIME
                    print(f"You have bought {BUY_CREDIT}Ghs worth of airtime on {recipient_no2}, your balance is {BALANCE}Ghs")  
                else:
                     print("You do not have enough funds to perform this transaction") 
        elif CHOICE == 4:
            exit()

        else:
            print('Please choose from one of the options')

    else:
        print("Invalid code, please input *123# to access your portal")


