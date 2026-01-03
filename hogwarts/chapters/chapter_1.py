from hogwarts.utils.input_utils import ask_text, ask_number, ask_choice, load_file
from hogwarts.universe.character import init_character, display_character, modify_money, add_item


def introduction():
    print("========================================")
    print("Chapter 1 – Arrival in the magical world")
    print("========================================\n")

    print("Welcome to the Wizarding World!")
    print("You are about to begin an extraordinary adventure at Hogwarts.\n")
    input("Press Enter to begin your adventure... ")


def create_character():
    print("Let's create your character!")

    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter your character's first name: ")

    print("Choose your attributes (1 to 10):")
    courage = ask_number("Courage level (1-10): ", 1, 10)
    intelligence = ask_number("Intelligence level (1-10): ", 1, 10)
    loyalty = ask_number("Loyalty level (1-10): ", 1, 10)
    ambition = ask_number("Ambition level (1-10): ", 1, 10)

    attributes = {
        "courage": courage,
        "intelligence": intelligence,
        "loyalty": loyalty,
        "ambition": ambition
    }

    character = init_character(last_name, first_name, attributes)

    print()
    display_character(character)
    return character


def receive_letter():
    print("\nAn owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    print("“Dear Student,")
    print("We are pleased to inform you that you have been accepted to Hogwarts")
    print("School of Witchcraft and Wizardry!”\n")

    choice = ask_choice(
        "Do you accept this invitation and go to Hogwarts?",
        ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."]
    )

    if choice.startswith("No"):
        print("\nYou tear up the letter, and Uncle Vernon cheers:")
        print("“EXCELLENT! Finally, someone NORMAL in this house!”")
        print("The magical world will never know you existed... Game over.")
        exit(0)

    print("\nWonderful! You accept the invitation and your magical journey begins...\n")


def meet_hagrid(character):
    first_name = character["First Name"]

    print(f"\nHagrid: 'Hello {first_name}! I’m here to help you with your shopping on Diagon Alley.'")

    choice = ask_choice("Do you want to follow Hagrid?", ["Yes", "No"])

    if choice == "Yes":
        print("\nGreat! You follow Hagrid toward Diagon Alley.")
    else:
        print("\nHagrid gently insists and takes you along anyway!")

    print("You are now heading to Diagon Alley...\n")


def buy_supplies(character, file_path="data/inventory.json"):
    catalog = load_file(file_path)

    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"]
    bought_required = []

    print("Welcome to Diagon Alley!")
    print("Catalog of available items:")

    # afficher le catalogue
    for key in catalog:
        name, price = catalog[key]
        required = " (required)" if name in required_items else ""
        print(f"{key}. {name} - {price} Galleons{required}")

    # acheter les items obligatoires
    while len(bought_required) < 3:
        print(f"\nYou have {character['Money']} Galleons.")
        remaining = [item for item in required_items if item not in bought_required]
        print("Remaining required items:", ", ".join(remaining))

        choice = ask_text("Enter the number of the item to buy: ")

        if choice not in catalog:
            print("Please choose a valid item number.")
            continue

        name, price = catalog[choice]

        if price > character["Money"]:
            print("You don't have enough money... Game over.")
            exit(0)

        modify_money(character, -price)
        add_item(character, "Inventory", name)
        print(f"You bought: {name} (-{price} Galleons).")

        if name in required_items and name not in bought_required:
            bought_required.append(name)

    print("\nAll required items have been purchased!")

    # choisir un animal
    pets = ["Owl", "Cat", "Rat", "Toad"]
    pet_prices = {"Owl": 20, "Cat": 15, "Rat": 10, "Toad": 5}

    print("\nIt's time to choose your Hogwarts pet!")
    print(f"You have {character['Money']} Galleons.")

    choice_pet = ask_choice("Which pet do you want?", pets)
    price = pet_prices[choice_pet]

    if price > character["Money"]:
        print("You don't have enough money to buy a pet... Game over.")
        exit(0)

    modify_money(character, -price)
    add_item(character, "Inventory", choice_pet)
    print(f"You chose: {choice_pet} (-{price} Galleons).")

    print("\nFinal inventory:\n")
    display_character(character)


def start_chapter_1():
    introduction()
    character = create_character()
    receive_letter()
    meet_hagrid(character)
    buy_supplies(character)
    print("\nEnd of Chapter 1! Your adventure begins at Hogwarts...\n")
    return character
