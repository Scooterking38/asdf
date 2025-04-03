import json

# Load the JSON data from a file (e.g., 'data.json')
with open('data.json', 'r') as file:
    parsed_data = json.load(file)

# Initialize a list to store question numbers and answers
question_answers = []

# Iterate through the questions and extract question number and correct answer
for question in parsed_data['questions']:
    question_number = question['number']
    correct_answers = question['correctAnswers']
    
    # Extract the first correct answer (assuming there's only one)
    answer = correct_answers[0] if correct_answers else None
    
    question_answers.append((question_number, answer))

# Output the results
for question_number, answer in question_answers:
    print(f"Question {question_number}: {answer}")
