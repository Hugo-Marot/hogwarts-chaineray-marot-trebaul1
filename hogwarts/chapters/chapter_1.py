from hogwarts.universe.character import *
from hogwarts.utils.input_utils import *
import os

# Path to the project root (hogwarts/)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # go up from chapters/ to hogwarts/

INVENTORY_PATH = os.path.join(BASE_DIR, "data", "inventory.json")


def introduction():
    """Display the introduction of Chapter 1 and wait for the player to continue."""

    print("========================================")
    print("Chapter 1 – Arrival in the magical world")
    print("========================================\n")

    print("Welcome to the Wizarding World!")
    print("You are about to begin an extraordinary adventure at Hogwarts School of Witchcraft and Wizardry.")
    print("Very soon, your life will change forever: mysterious letters, strange encounters, and a destiny")
    print("tightly bound to magic await you...\n")

    print("Get ready to create your character, receive your Hogwarts letter,")
    print("meet Hagrid, and buy your first supplies in Diagon Alley.\n")

    input("Press Enter to begin your adventure... ")


def create_character():
    """Create the player's character by asking for personal info and attributes."""

    print("Let's create your character!")

    last_name = input("Enter your character's last name: ")
    first_name = input("Enter your character's first name: ")

    print("Choose your attributes:")

    # Helper function to ensure value is between 1 and 10
    def ask_attribute(prompt):
        while True:
            try:
                value = int(input(prompt))
                if 1 <= value <= 10:
                    return value
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid integer.")

    courage = ask_attribute("Courage level (1-10): ")
    intelligence = ask_attribute("Intelligence level (1-10): ")
    loyalty = ask_attribute("Loyalty level (1-10): ")
    ambition = ask_attribute("Ambition level (1-10): ")

    # Create the attributes dictionary
    attributes = {
        "Courage": courage,
        "Intelligence": intelligence,
        "Loyalty": loyalty,
        "Ambition": ambition
    }

    # Build the full character with your previously coded function
    character = init_character(last_name, first_name, attributes)

    # Show the result
    print()
    display_character(character)

    return character

def receive_letter():
    """Simulate receiving the Hogwarts acceptance letter."""

    print("\nAn owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    print("“Dear Student,")
    print("We are pleased to inform you that you have been accepted to Hogwarts")
    print("School of Witchcraft and Wizardry!”\n")

    print("Do you accept this invitation and go to Hogwarts?")
    print("1. Yes, of course!")
    print("2. No, I'd rather stay with Uncle Vernon...")

    # Validate choice
    while True:
        choice = input("Your choice: ")
        if choice in ["1", "2"]:
            break
        print("Please enter 1 or 2.")

    if choice == "2":
        # Player declines → immediate game over
        print("\nYou tear up the letter, and Uncle Vernon cheers:")
        print("“EXCELLENT! Finally, someone NORMAL in this house!”")
        print("The magical world will never know you existed... Game over.")
        exit(0)   # stop the game cleanly

    # Player accepts → continue the adventure
    print("\nWonderful! You accept the invitation and your magical journey begins...\n")

def meet_hagrid(character):
    """Introduce Hagrid and ask the player if they want to follow him."""

    # Use the character's first name for immersion
    first_name = character["First Name"]

    print(f"\nHagrid: 'Hello {first_name}! I’m here to help you with your shopping on Diagon Alley.'")
    print("Do you want to follow Hagrid?")
    print("1. Yes")
    print("2. No")

    # Input validation
    while True:
        choice = input("Your choice: ")
        if choice in ["1", "2"]:
            break
        print("Please enter 1 or 2.")

    # Handle player choice
    if choice == "1":
        print("\nGreat! You follow Hagrid toward Diagon Alley.")
    else:
        print("\nHagrid gently insists and takes you along anyway!")

    print("You are now heading to Diagon Alley...\n")

def buy_supplies(character):
    """Let the player buy the required school supplies in Diagon Alley."""

    # Load catalog from JSON file (dict: "1": ["Magic Wand", 35], ...)
    catalog = load_file(INVENTORY_PATH)

    if catalog is None:
        print("Error: could not load inventory file.")
        exit(1)


    # Required items
    required_items = {"Magic Wand", "Wizard Robe", "Potions Book"}
    remaining_required = set(required_items)

    print("Welcome to Diagon Alley!")
    print("Catalog of available items:")

    # Display catalog sorted by numeric key
    for key in sorted(catalog.keys(), key=int):
        name, price = catalog[key]
        required_label = " (required)" if name in required_items else ""
        print(f"{key}. {name} - {price} Galleons{required_label}")

    # --- SHOPPING LOOP: must buy all required items ---
    while remaining_required:
        print(f"\nYou have {character['Money']} Galleons.")
        print(
            "Remaining required items: "
            + ", ".join(sorted(remaining_required))
        )

        choice = input("Enter the number of the item to buy: ")

        # validate choice
        if choice not in catalog:
            print("Please choose a valid item number.")
            continue

        name, price = catalog[choice]

        # Check money
        if price > character["Money"]:
            print(
                f"\nYou don't have enough Galleons to buy {name} "
                f"({price} Galleons)."
            )
            print(
                "Without the required equipment, you cannot go to Hogwarts..."
            )
            print("Game over.")
            exit(0)

        # Perform purchase
        modify_money(character, -price)
        add_item(character, "Inventory", name)
        print(f"\nYou bought: {name} (-{price} Galleons).")
        print(f"You have {character['Money']} Galleons.")

        # Update required items
        if name in remaining_required:
            remaining_required.remove(name)

        if not remaining_required:
            print("All required items have been purchased!")

    # --- PET SELECTION ---

    print("\nIt's time to choose your Hogwarts pet!")
    print(f"You have {character['Money']} Galleons.")

    pets = [
        ("Owl", 20),
        ("Cat", 15),
        ("Rat", 10),
        ("Toad", 5),
    ]

    print("Available pets:")
    for i, (pet_name, pet_price) in enumerate(pets, start=1):
        print(f"{i}. {pet_name} - {pet_price} Galleons")

    while True:
        print("Which pet do you want?")
        for i, (pet_name, _) in enumerate(pets, start=1):
            print(f"{i}. {pet_name}")
        choice = input("Your choice: ")

        try:
            choice_int = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not (1 <= choice_int <= len(pets)):
            print("Please choose a valid pet number.")
            continue

        pet_name, pet_price = pets[choice_int - 1]

        if pet_price > character["Money"]:
            print(
                f"\nYou don't have enough Galleons to buy {pet_name} "
                f"({pet_price} Galleons)."
            )
            print("Without a familiar, your magical journey cannot begin...")
            print("Game over.")
            exit(0)

        modify_money(character, -pet_price)
        add_item(character, "Inventory", pet_name)
        print(f"\nYou chose: {pet_name} (-{pet_price} Galleons).")
        break

    print(
        "\nAll required items have been successfully purchased! "
        "Here is your final inventory:\n"
    )
    display_character(character)

def start_chapter_1():
    """Run all events of Chapter 1 and return the created character."""

    # 1. Display introduction
    introduction()

    # 2. Character creation
    character = create_character()

    # 3. Receiving the letter
    receive_letter()

    # 4. Meeting Hagrid
    meet_hagrid(character)

    # 5. Purchasing supplies on Diagon Alley
    buy_supplies(character)

    # 6. End of chapter message
    print("\nEnd of Chapter 1! Your adventure begins at Hogwarts...\n")

    # 7. Return the character dictionary
    return character

start_chapter_1()