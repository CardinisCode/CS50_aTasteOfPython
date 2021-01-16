import random

def main():
    number = random.randint(5, 15)
    count_down(number)
    print("Happy new year!")

def count_down(n):
    for i in range(n):
        print(n - i)

main()