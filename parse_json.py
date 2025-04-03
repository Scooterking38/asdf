import json

# Load the JSON data from a file (e.g., 'data.json')
try:
    with open('data.json', 'r') as file:
        parsed_data = json.load(file)
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
    exit()

# Initialize a list to store question numbers and answers
question_answers = []

# Iterate through the questions and extract question number and correct answer
for question in parsed_data.get('questions', []):
    question_number = question.get('number')
    correct_answers = question.get('correctAnswers', [])

    if correct_answers:
        answer = correct_answers[0]  # Assume the first correct answer
        question_answers.append((question_number, answer))

# Output the results (only the question number and answer)
for question_number, answer in question_answers:
    print(f"Question {question_number}: {answer}")
