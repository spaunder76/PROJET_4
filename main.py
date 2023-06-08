from models import Tournament
from views import TournamentView
from controller import TournamentController
def display_menu():
    print("1. Create a tournament")
    print("2. Display tournament information")
    print("3. Display information for a specific round")
    print("4. Display registered players' information")
    print("5. Modify general remarks from the tournament director")
    print("6. Quit")

def display_tournament_info(tournament):
    print(tournament)
    #tournamentView = TournamentView()
    #tournamentView.display_tournament(tournament)
    '''print("Tournament information:")
    print("Name:", tournament["name"])
    print("Location:", tournament["location"])
    print("Start date:", tournament["start_date"])
    print("End date:", tournament["end_date"])
    print("Number of rounds:", tournament["num_rounds"])
    print("Current round:", tournament["current_round"])'''

def display_round_info(round):
    print("Round information:")
    print("Round number:", round["number"])
    print("Match list:")
    for match in round["matches"]:
        print(" -", match[0], "vs", match[1])

def display_registered_players(players):
    print("List of registered players:")
    for player in players:
        print("-", player)

def modify_general_remarks(tournament):
    remarks = input("Enter the general remarks from the tournament director: ")
    tournament["general_remarks"] = remarks
    print("General remarks modified successfully.")

tournament = Tournament(
    "Chess Tournament",
    "Chess Center",
    "2023-06-01",
    "2023-06-30",
    [],
    ["Stéphane""Loic","Mikael","Arthur","Antoine","Daniel"],
    4,
    2,
    "")

tournament_controller = TournamentController()

while True:
    display_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        tournament_controller.create_tournament()
    elif choice == "2":
        tournament_controller.display_tournament_info()
    elif choice == "3":
        tournament_controller.display_round_info()
    elif choice == "4":
        tournament_controller.display_registered_players()
    elif choice == "5":
        tournament_controller.modify_general_remarks()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")


