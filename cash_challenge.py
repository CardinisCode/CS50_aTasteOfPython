# Challenge #2: Write a program that asks the user to type in an ammount of money and print
# the minimum number of US coins required to make change. Assume you can use:
# - quarters (25c), 
#-  dimes (10c)
# - nickels (5c)
# - pennies (1c)


def check_cash_for_strings(cash):
    for i in range(len(cash)):
        current_char = cash[i]
        if ord(current_char) > 57 or ord(current_char) < 48: 
            return True
    
    return False



def verify_change_is_valid(cash):
    if cash == '':
        return "No value provided, please try again."
    
    cash_is_string = check_cash_for_strings(str(cash))
    if cash_is_string == True:
        return "Please provide integers or floats only"

    if int(cash) <= 0:
        return "Please provide a value higher than 0."

    return True


def check_cash_for_minimum_change(cash):
    if cash == 5:
        return 1

    return cash


def main(cash):
    message = "Testing..."
    cash_is_valid = verify_change_is_valid(cash)
    print(f"Your cash ${cash} is valid:", cash_is_valid)

    cash_in_cents = int(cash * 100)

    minimum_change =check_cash_for_minimum_change(cash_in_cents)
    print("Minimum changed needed:", minimum_change)

    return message




# users_cash = int(input("Give Cash Value: "))
print(main(1))
