class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.lower():
            print("You are right!")
            self.current_score += 1
        else:
            print("Sorry! You were wrong!")
        print(f"The answer was: {correct_answer}")
        print(f"Your current score is {self.current_score}/{self.question_number+1}")

    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1} {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(user_answer,self.question_list[self.question_number].answer)
        self.question_number += 1
        while not self.still_has_questions():
            print("\nYou have completed the quiz!")
            print(f"Your final score is {self.current_score}/{self.question_number}")
            break