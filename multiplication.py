# def main():
#     multiply(4, 3)
#     multiply(2, 7)


# def multiply(x, y): 
#     product = x * y
#     print(x, "*", y, "=", product)


# main()

# Lets simplify this using a loop:
def main():
    for i in range(10):
        multiply(2, i)


def multiply(x, y): 
    product = x * y
    print(x, "*", y, "=", product)


# Or simplify even further with 2 for loops:

def main():
    grand_total = 0
    for i in range(10):
        for j in range(10):
            grand_total += multiply(i, j)

    print("Our grand total is:", grand_total)


def multiply(x, y): 
    product = x * y
    print(x, "*", y, "=", product)
    return product


main()