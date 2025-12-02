def ask_text(message):
    text = input(message).strip()  # Read user input and remove leading/trailing spaces
    while text.isspace() or len(text) == 0:  # Check if the input is empty or only whitespace
        print("Error: please enter a valid text.")
        text = input(message).strip()  # Ask for input again and strip spaces
    return text

def ask_number(message, min_val=None, max_val=None):
    # Internal function: checks if a string represents a valid integer
    def is_int(s):
        if s == "":
            return False

        # If the number is negative
        if s[0] == "-":
            if len(s) == 1:
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