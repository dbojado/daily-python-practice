#Create a ATM program with ability to show balance, withdraw from account, deposit into account, and end session

while True: 
    balance = 10000
    print("     ATM     ")
    print("""
    1)          Balance
    2)          Withdraw
    3)          Deposit
    4)          Quit Session
    """)

    try: 
        Option = int(input("Enter Option: "))
    except Exception:
        print("Error: ", Exception)
        print("Enter 1, 2, 3 or 4 only")
        continue

    if Option == 1:
        print("Balance $ ", balance)

    if Option == 2:
        print("Balance $ ", balance)
        Withdraw = float(input("Enter Withdraw Amount $ "))
        if Withdraw > 0:
            new_balance = (balance - Withdraw)
            print("New Balance $ ", new_balance)
        elif Withdraw > balance:
            print("Not enough funds in account")
        else: 
            print("No withdraw made")

    if Option == 3:
        print("Balance $ ", balance)
        Deposit = float(input("Enter Deposit Amount $ "))
        if Deposit > 0:
            new_balance = (balance + Deposit)
            print("New Balance $ ", new_balance)
        else: 
            print("No deposit made")

    if Option == 4:
        exit()
    