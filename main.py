from models import Tournament
from controller import Controller
from view import View

controller = Controller(View)
while True:
    controller.display_menu()
    choice = controller.set_menu_choice()

    if choice == "0":
        break
    elif choice == "1":
        controller.create_tournament()
        controller.save_tournament()
        controller.save_registered_players()
    elif choice == "2":
        controller.display_tournament_info()
    elif choice == "3":
        controller.display_round_info()
    elif choice == "4":
        controller.display_registered_players()
    elif choice == "5":
        controller.modify_general_remarks()
    elif choice == "6":
        controller.calculate_scores()
    else:
        controller.display_menu_invalid_choice()



