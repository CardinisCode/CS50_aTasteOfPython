
def main():
    x = int(input("X: "))
    y = int(input("Y: "))
    z = maximum(x, y)
    print("Maximum:", z)


def maximum(a, b):
    if a > b:
        return a
    else:
        return b


main()