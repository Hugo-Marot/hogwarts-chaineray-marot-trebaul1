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

    for key in character:
        value = character[key]

        if type(value) == dict:
            print(f"{key}:")
            for sub_key in value:
                print(f"- {sub_key}: {value[sub_key]}")

        elif type(value) == list:
            print(f"{key}:")
            if len(value) == 0:
                print("None")
            else:
                print(", ".join(value))

        else:
            print(f"{key}: {value}")


def modify_money(character, amount):
    character["Money"] = character["Money"] + amount


def add_item(character, key, item):
    if key == "Inventory" or key == "Spells":
        character[key].append(item)
    else:
        print("Error: invalid key")
