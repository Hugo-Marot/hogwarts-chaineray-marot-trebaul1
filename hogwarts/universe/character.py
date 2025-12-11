



def init_character(last_name, first_name, attributes):
    """Initialize and return a new character dictionary."""

    character = {
        "Last Name": last_name,
        "First Name": first_name,
        "Money": 100,  # Starting amount of galleons
        "Inventory": [],  # Empty inventory
        "Spells": [],  # No spells at the beginning
        "Attributes": attributes  # The dictionary passed in parameter
    }

    return character

def display_character(character):
    """Display all information about the character."""

    print("Character profile:")

    for key, value in character.items():

        # --- Case 1: dictionary (Attributes) ---
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"- {sub_key}: {sub_value}")

        # --- Case 2: list (Inventory, Spells…) ---
        elif isinstance(value, list):
            print(f"{key}:")
            if len(value) == 0:
                continue  # empty → just print the title
            else:
                # Join list elements as strings
                print(", ".join(str(item) for item in value))

        # --- Case 3: simple value (string, int…) ---
        else:
            print(f"{key}: {value}")

def modify_money(character, amount):
    """Add (or remove) money from the character."""
    character["Money"] += amount

def add_item(character, key, item):
    """Add an item or spell to the specified list (Inventory or Spells)."""

    # Ensure the key is valid
    if key not in ["Inventory", "Spells"]:
        print(f"Erreur : '{key}' is not a valid field (must be 'Inventory' or 'Spells').")
        return

    character[key].append(item)
