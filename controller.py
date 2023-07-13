from models import Tournament,Player
import re
import datetime
from models import Round
import json


class Controller:
    def __init__(self, View, num_rounds = 1):
        self.num_rounds = num_rounds
        self.rounds = []
        self.players = []
        self.view = View
        self.tournament = self.load_tournament()
        self.players=self.load_registered_players()
        self.tournament.players = self.load_registered_players()



    def load_registered_players(self):
        filename = "registered_players.json"

        try:
            with open(filename, "r") as file:
                player_data = json.load(file)
                players = []
                for data in player_data:
                    name = data["name"]
                    surname = data["surname"]
                    birth_date = datetime.datetime.strptime(data["birth_date"], "%Y-%m-%d").date()
                    ranking = data["ranking"]
                    players.append((name, surname, birth_date, ranking))
            print("Registered players loaded from", filename)
            return players
        except FileNotFoundError:
            print("No previously registered players found.")
            return []

    def save_registered_players(self):
        filename = "registered_players.json"
        player_data = []
        for player in self.tournament.players:
            print("____ Saving player")
            print(player)
            data = {
                "name": player[0],
                "surname": player[1],
                "birth_date": str(player[2]),
                "ranking": player[3]
            }
            player_data.append(data)
        with open(filename, "w") as file:
            json.dump(player_data, file)

        print("Registered players saved to", filename)
    def load_tournament(self):
        filename = "tournament.json"

        try:
            with open(filename, "r") as file:
                tournament_data = json.load(file)
                name = tournament_data["name"]
                location = tournament_data["location"]
                start_date = tournament_data["start_date"]
                end_date = tournament_data["end_date"]
                num_rounds = tournament_data["num_rounds"]
                current_round = tournament_data["current_round"]
                remarks = tournament_data["remarks"]
                return Tournament(name, location, start_date, end_date, num_rounds=num_rounds,
                                  current_round=current_round, remarks=remarks)
            print("Tournament loaded from", filename)
        except FileNotFoundError:
            print("No previously saved tournament found.")

        return None

    def save_tournament(self):
        filename = "tournament.json"

        tournament_data = {
            "name": self.tournament.name,
            "location": self.tournament.location,
            "start_date": str(self.tournament.start_date),
            "end_date": str(self.tournament.end_date),
            "num_rounds": self.tournament.num_rounds,
            "current_round": self.tournament.current_round,
            "remarks": self.tournament.remarks
        }

        with open(filename, "w") as file:
            json.dump(tournament_data, file)

        print("Tournament saved to", filename)


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




   