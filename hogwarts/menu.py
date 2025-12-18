from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3

def display_main_menu():
    print("1. Start game")
    print("2. Exit")

def launch_menu_choice():
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    display_main_menu()
    choice = input("> ")

    if choice == "1":
        character = start_chapter_1()
        start_chapter_2(character)
        start_chapter_3(character, houses)
    else:
        print("Goodbye!")
