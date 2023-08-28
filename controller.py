from models import Tournament,Player
import re
import datetime
from models import Round
import json
import random
import os

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


    def load_rounds(self):
        for round_number in range(1, self.num_rounds + 1):
            filename = f"round{round_number}.json"  
            try:
                with open(filename, "r") as file:
                    round_data = json.load(file)
                    matches = []

                    for match_data in round_data:
                        player1_name = match_data["player1"]
                        player2_name = match_data["player2"]
                        player1 = self.find_player_by_name(player1_name)
                        player2 = self.find_player_by_name(player2_name)
                        result = match_data["result"]
                        match = Match(player1, player2)
                        match.result = result
                        matches.append(match)

                    round_obj = Round(round_number, self.players)
                    round_obj.matches = matches
                    self.rounds.append(round_obj)

                print(f"Round {round_number} loaded from", filename)
            except FileNotFoundError:
                print(f"No previously saved data found for Round {round_number}.")

    def save_round(self, round_obj):
        filename = f"round{round_obj.round_number}.json"  

        round_data = []
        for match in round_obj.matches:
            data = {
                "player1": match.player1.name,
                "player2": match.player2.name,
                "result": match.result
            }
            round_data.append(data)

        with open(filename, "w") as file:
            json.dump(round_data, file)

        print(f"Round {round_obj.round_number} saved to", filename)


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


    def calculate_scores(self):
        player_scores = {}  
        all_players = set() 

        round_files = [file for file in os.listdir() if file.startswith("round") and file.endswith(".json")]

        for round_file in round_files:
            with open(round_file, "r") as file:
                round_data = json.load(file)
                matches = round_data["matches"]

                for match in matches:
                    player1, player2 = match
                    all_players.add(player1)
                    all_players.add(player2)

                    outcome = input(f"Who wins between {player1} and {player2}? (1 for {player1}, 2 for {player2}, 3 for draw): ")

                    if outcome == "1":  # Player 1 wins
                        winner, loser = player1, player2
                    elif outcome == "2":  # Player 2 wins
                        winner, loser = player2, player1
                    else:  # Draw
                        winner, loser = None, None

                    if winner is not None:
                        player_scores.setdefault(winner, 0)
                        player_scores[winner] += 1 
                    if loser is not None:
                        player_scores.setdefault(loser, 0)

                    if outcome == "3":
                        player_scores.setdefault(player1, 0)
                        player_scores[player1] += 0.5
                        player_scores.setdefault(player2, 0)
                        player_scores[player2] += 0.5

        for player in all_players:
            player_scores.setdefault(player, 0)

        sorted_player_scores = sorted(player_scores.items(), key=lambda item: item[1], reverse=True)

        print("Player scores:")
        for player, score in sorted_player_scores:
            print(f"{player}: {score} points")




   