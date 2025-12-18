def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] += points
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

    scores["Gryffindor"] += character.get("courage", 0) * 2
    scores["Slytherin"] += character.get("ambition", 0) * 2
    scores["Hufflepuff"] += character.get("loyalty", 0) * 2
    scores["Ravenclaw"] += character.get("intelligence", 0) * 2

    for question, choices, houses in questions:
        print(question)
        for i in range(len(choices)):
            print(f"{i + 1}. {choices[i]}")

        choice = int(input("Your choice: ")) - 1
        chosen_house = houses[choice]

        scores[chosen_house] += 3
        print()

    print("Summary of scores:")
    for house in scores:
        print(f"{house}: {scores[house]} points")

    final_house = max(scores, key=scores.get)

    return final_house
