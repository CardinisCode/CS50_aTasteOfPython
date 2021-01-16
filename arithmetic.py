# "x = input("x: ")
# y = input("Y: ")
# print(x + y)
# # Ouch it's adding them together as strings! aka 4 + 2 = 42

# a = int(input("a: "))
# b = int(input("b: "))
# print(a + b)
# # Alas! I get the expected output! :) "


# c = input("c:")
# d = input("D:")
# print(a * b)
# # Intersting if I multiply characters, I get an integer value. 

# x = int(input("Enter a number above 0: "))
# if x > 0: 
#     print(x * 2)

# else: 
#     print("Error: You didnt give us a number above 0.")

# It fails and returns a ValueError if it gets an string. 

# An over-engineered solution LOL
try: 
    x = int(input("Enter a value above 0: "))
    if x > 0:
        print(x * 2)
    else:
        print("You didn't provide a number above 0!")
except ValueError:
    print("You didn't provide a numeric number!")


