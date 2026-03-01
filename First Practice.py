balance = 100000
user_pin = input("Enter your 4-digit PIN: ")
if user_pin == "1234":
    while True:
        print("\n--- ATM Menu---")
        print("1.Check Balance")
        print("2.Withdrawl Money")
        print("3.Exit")

        choice = input("Choose an option (1-3)")
        
        if choice == "1":
            print(f"Current Balnce: {balance} Kyats")
        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Success! Remaining balance: {balance}")
            else:
                print("Insufficient balnce!")
        elif choice == "3":
            print("Thank you for using our ATM.")
            break
        else:
            print("Invalid Option")
else:
    print("Wrong PIN!")