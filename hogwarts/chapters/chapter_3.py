import random
from hogwarts.utils.input_utils import load_file
from hogwarts.universe.house import update_house_points, display_winning_house
from hogwarts.universe.character import display_character

def learn_spells(character, file_path="../data/spells.json"):
    spells = load_file(file_path)
    quotas = {"Offensive": 1, "Defensive": 1, "Utility": 3}
    learned = []

    while sum(quotas.values()) > 0:
        spell = random.choice(spells)
        t = spell["type"]
        if quotas.get(t, 0) > 0 and spell not in learned:
            learned.append(spell)
            character["Spells"].append(spell)
            quotas[t] -= 1
            print(f"You learned {spell['name']} ({t})")
            input("Press Enter...")

    for s in learned:
        print(f"- {s['name']} ({s['type']}): {s['description']}")

def magic_quiz(character, file_path="../data/magic_quiz.json"):
    quiz = load_file(file_path)
    score = 0
    for q in quiz[:4]:
        print(q["question"])
        answer = input("> ")
        if answer.lower() == q["answer"].lower():
            score += 25
    print(f"Score obtained: {score}")
    return score

def start_chapter_3(character, houses):
    learn_spells(character)
    points = magic_quiz(character)
    update_house_points(houses, character["House"], points)
    display_winning_house(houses)
    display_character(character)
