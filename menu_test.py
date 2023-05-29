def display_menu():
    print("1. Display tournament information")
    print("2. Display information for a specific round")
    print("3. Display registered players' information")
    print("4. Modify general remarks from the tournament director")
    print("5. Quit")

def display_tournament_info(tournament):
    print("Tournament information:")
    print("Name:", tournament["name"])
    print("Location:", tournament["location"])
    print("Start date:", tournament["start_date"])
    print("End date:", tournament["end_date"])
    print("Number of rounds:", tournament["num_rounds"])
    print("Current round:", tournament["current_round"])

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

tournament = {
    "name": "Chess Tournament",
    "location": "Chess Center",
    "start_date": "2023-06-01",
    "end_date": "2023-06-30",
    "num_rounds": 4,
    "current_round": 2,
    "rounds": [...],  # To be completed with the list of rounds
    "registered_players": ["Stéphane""Loic","Mikael","Arthur","Antoine","Daniel"],  # To be completed with the list of registered players
    "general_remarks": "" #maybe get rid of this section ?
}

while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        display_tournament_info(tournament)
    elif choice == "2":
        round_number = int(input("Enter the round number: "))
        round = tournament["rounds"][round_number - 1]
        display_round_info(round)
    elif choice == "3":
        display_registered_players(tournament["registered_players"])
    elif choice == "4":
        modify_general_remarks(tournament)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

