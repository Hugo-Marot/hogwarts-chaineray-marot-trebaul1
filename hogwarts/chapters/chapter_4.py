import random

from hogwarts.utils.input_utils import load_file
from hogwarts.universe.house import update_house_points


def create_team(house, team_data, is_player=False, player=None):
    team = {
        "name": house,
        "score": 0,
        "goals_scored": 0,
        "goals_blocked": 0,
        "caught_snitch": False,
        "players": []
    }

    team["players"] = team_data[house]["players"][:]

    if is_player and player is not None:
        player_name = player["First Name"] + " " + player["Last Name"]
        player_seeker = player_name + " (Seeker)"

        new_list = [player_seeker]
        for p in team["players"]:
            if p != player_seeker and p != player_name and not p.startswith(player_name + " "):
                new_list.append(p)

        team["players"] = new_list

    return team


def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance_goal = random.randint(1, 10)

    if chance_goal >= 6:
        if player_is_seeker:
            scorer = attacking_team["players"][0]
        else:
            scorer = random.choice(attacking_team["players"])

        attacking_team["score"] = attacking_team["score"] + 10
        attacking_team["goals_scored"] = attacking_team["goals_scored"] + 1

        print(f"{scorer} scores a goal for {attacking_team['name']}! (+10 points)")
    else:
        defending_team["goals_blocked"] = defending_team["goals_blocked"] + 1
        print(f"{defending_team['name']} blocks the attack!")


def golden_snitch_appears():
    n = random.randint(1, 6)
    return n == 6


def catch_golden_snitch(e1, e2):
    winner = random.choice([e1, e2])
    winner["score"] = winner["score"] + 150
    winner["caught_snitch"] = True
    print(f"\n✨ The Golden Snitch is caught by {winner['name']}! (+150 points)")
    return winner


def display_score(e1, e2):
    print("Current score:")
    print(f"→ {e1['name']}: {e1['score']} points")
    print(f"→ {e2['name']}: {e2['score']} points")


def display_team(house, team):
    print(f"\n{house} team:")
    for p in team["players"]:
        print("-", p)


def quidditch_match(character, houses):
    team_data = load_file("data/teams_quidditch.json")

    player_house = character["House"]
    all_houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    opponents = [h for h in all_houses if h != player_house]
    opponent_house = random.choice(opponents)

    e1 = create_team(player_house, team_data, is_player=True, player=character)
    e2 = create_team(opponent_house, team_data, is_player=False)

    print(f"\nQuidditch Match: {player_house} vs {opponent_house}!")
    display_team(player_house, e1)
    display_team(opponent_house, e2)

    print(f"\nYou are playing for {player_house} as the Seeker.")

    for turn in range(1, 21):
        print(f"\n━━━ Turn {turn} ━━━")

        attempt_goal(e1, e2, player_is_seeker=True)

        attempt_goal(e2, e1, player_is_seeker=False)

        display_score(e1, e2)

        if golden_snitch_appears():
            catch_golden_snitch(e1, e2)
            break

        input("Press Enter to continue...")

    print("\n===== Match finished! =====")
    display_score(e1, e2)

    if e1["score"] > e2["score"]:
        winner_house = e1["name"]
        print(f"\n🏆 {winner_house} wins the match! (+500 house points)")
        update_house_points(houses, winner_house, 500)

    elif e2["score"] > e1["score"]:
        winner_house = e2["name"]
        print(f"\n🏆 {winner_house} wins the match! (+500 house points)")
        update_house_points(houses, winner_house, 500)

    else:
        winner_house = None
        print("\nIt's a tie! No house gets the +500 bonus.")

    return winner_house


def start_chapter_4_quidditch(character, houses):
    print("\n========================================")
    print("Chapter 4 – Quidditch Final")
    print("========================================")

    quidditch_match(character, houses)

    print("\nEnd of Chapter 4! The Hogwarts Cup is closer than ever...\n")
