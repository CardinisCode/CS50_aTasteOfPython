

# We take the scores from each player and then print "#" to match each score's value
# def main():
    score_1 = int(input("Score 1: "))
    score_2 = int(input("Score 2: "))
    score_3 = int(input("Score 3: "))

    print_scores(score_1)
    print_scores(score_2)
    print_scores(score_3)

# main()


def print_scores(n):
    for i in range(n):
        print("#", end="")
    print()
