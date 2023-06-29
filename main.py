from models import Tournament
from views import TournamentView
from controller import TournamentController
from controller import Controller



tournament_controller = TournamentController()

while True:
    Controller.display_menu()
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


