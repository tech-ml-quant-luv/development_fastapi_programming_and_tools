from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    ques = Question(item["text"], item["answer"])
    question_bank.append(ques)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations! You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")