# Define the price of one ticket and the discount for large groups
ticketPrice = 15  # Cost per ticket in GBP
discount = 5      # Discount given for groups of 6 or more people

# Initialize variables to store total cost and number of people
total = 0          # Variable to store the total cost
num_of_people = 0  # Variable to store the number of people in the group

# Prompt the user to enter the number of people in the group
print("Enter the number of people in your group: ")
num_of_people = int(input())  # Read input from the user and convert it to an integer

# Check if the group is small (fewer than 6 people)
if num_of_people < 6:
    # If the group has fewer than 6 people, no discount is applied
    total = num_of_people * ticketPrice
else:
    # If the group has 6 or more people, apply the discount
    total = (num_of_people * ticketPrice) - discount

# Print the results
print("The total number of people in your group: ", num_of_people)  # Display number of people
print("The total amount is = £", total)  # Display the total amount after any discount
