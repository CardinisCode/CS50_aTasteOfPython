import random

# answer = random.randint(1, 10)
# correct_guess = False

# for i in range(3):
#     guess = int(input("Choose a number between 1 & 10: "))
#     if guess == answer: 
#         print("Well done! That's the right answer :D")
#         correct_guess = True
#         break
#     elif guess < 1 or guess > 10: 
#         print("Please provide a guess between 1 & 10.")

#     else:
#         if guess > answer:
#             print("try <-")
#         else:
#             print("try: ->")

# if correct_guess == False:
#     print("Sorry you weren't successful. Please play again! :)")    


# Alt solution:

def main():
    number = random.randint(1, 10)

    for i in range(3):
        guess = int(input("Guess: "))

        if guess > number: 
            print("The number is too big!")

        elif guess < number: 
            print("The number is too small!")

        else: 
            print("Correct!")
            return 

main()