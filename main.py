from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
'''
we're going to be initializing that QuizBrain and the value that we're going to put in there as the question list is going to be the question bank. This way we'll receive the question bank and it will be inside this question list attribute.
'''
quiz = QuizBrain(question_bank)

# in our while loop, we can check to see if the quiz still has questions. And if this is true, then go to the next question. But if it's false, then exit the loop and we're at th end of the game.

while quiz.still_has_questions(): #if quiz still has questions remaining:
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Final Score: {quiz.score}/{quiz.question_number}")