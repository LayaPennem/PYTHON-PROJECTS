import random

# Step 1: Initialize scores
user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

# Step 2: Display a welcome message
print(" Welcome to Rock-Paper-Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.\n")

# Step 3: Start the game loop
while True:
    # Step 4: Get user input
    user_choice = input("Your move: ").lower()
    
    if user_choice == "quit":
        print("\n Exiting game...")
        break

    if user_choice not in options:
        print("❌ Invalid input. Please choose rock, paper, or scissors.\n")
        continue

    # Step 5: Generate computer's random choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Step 6: Decide the winner
    if user_choice == computer_choice:
        print(" It's a tie!\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("✅ You win this round!\n")
        user_score += 1
    else:
        print("💻 Computer wins this round!\n")
        computer_score += 1

    # Step 7: Show current score
    print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

# Step 8: Final result
print("Final Score:")
print(f"You: {user_score} | Computer: {computer_score}")
if user_score > computer_score:
    print("🎉 Congratulations! You won the game!")
elif user_score < computer_score:
    print("😢 You lost! Better luck next time!")
else:
    print("🤝 It's a tie!")
