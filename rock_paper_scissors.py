import random

VALID_CHOICES = ["rock", "paper", "scissors"]

def get_user_choice():
    """Gets and validates the user's choice."""
    while True:
        user_input = input(f"Enter your choice ({', '.join(VALID_CHOICES)}): \n").lower()
        if user_input in VALID_CHOICES:
            return user_input
        else:
            print(f"Invalid input. Please enter one of: {', '.join(VALID_CHOICES)}.")

def get_computer_choice():
    """Randomly selects the computer's choice."""
    return random.choice(VALID_CHOICES)

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "🎉🍾🥂🎉 You win!"
    else:
        return "😜😜 You lose!"

def play_game():
    """Runs the main game loop."""
    print("\n--- Rock Paper Scissors ---")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    print("-------------------------\n")

if __name__ == "__main__":
    play_game()