# Challenge: Take a number (n) from the user and build a pyramid of size n

height = int(input("Height: "))
spaces = " "
hashes = "#"


for i in range(1, height + 1):
    left_side_spaces = (height - i)
    left_side_hashes = i
    left_side = (left_side_spaces * spaces) + (left_side_hashes * hashes)
    right_side = "  " + (left_side_hashes * hashes)
    print(left_side + right_side)

