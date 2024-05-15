# Command-line Password Generator Program

import string
import random

def generate_password(length):
    # Following defines character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # This will combine character sets based on user preferences
    character_set = ""
    while True:
        print("Choose character set for password:")
        print("1. Lowercase letters")
        print("2. Uppercase letters")
        print("3. Digits")
        print("4. Symbols")
        choice = input("Enter your choice (comma-separated, e.g., 1,2,3): ")

        if not choice:
            print("Please select at least one character set.")
            continue

        selected_sets = choice.split(",")
        for s in selected_sets:
            if s == "1":
                character_set += lowercase_letters
            elif s == "2":
                character_set += uppercase_letters
            elif s == "3":
                character_set += digits
            elif s == "4":
                character_set += symbols
            else:
                print(f"Invalid choice: {s}")

        if character_set:
            break

    # Finally generates the password
    password = "".join(random.choice(character_set) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Enter password length: "))
        generated_password = generate_password(password_length)
        print(f"Generated password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")