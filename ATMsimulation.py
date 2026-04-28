from datetime import datetime
balance = 1000
transactions = []
PIN = "1234"

def login():
    for _ in range(3):
        entered = input("Enter PIN: ")
        if entered == PIN:
            print("Login successful!\n")
            return True
        else:
            print("Wrong PIN")
    return False


def display_balance():
    print(f"\nCurrent Balance: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    transactions.append(f"{datetime.now()} - Deposited ₹{amount}")
    print("Deposit successful!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        transactions.append(f"{datetime.now()} - Withdrew ₹{amount}")
        print("Withdrawal successful!")

def transfer():
    global balance
    amount = float(input("Enter amount to transfer: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        account = input("Enter receiver account number: ")
        balance -= amount
        transactions.append(f"{datetime.now()} - Transferred ₹{amount} to {account}")
        print("Transfer successful!")

def show_statement():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print("-", t)

def menu():
    print("\n===== ATM MENU =====")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Show Statement")
    print("6. Exit")

if not login():
    print("Too many incorrect attempts. Exiting...")
    exit()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        display_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        transfer()
    elif choice == "5":
        show_statement()
    elif choice == "6":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice! Please try again.")

