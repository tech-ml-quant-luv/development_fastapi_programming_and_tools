import random

number = random.choice(range(100))
correct_guess = False
trials = 0
while not correct_guess:
    trials += 1
    user_input = int(input("Please guess a number: "))
    if user_input<number:
        print("Too Low")
    elif user_input>number:
        print("Too High")
    else:
        print(f"You guessed it right in {trials} trials!")
        correct_guess=True


