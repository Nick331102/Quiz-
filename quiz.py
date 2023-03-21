class Quiz:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
    
    def add_question(self, question_data):
        self.questions.append(question_data['question'])
        self.answers.append(question_data['answers'])
     
    def remove_question(self, index):
        del self.questions[index]
        del self.answers[index]
        
    def take_quiz(self):
        score = 0
        for i in range(len(self.questions)):
            # Display the question and answer choices
            print(f"{self.questions[i]}")
            for j, choice in enumerate(self.answers[i]):
                print(f"{j+1}. {choice}")
            
            # Get the user's answer
            answer_idx = int(input("Enter your answer (1-4): ")) - 1
            
            # Check if the answer is correct
            if self.answers[i][answer_idx] == self.answers[i][0]:
                score += 1
        # Display the results
        print(f"You got {score} out of {len(self.questions)} questions correct.")


# Create a Quiz object with two questions and answers
q = Quiz(["What color is the sky?", "What is the capital of France?"],
         [["blue", "green", "red", "yellow"], ["Paris", "Madrid", "Rome", "Berlin"]])

# Add a third question and answer
q.add_question({
    'question': 'What is the capital of Germany?',
    'answers': ['Berlin', 'Paris', 'Madrid', 'Rome']
})

# Take the quiz
q.take_quiz()
