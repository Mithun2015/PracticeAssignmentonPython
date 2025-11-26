def check_password_strength(password):
    if len(password) < 8:
        return False  # Length rule failed

    lowercase_found = False
    uppercase_found = False
    digit_found = False
    special_found = False

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/|\\"

    # Check each character
    for char in password:
        if 'a' <= char <= 'z':
            lowercase_found = True
        elif 'A' <= char <= 'Z':
            uppercase_found = True
        elif char.isdigit():  # digits check
            digit_found = True
        elif char in special_characters:
            special_found = True

    # Final decision
    if lowercase_found and uppercase_found and digit_found and special_found:
        return True
    else:
        return False


# Taking input from the user
password = input("Enter your password: ")

# Calling the function and giving feedback
if check_password_strength(password):
    print("Password is STRONG ")
else:
    print("Password is WEAK ")
    print("Make sure your password has:")
    print("- At least 8 characters")
    print("- Uppercase + lowercase letters")
    print("- At least one number")
    print("- At least one special symbol (!@#$%, etc.)")
