import json


def ask_text(message):
    text = input(message).strip()

    while text == "":
        print("Please enter some text.")
        text = input(message).strip()

    return text


def ask_number(message, min_val=None, max_val=None):
    while True:
        user_input = input(message).strip()

        if user_input.startswith("-"):
            is_number = user_input[1:].isdigit()
        else:
            is_number = user_input.isdigit()

        if not is_number:
            print("Please enter a valid integer.")
            continue

        number = int(user_input)

        if min_val is not None and number < min_val:
            print(f"Please enter a number >= {min_val}.")
            continue

        if max_val is not None and number > max_val:
            print(f"Please enter a number <= {max_val}.")
            continue

        return number


def ask_choice(message, options):
    print(message)

    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    choice = ask_number("Your choice: ", 1, len(options))
    return options[choice - 1]


def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
