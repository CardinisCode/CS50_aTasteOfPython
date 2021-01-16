# take 10 inputs from user (int numbers)
# Add the sum of all 10 numbers
# Print the result of this sum

total = 0
for i in range(10): 
    user_int = int(input("Enter a number: "))
    total += user_int
print("The sum total:", total)


