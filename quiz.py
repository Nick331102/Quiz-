class Quiz:
    def __init__(self, questions, answers):
        self.questions = []
        self.answers = []
    
    # take a question and answer as parameters, and append to their respective lists
    def add_question(self, question, answer):
        self.questions.append(question)
        self.answers.append(answer)
     
     # take an index as an argument and remove the corresponding question and answer from the lists   
    def remove_question(self, index):
        del self.questions[index]
        del self.answers[index]
        
    def take_quiz(self):
        score = 0
        for i in range(len(self.questions)):
            answer = input()
        
        