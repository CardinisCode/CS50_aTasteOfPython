# Solution #1: 
# for i in range(10, -1, -1): 
#     print(i)
# print("Happy new year!")

# Solution #2: 
# for i in range(10):
#     print(10 - i)
# print("Happy new year!")

# Lets create a function to call on when we want to count down
# def count_down():
#     for i in range(10):
#         print(10 - i)
#     print("Happy new year!")
# count_down()

# # Lets do this again using a Main function plus this count_down function
# def main():
#     count_down()
#     print("Happy new year!")

# def count_down():
#     for i in range(10):
#         print(10 - i)

# main()

# Let's do this again but adjust our countdown
def main():
    count_down(5)
    print("Happy new year!")

def count_down(n):
    for i in range(n):
        print(n - i)

main()


