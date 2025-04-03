import json

# Load the JSON data from a file (e.g., 'data.json')
try:
    with open('data.json', 'r') as file:
        parsed_data = json.load(file)
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
    exit()

# Debug: Print the loaded data to confirm the structure
print("Loaded JSON data:")
print(json.dumps(parsed_data, indent=2))  # Pretty print the JSON to inspect the structure

# Initialize a list to store question numbers and answers
question_answers = []

# Iterate through the questions and extract question number and correct answer
for question in parsed_data.get('questions', []):  # Safely get 'questions' key
    question_number = question.get('number')
    correct_answers = question.get('correctAnswers', [])

    if correct_answers:
        answer = correct_answers[0]  # Assume the first correct answer
        question_answers.append((question_number, answer))

# If no answers were found, print a message
if not question_answers:
    print("No questions or answers found.")
else:
    # Output the results
    print("\nParsed Question and Answers:")
    for question_number, answer in question_answers:
        print(f"Question {question_number}: {answer}")
