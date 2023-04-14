def check_password_strength(password):
    conditions = {}

    if len(password) > 8:
        conditions["length"] = True
    else:
        conditions["length"] = False

    contains_digit = False
    for i in password:
        if i.isdigit():
            contains_digit = True
    conditions["contains_digit"] = contains_digit

    contains_uppercase = False
    for i in password:
        if i.isupper():
            contains_uppercase = True
    conditions["contains_uppercase"] = contains_uppercase

    # print(conditions)

    if all(conditions.values()):
        print("Strong password")
    else:
        print("Weak password")


while True:
    print("Strong Password Checker")

    check_password_strength(input("Please enter your password: "))

    user_input = input("Would you like to exit? (y/n): ")
    if user_input.lower() == "y":
        break
    continue

print("Bye ^^")
