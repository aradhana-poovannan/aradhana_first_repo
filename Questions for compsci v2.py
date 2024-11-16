import os
import json

# File to store user results
RESULTS_FILE = "quiz_results.json"

# Function to load quiz results from the file
def load_results():
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save a user's results to the file
def save_results(results):
    with open(RESULTS_FILE, "w") as file:
        json.dump(results, file)

# Function to calculate and display statistics
def show_statistics(results):
    if results:
        total_users = len(results)
        average_score = sum(r["score"] for r in results) / total_users
        print(f"\nTotal users who have completed the quiz: {total_users}")
        print(f"Average score: {average_score:.2f}")
    else:
        print("\nNo one has completed the quiz yet.")

# Greeting and instructions
def greet_user():
    name = input("What is your name? ")
    print(f"\nHello, {name}! Welcome to the quiz. For each question, please choose one of the given options. You will be asked to rate each question on a scale from 1 to 4, where:")
    print("1 - Not important at all")
    print("2 - Slightly important")
    print("3 - Moderately important")
    print("4 - Very important\n")
    return name

# Main quiz function
def run_quiz(name, results):
    score = 0  # Initialize the score variable

    # Question 1: Gender
    print("\n1. Are you female or male?")
    q1 = input("a. Female\nb. Male\nChoose a letter: ").lower()
    while q1 not in ['a', 'b']:
        print("Please choose one of the given options.")
        q1 = input("a. Female\nb. Male\nChoose a letter: ").lower()
    q1_answer = "Female" if q1 == "a" else "Male"
    print("Next...")

    # Preferred gender for match
    print("\n1. Would you like your match to be female or male?")
    p2q1 = input("a. Female\nb. Male\nChoose a letter: ").lower()
    while p2q1 not in ['a', 'b']:
        print("Please choose one of the given options.")
        p2q1 = input("a. Female\nb. Male\nChoose a letter: ").lower()
    p2q1_answer = "Female" if p2q1 == "a" else "Male"
    print("Next...")

    # Rank importance of the gender question
    q1rank = int(input("How important is this for you from 1-4? "))
    while q1rank < 1 or q1rank > 4:
        print("Please enter a number between 1 and 4.")
        q1rank = int(input("How important is this for you from 1-4? "))

    score += q1rank
    print(f"Current score: {score}")

    # Question 2: Age range
    print("\n2. Around what age are you?")
    q2 = input("a. 18-25\nb. 26-32\nc. 33-40\nd. 41-46\ne. 47+\nChoose a letter: ").lower()
    while q2 not in ['a', 'b', 'c', 'd', 'e']:
        print("Please choose one of the given options.")
        q2 = input("a. 18-25\nb. 26-32\nc. 33-40\nd. 41-46\ne. 47+\nChoose a letter: ").lower()
    q2_answer = {
        "a": "18-25", "b": "26-32", "c": "33-40", "d": "41-46", "e": "47+"
    }[q2]
    print("Next...")

    # Preferred age for match
    print("\n2. Around what age would you like your match to be?")
    p2q2 = input("a. 18-25\nb. 26-32\nc. 33-40\nd. 41-46\ne. 47+\nChoose a letter: ").lower()
    while p2q2 not in ['a', 'b', 'c', 'd', 'e']:
        print("Please choose one of the given options.")
        p2q2 = input("a. 18-25\nb. 26-32\nc. 33-40\nd. 41-46\ne. 47+\nChoose a letter: ").lower()
    p2q2_answer = {
        "a": "18-25", "b": "26-32", "c": "33-40", "d": "41-46", "e": "47+"
    }[p2q2]
    print("Next...")

    # Rank importance of the age question
    q2rank = int(input("How important is this for you from 1-4? "))
    while q2rank < 1 or q2rank > 4:
        print("Please enter a number between 1 and 4.")
        q2rank = int(input("How important is this for you from 1-4? "))

    score += q2rank
    print(f"Current score: {score}")

    # Store the user's responses with questions and their scores
    user_data = {
        "name": name,
        "answers": [
            {"question": "Are you female or male?", "answer": q1_answer},
            {"question": "Would you like your match to be female or male?", "answer": p2q1_answer},
            {"question": "Around what age are you?", "answer": q2_answer},
            {"question": "Around what age would you like your match to be?", "answer": p2q2_answer},
        ],
        "score": score
    }

    # Save the result
    results.append(user_data)
    save_results(results)

    print(f"\n{user_data['name']}, your total score is: {score}. Thank you for completing the quiz!")

def main():
    # Load previous results if any
    results = load_results()

    # Show statistics
    show_statistics(results)

    # Greet the user and start the quiz
    name = greet_user()

    # Run the quiz
    run_quiz(name, results)

if __name__ == "__main__":
    main()
