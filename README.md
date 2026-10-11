# Project Title: asdf

## One-line Tagline
A Python script to parse JSON data containing questions and answers.

## Architecture Overview
The `asdf` repository is structured with a simple yet effective architecture designed for parsing JSON data. The primary components are:

- **parse_json.py**: A Python script responsible for loading and processing the JSON data.
- **data.json**: A JSON file containing structured data, specifically questions and their correct answers.
- **mem**: An empty directory that could be used for storing additional resources or temporary files in future enhancements.

The `parse_json.py` script reads from `data.json`, extracts question numbers and their corresponding correct answers, and prints them out. This setup is ideal for applications requiring data extraction and processing from structured JSON inputs.

## Tech Stack
- **Programming Language**: Python 3.x
- **Libraries/Frameworks**:
  - `json`: Built-in library for parsing JSON files.

## Getting Started / Setup Guide

### Prerequisites
Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation
1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/yourusername/asdf.git
   cd asdf
   ```

2. **Prepare Data**:
   - Ensure that `data.json` is present in the root directory of the repository. This file should contain valid JSON data structured with a key named 'questions', where each question has a 'number' and 'correctAnswers'.

3. **Run the Script**:
   ```bash
   python parse_json.py
   ```

### Example Data Structure for `data.json`
```json
{
  "questions": [
    {
      "number": 1,
      "correctAnswers": ["Answer A"]
    },
    {
      "number": 2,
      "correctAnswers": ["Answer B"]
    }
  ]
}
```

This setup will output:
```
Question 1: Answer A
Question 2: Answer B
```

### Additional Notes
- The script assumes that each question has at least one correct answer. If a question lacks correct answers, it will be skipped.
- The `mem` directory is currently empty but can be utilized for future enhancements or to store additional resources like logs or configuration files.

Feel free to extend the functionality of this script by adding more features such as error handling, data validation, or integration with other systems.