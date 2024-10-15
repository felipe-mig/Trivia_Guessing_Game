class QuizBrain:
    
    def __init__(self, q_list):
        # So this means every time we create a new QuizBrain object from this class, it's ready going to have an attribute called question_number that set to zero.
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
        
    def  still_has_questions(self):
         return self.question_number < len(self.question_list)
    
        
    # we're gonna define a new method called the next_question, and this method is basically going to get hold of the current question and that is of course going to be from the question list. And then we're going to tap into that list and get hold of the item at the current question_number.
    def next_question(self):
        # This is the correct answer
        current_question = self.question_list[self.question_number]
        '''we actually need to increase the question number every single time we call next_question anyways,then once we've gotten hold of the current question, we can actually tap into that self.question_number and increase it by one.'''
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        '''
        And then I'm going to call our check_answer method and I want to pass over the user_answer. Now, in addition, I also want to pass over the correct answer and the correct answer is going to be the current_question.answer.
        '''
        self.check_answer(user_answer, current_question.answer)
        
    
    # we're going to create a new method called check_answer. And this check_answer function is going to be used to see if the user's answer which comes from this input is the same as the actual answer to the current question.
    def check_answer(self, user_answer, correct_answer ):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        # This is outside the if/else statement
        print(f"The corrects answer was: {correct_answer}.")
        # now we want to be able to print out what the users' current score is.
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        



