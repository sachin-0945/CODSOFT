import random

def main():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"You chose: {user_choice},\nComputer chose: {computer_choice}.")

        if (user_choice == "rock" and computer_choice == "scissors") or \
           (user_choice == "paper" and computer_choice == "rock") or \
           (user_choice == "scissors" and computer_choice == "paper"):
            print("User wins!")
        elif user_choice == computer_choice:
            print("It's a tie!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes(y) / no(n)): ")
        if play_again.lower() != "y":
            break

if __name__ == "__main__":
    main()