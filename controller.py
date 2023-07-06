from models import Tournament
import re
import datetime
from models import Round

class Controller:
    def __init__(self, View, num_rounds = 1):
        self.num_rounds = num_rounds
        self.rounds = []
        self.players = []
        self.view = View
        self.tournament = None

    ### DISPLAY ###
    def display_menu(self):
        self.view.display_menu()

    def display_menu_invalid_choice(self):
        self.view.display_menu_invalid_choice()

    def display_tournament_results(self):
        self.view.display_tournament_results(self.players)

    def display_tournament(self):
        self.view.display_tournament(self.rounds)
        
    def display_tournament_info(self):
        self.view.display_tournament_info(self)

    def display_round_info(self):
        self.view.display_tournament_round_info(self)

    def display_registered_players(self):
        self.view.display_tournament_registered_players(self)

    ### SET ###
    def set_menu_choice(self):
        return self.view.set_menu_choice()

    ### ADD ###
    def add_Player(self, name):
        player = self.view.add_player()
        self.players.append(player)

    ### CREATE ###
    def create_round(self, round_number):
        round = Round(round_number, self.players)
        self.rounds.append(round)

    def create_tournament(self):
        name = self.view.set_tournament_name()
        location = self.view.set_tournament_location()
        start_date = self.view.set_tournament_date("start")
        end_date = self.view.set_tournament_date("end")
        num_rounds, current_round = self.view.set_tournament_round_info()
        general_remarks = self.view.set_tournament_general_remarks()
        registered_players = self.view.set_tournament_registered_players(self)
        rounds = self.view.set_tournament_rounds_info(self, num_rounds)

        self.tournament = Tournament(name, location, start_date, end_date, rounds, registered_players,
                                     num_rounds, current_round, general_remarks)
        
        self.view.display_tournament_created()

    ### PLAY ###
    def play_tournament(self):
        for round in self.rounds:
            round.play_round()

    ### MODIFY ###
    def modify_general_remarks(self):
        self.view.modify_tournament_general_remarks(self)



   