from hogwarts.utils.input_utils import ask_choice


def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] = houses[house_name] + points
        print(f"{house_name} gains {points} points.")
        print(f"New total for {house_name}: {houses[house_name]} points.")
    else:
        print("Warning: house not found.")


def display_winning_house(houses):
    max_score = max(houses.values())

    winners = []
    for house in houses:
        if houses[house] == max_score:
            winners.append(house)

    if len(winners) == 1:
        print(f"The winning house is {winners[0]} with {max_score} points!")
    else:
        print(f"There is a tie with {max_score} points between:")
        for house in winners:
            print("-", house)


def assign_house(character, questions):
    scores = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    attributes = character["Attributes"]

    scores["Gryffindor"] = scores["Gryffindor"] + attributes["courage"] * 2
    scores["Slytherin"] = scores["Slytherin"] + attributes["ambition"] * 2
    scores["Hufflepuff"] = scores["Hufflepuff"] + attributes["loyalty"] * 2
    scores["Ravenclaw"] = scores["Ravenclaw"] + attributes["intelligence"] * 2

    for question, choices, houses_list in questions:
        choice_text = ask_choice(question, choices)

        index = choices.index(choice_text)

        chosen_house = houses_list[index]
        scores[chosen_house] = scores[chosen_house] + 3

        print()

    print("Summary of scores:")
    for house in scores:
        print(f"{house}: {scores[house]} points")

    final_house = max(scores, key=scores.get)
    return final_house
