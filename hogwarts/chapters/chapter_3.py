import random
from hogwarts.utils.input_utils import load_file
from hogwarts.universe.house import update_house_points, display_winning_house
from hogwarts.universe.character import display_character, add_item

def learn_spells(character, file_path="data/spells.json"):
    spells = load_file(file_path)

    quotas = {"Offensive": 1, "Defensive": 1, "Utility": 3}
    learned = []

    print("You begin your magic lessons at Hogwarts...")

    while sum(quotas.values()) > 0:
        spell = random.choice(spells)
        spell_type = spell["type"]

        if quotas[spell_type] > 0 and spell not in learned:
            learned.append(spell)
            add_item(character, "Spells", spell["name"])
            quotas[spell_type] = quotas[spell_type] - 1

            print(f"You have just learned the spell: {spell['name']} ({spell_type})")
            input("Press Enter to continue...")

    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for s in learned:
        print(f"- {s['name']} ({s['type']}): {s['description']}")


def magic_quiz(character, file_path="data/magic_quiz.json"):
    quiz = load_file(file_path)

    print("\nWelcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.\n")

    selected = []
    while len(selected) < 4:
        q = random.choice(quiz)
        if q not in selected:
            selected.append(q)

    score = 0
    for i in range(4):
        print(f"{i + 1}. {selected[i]['question']}")
        answer = input("> ").strip()

        if answer.lower() == selected[i]["answer"].lower():
            print("Correct answer! +25 points for your house.\n")
            score = score + 25
        else:
            print(f"Wrong answer. The correct answer was: {selected[i]['answer']}\n")

    print(f"Score obtained: {score} points")
    return score


def start_chapter_3(character, houses):
    learn_spells(character)
    points = magic_quiz(character)

    update_house_points(houses, character["House"], points)
    display_winning_house(houses)
    display_character(character)
