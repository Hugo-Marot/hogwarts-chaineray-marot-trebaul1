from hogwarts.utils.input_utils import ask_choice, load_file
from hogwarts.universe.character import display_character
from hogwarts.universe.house import assign_house


def meet_friends(character):
    attrs = character["Attributes"]

    print("You board the Hogwarts Express. The train slowly departs northward...")

    # Ron
    choice = ask_choice(
        "\nA red-haired boy enters your compartment.\n— Hi! I'm Ron Weasley. Mind if I sit with you?\nHow do you respond?",
        ["Sure, have a seat!", "Sorry, I prefer to travel alone."]
    )

    if choice.startswith("Sure"):
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
        attrs["loyalty"] = attrs["loyalty"] + 1
    else:
        print("Ron looks a bit disappointed, but shrugs and leaves.")
        attrs["ambition"] = attrs["ambition"] + 1

    # Hermione
    choice = ask_choice(
        "\nA girl enters next, carrying a stack of books.\n— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?\nHow do you respond?",
        ["Yes, I love learning new things!", "Uh… no, I prefer adventures over books."]
    )

    if choice.startswith("Yes"):
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
        attrs["intelligence"] = attrs["intelligence"] + 1
    else:
        print("Hermione raises an eyebrow: — Well, I suppose there are different kinds of courage...")
        attrs["courage"] = attrs["courage"] + 1

    # Draco
    choice = ask_choice(
        "\nThen a blonde boy enters, looking arrogant.\n— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?\nHow do you respond?",
        ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."]
    )

    if choice.startswith("Shake"):
        print("You shake Draco's hand politely. He smirks, satisfied.")
        attrs["ambition"] = attrs["ambition"] + 1
    elif choice.startswith("Ignore"):
        print("Draco frowns, annoyed. — You'll regret that!")
        attrs["loyalty"] = attrs["loyalty"] + 1
    else:
        print("You respond with confidence. Draco looks taken aback, then glares at you.")
        attrs["courage"] = attrs["courage"] + 1

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
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]

    house = assign_house(character, questions)
    character["House"] = house

    print(f"\nThe Sorting Hat exclaims: {house}!!!")
    print(f"You join the {house} students to loud cheers!")


def enter_common_room(character):
    house_name = character.get("House")
    if house_name is None:
        print("Error: The character has no assigned house.")
        return

    house_data = load_file("data/houses.json")
    info = house_data[house_name]

    emoji = info["emoji"]
    description = info["description"]
    installation_message = info["installation_message"]
    colors = info["colors"]

    print("\nYou follow the prefects through the castle corridors...")
    print(f"{emoji} {description}")
    print(f"✨ {installation_message}")
    print(f"Your house colors: {', '.join(colors)}\n")


def start_chapter_2(character):
    print("\n--- Chapter 2: A New Beginning at Hogwarts ---\n")

    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)

    display_character(character)

    print("\nEnd of Chapter 2!")
    print("Tomorrow, your first classes at Hogwarts will begin...")
