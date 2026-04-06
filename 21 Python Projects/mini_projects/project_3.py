import random

print("Welcome to Rock, Paper and Scissors!")

items = ["rock", "paper", "scissors"]
score = {
    "player": 0,
    "computer": 0
}

while True:
    user_input = input("Please choose rock, paper, scissors or Q to quit: ").lower()

    if user_input == "q":
        print(f"Final Scores - Player: {score['player']} , Computer: {score['computer']}")
        print("See you again, next time, BBye!")
        break

    if user_input not in items:
        print("Invalid choice! Please type rock, paper or scissors.")
        continue

    computer_choice = random.choice(items)
    choices = [user_input, computer_choice]
    choices_dict = {"player": user_input, "computer": computer_choice}

    print(f"Player's choice: {user_input}, Computer's choice: {computer_choice}")

    if user_input == computer_choice:
        print("This round was a tie!")
    elif ("rock" in choices) and ("paper" in choices):
        winner = [key for key, val in choices_dict.items() if val == "paper"][0]
        score[winner] += 1
        print("You win!" if winner == "player" else "Computer wins!")
    elif ("rock" in choices) and ("scissors" in choices):
        winner = [key for key, val in choices_dict.items() if val == "rock"][0]
        score[winner] += 1
        print("You win!" if winner == "player" else "Computer wins!")
    elif ("scissors" in choices) and ("paper" in choices):
        winner = [key for key, val in choices_dict.items() if val == "scissors"][0]
        score[winner] += 1
        print("You win!" if winner == "player" else "Computer wins!")

    print(f"Scores - Player: {score['player']} , Computer: {score['computer']}")