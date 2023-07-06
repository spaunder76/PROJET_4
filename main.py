from models import Tournament
from controller import Controller
from view import View

controller = Controller(View)

while True:
    controller.display_menu()
    choice = controller.set_menu_choice()

    match choice:
        case "0":
            break
        case "1":
            controller.create_tournament()
        case "2":
            controller.display_tournament_info()
        case "3":
            controller.display_round_info()
        case "4":
            controller.display_registered_players()
        case "5":
            controller.modify_general_remarks()
        case _:
            controller.display_menu_invalid_choice()




