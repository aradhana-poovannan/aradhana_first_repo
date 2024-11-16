ticketPrice = 15
discount = 5
total = 0
num_of_people = 0

print("Enter the number of poeple in your group: ")
num_of_people=int(input())

if num_of_people < 6:
    total = num_of_people * ticketPrice
else:
    total = (num_of_people * ticketPrice) - discount

print("The total number of people in your group: ",num_of_people)
print("The total amount is = £",total)

