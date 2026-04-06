import json
print("Welcome!")
user = input("Please Enter your name: ")
score = 0
playing_or_not = input(f"Hello {user}!, Do you want to play this quiz? yes/no: ").lower()
if playing_or_not == "no":
    print("Bye, Good to see you!")
else:

    with open("data/questions.json", "r") as file:
        questions = json.load(file)

    for question in questions:
        current_question = question["question"]
        correct_answer = question["answer"]
        users_answer = input(f"{current_question}: ").lower()
        if users_answer == correct_answer:
            print("You are right!")
            score+=1
        else:
            print("You are wrong!")

    print(f"{user}'s final score is {score}/5")