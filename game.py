import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choices: rock, paper, scissors")
    
    user = input("Enter your choice: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])
    
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")
    
    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return "You win!"
    
    return "You lose!"

def is_win(player, opponent):
    # return True if player beats opponent
    if (player == "rock" and opponent == "scissors") or \
       (player == "scissors" and opponent == "paper") or \
       (player == "paper" and opponent == "rock"):
        return True
    return False

# Run the game
print(play())
