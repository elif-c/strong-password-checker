while True:
    print("Strong Password Checker")
    password = input("Please enter your password: ")
    conditions = []

    if len(password) > 8:
        conditions.append(True)
    else:
        conditions.append(False)

    contains_digit = False
    for i in password:
        if i.isdigit():
            contains_digit = True
    conditions.append(contains_digit)

    contains_uppercase = False
    for i in password:
        if i.isupper():
            contains_uppercase = True
    conditions.append(contains_uppercase)

    if all(conditions):
        print("Strong password")
    else:
        print("Weak password")
    user_input = input("Would you like to exit? (y/n): ")
    if user_input.lower() == "y":
        break
    continue
print("Bye ^^")