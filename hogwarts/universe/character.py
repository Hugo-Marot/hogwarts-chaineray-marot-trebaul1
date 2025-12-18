def init_character(last_name, first_name, attributes):
    character = {
        "Last Name": last_name,
        "First Name": first_name,
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": attributes
    }

    return character

def display_character(character):

    print("Character profile:")

    for key, value in character.items():

        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"- {sub_key}: {sub_value}")

        elif isinstance(value, list):
            print(f"{key}:")
            if len(value) == 0:
                continue
            else:
                print(", ".join(str(item) for item in value))

        else:
            print(f"{key}: {value}")

def modify_money(character, amount):
    character["Money"] += amount

def add_item(character, key, item):

    if key not in ["Inventory", "Spells"]:
        print(f"Erreur : '{key}' is not a valid field (must be 'Inventory' or 'Spells').")
        return

    character[key].append(item)
