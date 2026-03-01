def show_balance(current_balance):
    print(f"\n[Your current balance is: {current_balance} Kyats ]")

def withdraw(current_balance):
    amount = int(input("Enter amount to withdraw: "))
    if amount > current_balance:
        print("Insufficient balance!")
        return current_balance
    elif amount <= 0:
        print("Invalid amount!")
        return current_balance
    else:
        current_balance -= amount
        print(f"Success! You withdraw {amount} Kyats.")
        return current_balance
def deposit(current_balance):
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        current_balance += amount
        print(f"Success! You deposited {amount} Kyats.")
        return current_balance
    else:
        print("Invalid amount")
        return current_balance
balance = 1000000
pin = "1234"

enter_pin = input("Enter your PIN: ")

if enter_pin == pin:
    while True:
        print("\n---ATM Menu---")
        print("1. Check Balance")
        print("2. Withdrawl")
        print("3. Deposit")
        print("4. Exit")
    
        choice = input("Select an option (1-4)")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = withdrawl(balance)
        elif choice == "3":
            balance = deposit(balance)
        elif choice == "4":
            print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")
        
else:
    print("Incorrect PIN")