###### CREATE A NEW CLASS CALLED QUIZBRAIN TO HOLD THE FUNCTIONALITIES ####################
###########################################################################################
class QuizBrain:
    # CREATE ATTRIBUTES QUESTION NUMBER, CURRENT SCORE, AND QUESTION LIST
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # CREATE A NEW METHOD CALLED TO CHECK IF THERE IS STILL QUESTIONS TO ANSWER
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    # return self.question_number < len(self.question_list) works same as above ##########

    # CREATE A NEW METHOD TO DISPLAY SUBSEQUENTS QUESTIONS
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True/False)')
        self.check_answer(user_answer, current_question.answer)

    # CREATE A NEW METHOD TO CHECK ANSWER AGAINST THE CORRECT ANSWER FROM THE QUESTION DATA ############
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")

        else:
            print('That\'s wrong')
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
