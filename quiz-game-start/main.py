from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from display import logo

##### CONVERTS THE DATA DICTIONARY TO A LIST OF OBJECTS CALLED QUESTION_BANK  #############
question_bank = []
for item in question_data:
    new_question = Question(item["text"], item["answer"])
    question_bank.append(new_question)
print(question_bank)

####### CREATE A NEW OBJECT quiz FROM QUIZBRAIN CLASS ##############
quiz = QuizBrain(question_bank)

######## QUESTION FUNCTIONALITY #################
while quiz.still_has_question():
    print(logo)
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")




