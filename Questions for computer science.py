# Prompt for the user's name and greet them
name = input("What is your name? ")
print(f"Hello, {name}! I've got some questions for you to answer. Please select one of the given options for each question. Here they come...")

score = 0  # Initialize the score variable

# Question 1: Gender
q1 = input("1. Are you female or male? ").lower()
while q1 != "female" and q1 != "male":
    print("Please choose one of the given options: female or male.")
    q1 = input("1. Are you female or male? ").lower()
print("Next...")

# Question 2: Preferred gender for match
p2q1 = input("1. Would you like your match to be female or male? ").lower()
while p2q1 != "female" and p2q1 != "male":
    print("Please choose one of the given options: female or male.")
    p2q1 = input("1. Would you like your match to be female or male? ").lower()
print("Next...")

# Rank importance of the gender question
q1rank = int(input("How important is this for you from 1-4? "))
while q1rank < 1 or q1rank > 4:
    print("Please enter a number between 1 and 4.")
    q1rank = int(input("How important is this for you from 1-4? "))

# Update score based on ranking
score += q1rank
print(f"Current score: {score}")
print("Next question...")

# Question 3: Age range
q2 = input("2. Around what age are you? a. 18-25, b. 26-32, c. 33-40, d. 41-46, or e. 47+ ? Choose a letter: ").lower()
while q2 not in ['a', 'b', 'c', 'd', 'e']:
    print("Please choose one of the given options.")
    q2 = input("2. Around what age are you? a. 18-25, b. 26-32, c. 33-40, d. 41-46, or e. 47+ ? Choose a letter: ").lower()
print("Next...")

# Preferred age for match
p2q2 = input("2. Around what age would you like your match to be? a. 18-25, b. 26-32, c. 33-40, d. 41-46, or e. 47+ ? Choose a letter: ").lower()
while p2q2 not in ['a', 'b', 'c', 'd', 'e']:
    print("Please choose one of the given options.")
    p2q2 = input("2. Around what age would you like your match to be? a. 18-25, b. 26-32, c. 33-40, d. 41-46, or e. 47+ ? Choose a letter: ").lower()
print("Next...")

# Rank importance of the age question
q2rank = int(input("How important is this for you from 1-4? "))
while q2rank < 1 or q2rank > 4:
    print("Please enter a number between 1 and 4.")
    q2rank = int(input("How important is this for you from 1-4? "))

score += q2rank
print(f"Current score: {score}")
print("Next question...")

# Question 4: Relationship type
q3 = input("3. Do you want to have a long-term or short-term relationship? ").lower()
while q3 != "long-term" and q3 != "short-term":
    print("Please choose one of the given options: long-term or short-term.")
    q3 = input("3. Do you want to have a long-term or short-term relationship? ").lower()
print("Next...")

# Rank importance of the relationship type question
q3rank = int(input("How important is this for you from 1-4? "))
while q3rank < 1 or q3rank > 4:
    print("Please enter a number between 1 and 4.")
    q3rank = int(input("How important is this for you from 1-4? "))

score += q3rank
print(f"Current score: {score}")
print("Next question...")

# Question 5: Preferences for movies/books
q4 = input("4. Do you prefer movies, books, or both? ").lower()
while q4 not in ['movies', 'books', 'both']:
    print("Please choose one of the given options: movies, books, or both.")
    q4 = input("4. Do you prefer movies, books, or both? ").lower()
print("Next...")

# Preferred preference for match
p2q4 = input("4. Would you like your match to prefer movies, books, or both? ").lower()
while p2q4 not in ['movies', 'books', 'both']:
    print("Please choose one of the given options: movies, books, or both.")
    p2q4 = input("4. Would you like your match to prefer movies, books, or both? ").lower()
print("Next...")

# Rank importance of the preference question
q4rank = int(input("How important is this for you from 1-4? "))
while q4rank < 1 or q4rank > 4:
    print("Please enter a number between 1 and 4.")
    q4rank = int(input("How important is this for you from 1-4? "))

score += q4rank
print(f"Current score: {score}")
print("Next question...")

# Question 6: Introvert/Extrovert/Ambivert
q5 = input("5. Are you an introvert, extrovert, or ambivert? ").lower()
while q5 not in ['introvert', 'extrovert', 'ambivert']:
    print("Please choose one of the given options: introvert, extrovert, or ambivert.")
    q5 = input("5. Are you an introvert, extrovert, or ambivert? ").lower()
print("Next...")

# Preferred personality for match
p2q5 = input("5. Would you like your match to be an introvert, extrovert, or ambivert? ").lower()
while p2q5 not in ['introvert', 'extrovert', 'ambivert']:
    print("Please choose one of the given options: introvert, extrovert, or ambivert.")
    p2q5 = input("5. Would you like your match to be an introvert, extrovert, or ambivert? ").lower()
print("Next...")

# Rank importance of the personality question
q5rank = int(input("How important is this for you from 1-4? "))
while q5rank < 1 or q5rank > 4:
    print("Please enter a number between 1 and 4.")
    q5rank = int(input("How important is this for you from 1-4? "))

score += q5rank
print(f"Current score: {score}")
print("Next question...")

# Question 7: Travel preference
q6 = input("6. Do you like to travel, yes or no? ").lower()
while q6 != "yes" and q6 != "no":
    print("Please choose one of the given options: yes or no.")
    q6 = input("6. Do you like to travel, yes or no? ").lower()
print("Next...")

# Rank importance of the travel question
q6rank = int(input("How important is this for you from 1-4? "))
while q6rank < 1 or q6rank > 4:
    print("Please enter a number between 1 and 4.")
    q6rank = int(input("How important is this for you from 1-4? "))

score += q6rank
print(f"Current score: {score}")
print("Next question...")

# Question 8: Creativity (Left-brained, right-brained, or middle-brained)
q7 = input("7. Are you left-brained, right-brained, or middle-brained? ").lower()
while q7 not in ['left-brained', 'right-brained', 'middle-brained']:
    print("Please choose one of the given options: left-brained, right-brained, or middle-brained.")
    q7 = input("7. Are you left-brained, right-brained, or middle-brained? ").lower()
print("Next...")

# Rank importance of the creativity question
q7rank = int(input("How important is this for you from 1-4? "))
while q7rank < 1 or q7rank > 4:
    print("Please enter a number between 1 and 4.")
    q7rank = int(input("How important is this for you from 1-4? "))

score += q7rank
print(f"Current score: {score}")
print("Next question...")

# Question 9: Relationship traits (Caring, funny, smart, or attractive)
q8 = input("8. Do you want to be in a relationship with a person who is caring, funny, smart, or attractive? ").lower()
while q8 not in ['caring', 'funny', 'smart', 'attractive']:
    print("Please choose one of the given options: caring, funny, smart, or attractive.")
    q8 = input("8. Do you want to be in a relationship with a person who is caring, funny, smart, or attractive? ").lower()
print("Next...")

# Rank importance of the relationship trait question
q8rank = int(input("How important is this for you from 1-4? "))
while q8rank < 1 or q8rank > 4:
    print("Please enter a number between 1 and 4.")
    q8rank = int(input("How important is this for you from 1-4? "))

score += q8rank
print(f"Current score: {score}")
print("Next question...")

# Question 10: Support system (Family, friends, or partner)
q9 = input("9. Who, in your life, is/are important to you: family, friends, or partner? ").lower()
while q9 not in ['family', 'friends', 'partner']:
    print("Please choose one of the given options: family, friends, or partner.")
    q9 = input("9. Who, in your life, is/are important to you: family, friends, or partner? ").lower()
print("Next...")

# Rank importance of the support system question
q9rank = int(input("How important is this for you from 1-4? "))
while q9rank < 1 or q9rank > 4:
    print("Please enter a number between 1 and 4.")
    q9rank = int(input("How important is this for you from 1-4? "))

score += q9rank
print(f"Current score: {score}")

# Final message
print(f"You have successfully finished all the questions. Thank you for completing the quiz, {name}!")
