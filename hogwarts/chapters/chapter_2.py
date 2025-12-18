from hogwarts.universe.character import *
from hogwarts.universe.house import *
from hogwarts.utils.input_utils import *

def meet_friends(character):

    attrs = character["Attributes"]

    print("You board the Hogwarts Express. The train slowly departs northward...")
    print("\nA red-haired boy enters your compartment, looking friendly.")
    print("— Hi! I'm Ron Weasley. Mind if I sit with you?")
    print("How do you respond?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")

    while True:
        choice = input("Your choice: ")
        if choice in ["1", "2"]:
            break
        print("Please enter 1 or 2.")

    if choice == "1":
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
        attrs["Loyalty"] += 1
    else:
        print("Ron looks a bit disappointed, but shrugs and leaves.")
        attrs["Ambition"] += 1

    print("\nA girl enters next, already carrying a stack of books.")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print("How do you respond?")
    print("1. Yes, I love learning new things!")
    print("2. Uh… no, I prefer adventures over books.")

    while True:
        choice = input("Your choice: ")
        if choice in ["1", "2"]:
            break
        print("Please enter 1 or 2.")

    if choice == "1":
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
        attrs["Intelligence"] += 1
    else:
        print("Hermione raises an eyebrow: — Well, I suppose there are different kinds of courage...")
        attrs["Courage"] += 1

    print("\nThen a blonde boy enters, looking arrogant.")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    print("How do you respond?")
    print("1. Shake his hand politely.")
    print("2. Ignore him completely.")
    print("3. Respond with arrogance.")

    while True:
        choice = input("Your choice: ")
        if choice in ["1", "2", "3"]:
            break
        print("Please enter 1, 2 or 3.")

    if choice == "1":
        print("You shake Draco's hand politely. He smirks, satisfied.")
        attrs["Ambition"] += 1
    elif choice == "2":
        print("Draco frowns, annoyed. — You'll regret that!")
        attrs["Loyalty"] += 1
    else:
        print("You respond with confidence. Draco looks taken aback, then glares at you.")
        attrs["Courage"] += 1

    print("\nThe train continues its journey. Hogwarts Castle appears on the horizon...")
    print("Your choices already say a lot about your personality!")
    print(f"Your updated attributes: {attrs}")

def welcome_message():

    print("\n======================================================")
    print("Welcome to Hogwarts School of Witchcraft and Wizardry!")
    print("======================================================\n")

    print("Professor Dumbledore appears with a warm smile:")
    print("“Welcome, dear students, to Hogwarts. Here, you will discover magic,")
    print("forge friendships, and learn more about yourselves than you ever imagined.")
    print("But for now… let the Sorting Ceremony begin!”\n")

    input("Press Enter to continue... ")

def sorting_ceremony(character):
    print("The sorting ceremony begins in the Great Hall...")
    print("The Sorting Hat observes you for a long time before asking its questions:\n")

    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious",
             "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy",
             "Rely on your friends", "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]

    house = assign_house(character, questions)

    character["House"] = house

    print(f"\nThe Sorting Hat exclaims: {house}!!!")
    print(f"You join the {house} students to loud cheers!")


def enter_common_room(character):

    house_name = character.get("House")

    if not house_name:
        print("Error: The character has no assigned house.")
        return

    house_data = load_file("data/houses.json")

    if house_data is None:
        print("Error: Could not load houses.json")
        return

    info = house_data.get(house_name)

    if info is None:
        print(f"Error: House '{house_name}' not found in houses.json")
        return

    emoji = info.get("emoji", "")
    description = info.get("description", "")
    welcome = info.get("welcome", "")
    colors = info.get("colors", [])

    print("\nYou follow the prefects through the castle corridors...")

    print(f"{emoji} {description}")

    print(f"✨ {welcome}")

    print(f"Your house colors: {', '.join(colors)}\n")

def start_chapter_2(character):
    print("\n--- Chapter 2: A New Beginning at Hogwarts ---\n")

    meet_friends(character)

    welcome_message()

    sorting_ceremony(character)

    enter_common_room(character)

    display_character(character)

    print("\nChapter 2 ends here.")
    print("Tomorrow, your first classes at Hogwarts will begin...")
