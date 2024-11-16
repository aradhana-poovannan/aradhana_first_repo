name=input ("What is your name? ") 
print ("Hello, " + name + "! I've got some questions for you to answer. Please select one of the given options for each question. Here they come...") 
score = 0 
  
q1 = input ("1. Are you a female or male? ").lower()
while q1 != "female" or "male": 
    if q1 == "female": 
        print ("Next...") 
        break 
    elif q1 == "male": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        q1 =input("1. Are you a female or male? ").lower()
p2q1 = input ("1. Would you like your match to be a female or male? ").lower()
while p2q1 != "female" or "male": 
    if p2q1 == "female": 
        print ("Next...") 
        break 
    elif p2q1 == "male": 
        print("Next...") 
        break 
    else:
         print("Please choose one of the given options") 
q1rank = int(input("How important is this for you from 1-4? ")) 
if q1rank == 1: 
     score =score + 1 
     print(score) 
elif q1rank == 2: 
     score =score + 2 
     print(score) 
elif q1rank == 3: 
     score =score + 3 
     print(score) 
else: 
     score =score + 4 
     print(score) 
print("Next question")
  
  
q2 = input ("2. Around what age are you?  a. 18-25, b. 26-32, c. 33-40, d. 41-46, or e. 47+ ? Choose a letter. ").lower() 
while q2 != "a" or "b" or "c" or "d" or "e" or "f": 
    if q2 == "a": 
        print ("Next...") 
        break
    elif q2 == "b": 
        print("Next...") 
        break 
    elif q2 == "c": 
        print("Next...") 
        break 
    elif q2 == "d": 
        print("Next...") 
        break 
    elif q2 == "e": 
        print("Next...") 
        break 
    elif q2 == "f": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options")
        q2=input("2. Around what age are you? a. 13-18, b. 19-25, c. 26-32, d. 33-40, e. 41-46, or f. 47+ ? Choose a letter. ").lower() 
p2q2 = input ("2. Around what age would you like your match to be?  a. 18-25, b. 26-32, c. 33-40, d. 41-46, or e. 47+ ? Choose a letter. ").lower() 
while p2q2 != "a" or "b" or "c" or "d" or "e" or "f": 
    if p2q2 == "a": 
        print ("Next...") 
        break
    elif p2q2 == "b": 
        print("Next...") 
        break 
    elif p2q2 == "c": 
        print("Next...") 
        break 
    elif p2q2 == "d": 
        print("Next...") 
        break 
    elif p2q2 == "e": 
        print("Next...") 
        break 
    elif p2q2 == "f": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        q2=input("2. Around what age are you? a. 13-18, b. 19-25, c. 26-32, d. 33-40, e. 41-46, or f. 47+ ? Choose a letter. ").lower() 
q2rank = int(input("How important is this for you from 1-4? ")) 
if q2rank == 1: 
     score =score + 1 
     print(score) 
elif q2rank == 2: 
     score =score + 2 
     print(score) 
elif q2rank == 3: 
     score =score + 3 
     print(score) 
else: 
     score =score + 4 
     print(score) 
print("Next question") 



q3 = input ("3. Do you want to have a long-term or short-term relationship? ").lower()  
while q3 != "long-term" or "short-term":  
    if q3 == "long-term":  
        print ("Next...")  
        break  
    elif q3 == "short-term":  
        print("Next...")  
        break  
    else:  
        print("Please choose one of the given options")  
        q3 =input("3. Do you want to have a long-term or short-term relationship? ").lower()  
q3rank = int(input("How important is this for you from 1-4? "))  
if q3rank == 1:  
     score =score + 1  
     print(score) 
elif q3rank == 2:  
     score =score + 2  
     print(score)
elif q3rank == 3:  
     score =score + 3  
     print(score) 
else:   
     score =score + 4  
     print(score)  
print("Next question")  

   

q4 = input ("4. Do you prefer movies, books or both? ").lower() 
while q4 != "movies" or "books" or "both": 
    if q4 == "movies": 
        print ("Next...") 
        break 
    elif q4 == "books": 
        print("Next...") 
        break
    elif q4 == "both": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        q4 =input("4. Do you prefer movies, books or both? ").lower()
q4 = input ("4. Would you like your match to prefer movies, books or both? ").lower()
while q4 != "movies" or "books" or "both": 
    if q4 == "movies": 
        print ("Next...") 
        break 
    elif q4 == "books": 
        print("Next...") 
        break
    elif q4 == "both": 
        print("Next...") 
        break 
    else:
         print("Please choose one of the given options") 
q4rank = int(input("How important is this for you from 1-4? ")) 
if q4rank == 1: 
     score =score + 1 
     print(score) 
elif q4rank == 2: 
     score =score + 2 
     print(score) 
elif q4rank == 3: 
     score =score + 3 
     print(score) 
else:  
     score =score + 4 
     print(score) 
print("Next question") 

  

q5 = input ("5. Are you an introvert, extrovert or ambivert? ").lower() 
while q5 != "introvert" or "extrovert" or "ambivert": 
    if q5 == "introvert": 
        print ("Next...") 
        break 
    elif q5 == "extrovert": 
        print("Next...") 
        break 
    elif q5 == "ambivert": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        q5 =input("5. Are you an introvert, extrovert or ambivert? ").lower()
q5 = input ("5. Would you like your match to be an introvert, extrovert or ambivert? ").lower() 
while q5 != "introvert" or "b" or "c": 
    if q5 == "introvert": 
        print ("Next...") 
        breakq5 = input ("5. Would you like your match to be an introvert, extrovert or ambivert? ").lower() 
while q5 != "introvert" or "b" or "c": 
    if q5 == "introvert": 
        print ("Next...") 
        break
    elif q5 == "extrovert": 
        print("Next...") 
        break 
    elif q5 == "ambivert": 
        print("Next...") 
        break  
    else: 
        print("Please choose one of the given options") 
q5rank = int(input("How important is this for you from 1-4? ")) 
if q5rank == 1: 
     score =score + 1 
     print(score) 
elif q5rank == 2: 
     score =score + 2 
     print(score) 
elif q5rank == 3: 
     score =score + 3
while q5 != "introvert" or "b" or "c": 
    if q5 == "introvert": 
        print ("Next...") 
        break
    elif q5 == "extrovert": 
        print("Next...") 
        break 
    elif q5 == "ambivert": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
     print(score) 
else:  
     score =score + 4 
     print(score) 
print("Next question")

  

q6 = input ("6. Do you like to travel, yes or no? ").lower() 
while q6 != "yes" or "no": 
    if q6 == "yes": 
        print ("Next...") 
        break
    elif q6 == "no": 
        print("Next...") 
        break 
    elif q6 == "no":
    q5 = input ("5. Would you like your match to travel, yes or no? ").lower() 
while q6 != "yes" or "no": 
    if q6 == "yes": 
        print ("Next...") 
        break
    elif q6 == "no": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        q6 =input("6. Do you like to travel, yes or no? ").lower() 
q6rank = int(input("How important is this for you from 1-4? ")) 
if q6rank == 1: 
     score =score + 1 
     print(score) 
elif q6rank == 2: 
     score =score + 2 
     print(score) 
elif q6rank == 3: 
     score =score + 3 
     print(score) 
else:  
     score =score + 4 
     print(score) 
print("Next question") 

  

q7 = input ("7. Are you left-brained, right-brained, or middle-brained? ").lower() 
while q7 != "left-brained" or "right-brained" or "middle-brained": 
    if q7 == "left-brained": 
        print ("Next...") 
        break 
    elif q7 == "right-brained": 
        print("Next...") 
        break 
    elif q7 == "middle-brained": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        q7 =input("7. Are you left-brained, right-brained, or middle-brained? ").lower() 
q7rank = int(input("How important is this for you from 1-4? ")) 
if q7rank == 1: 
     score =score + 1 
     print(score) 
elif q7rank == 2: 
     score =score + 2 
     print(score) 
elif q7rank == 3: 
     score =score + 3 
     print(score) 
else:  
     score =score + 4 
     print(score) 
print("Next question") 

 

q8 = input ("8. Do you want to be in a relationship with a person who is caring, funny, clever, or attractive? ").lower() 
while q8 != "caring" or "funny" or "smart" or "attractive": 
    if q8 == "caring": 
        print ("Next...") 
        break 
    elif q8 == "funny": 
        print("Next...") 
        break 
    elif q8 == "smart": 
        print("Next...") 
        break 
    elif q8 == "attractive": 
        print("Next...") 
        break 

    else: 
        print("Please choose one of the given options") 
        q8 =input("8. Do you want to be in a relationship with a person who is caring, funny, smart, or attractive? ").lower()
q8rank = int(input("How important is this for you from 1-4? ")) 
if q8rank == 1: 
     score =score + 1 
     print(score) 
elif q8rank == 2:
     score =score + 2 
     print(score) 
elif q8rank == 3: 
     score =score + 3 
     print(score) 
else:  
     score =score + 4 
     print(score) 
print("Next question") 



q9 = input ("9. If there was one place you would go whenever you're feeling down, where would that be: home, friend’s house or somewhere by yourself? ").lower() 
while q9 != "home" or "friend's house" or "somewhere by myself": 
    if q9 == "home": 
        print ("Next...") 
        break 
    elif q9 == "friend’s house": 
        print("Next...") 
        break 
    elif q9 == "somewhere by myself": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        q9 =input("9. If there was one place you would go whenever you're feeling down, where would that be: home, friend’s house or somewhere by yourself? ").lower()
q9rank = int(input("How important is this for you from 1-4? ")) 
if q9rank == 1: 
     score =score + 1 
     print(score) 
elif q9rank == 2:
     score =score + 2 
     print(score) 
elif q9rank == 3: 
     score =score + 3 
     print(score) 
else:  
     score =score + 4 
     print(score) 
print("Next question")



q10 = input ("10. Who, in your life, is/are important to you: family, friends or partner?​ ").lower() 
while q10 != "family" or "friends" or "partner": 
    if q10 == "family": 
        print ("Next...") 
        break 
    elif q10 == "friends": 
        print("Next...") 
        break 
    elif q10 == "partner": 
        print("Next...") 
        break 
    else: 
        print("Please choose one of the given options") 
        q10 =input("10. Who, in your life, is/are important to you: family, friends or partner?​ ").lower()
q10rank = int(input("How important is this for you from 1-4? ")) 
if q10rank == 1: 
     score =score + 1 
     print(score) 
elif q10rank == 2:
     score =score + 2 
     print(score) 
elif q10rank == 3: 
     score =score + 3 
     print(score) 
else:  
     score =score + 4 
     print(score) 
print("You have succesfully finished all the questions. Thank you for completing the quiz"  + name + "!") 

