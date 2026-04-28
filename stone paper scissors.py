import random

choices = ["stone", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Wins!"


user_score = 0
computer_score = 0

def menu():
    print("\n===== GAME MENU =====")
    print("1. Play Game")
    print("2. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        rounds = int(input("Enter number of rounds: "))

        for i in range(rounds):
            print(f"\nRound {i+1}")
            user = input("Enter stone/paper/scissors: ").lower()

            if user not in choices:
                print("Invalid choice!")
                continue

            computer = get_computer_choice()
            print(f"Computer chose: {computer}")

            result = decide_winner(user, computer)
            print(result)

            if result == "You Win!":
                user_score += 1
            elif result == "Computer Wins!":
                computer_score += 1

        print(f"\nFinal Score → You: {user_score} | Computer: {computer_score}")

    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")