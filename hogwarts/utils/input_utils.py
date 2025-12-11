def ask_text(message):
    text = input(message).strip()
    while text.isspace() or len(text) == 0:
        print("Error: please enter a valid text.")
        text = input(message).strip()
    return text


def ask_number(message, min_val=None, max_val=None):
    # Internal function: checks if a string represents a valid integer
    def is_int(s):
        if s == "":
            return False

        # If the number is negative
        if s[0] == "-":
            if len(s) == 1:  # just "-" → not a number
                return False
            s = s[1:]  # we check the remaining characters

        # Check that each character is a digit
        for c in s:
            if c < '0' or c > '9':
                return False
        return True

    while True:
        user_input = input(message).strip()

        # Check that it is a valid integer
        if not is_int(user_input):
            print("Please enter a valid integer.")
            continue

        # Manual conversion from string to int
        negative = False
        if user_input[0] == "-":
            negative = True
            user_input = user_input[1:]

        number = 0
        for c in user_input:
            digit = ord(c) - ord('0')  # ASCII conversion → digit
            number = number * 10 + digit  # rebuild the number

        if negative:
            number = -number

        # Check min/max bounds
        if min_val is not None and number < min_val:
            print(f"Please enter a number between {min_val} and {max_val}.")
            continue

        if max_val is not None and number > max_val:
            print(f"Please enter a number between {min_val} and {max_val}.")
            continue

        return number


def ask_choice(message, options):
    # Display the message
    print(message)

    # Display the numbered list of options
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    # Ask the user for a valid choice number
    choice_index = ask_number("Your choice: ", 1, len(options))

    # Return the corresponding option (convert 1-based index to 0-based)
    return options[choice_index - 1]

import json

def load_file(file_path):
    #Load and return data from a JSON file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        return None
    except json.JSONDecodeError:
        print(f"Erreur : Le fichier {file_path} n'est pas un JSON valide.")
        return None


#ask_text(message)
#ask_number(message,min_val,max_val)
#ask_choice(message,["yes", "no"])