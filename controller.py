from models import Tournament
import re
import datetime
from models import Round

class Controller:
    def __init__(self, num_rounds,View):
        self.num_rounds = num_rounds
        self.rounds = []
        self.players = []
        self.view = View()

    def __init__(self):
        self.players = []

    def add_Player(self, name):
        player = player(name)
        self.players.append(player)

    def create_round(self, round_number):
        round = Round(round_number, self.players)
        self.rounds.append(round)

    def play_tournament(self):
        for round in self.rounds:
            round.play_round()

    def display_tournament_results(self):
        self.view.display_tournament_results(self.players)

    def display_tournament(self):
        self.view.display_tournament(self.rounds)
    
    def display_menu():
        print("1. Create a tournament")
        print("2. Display tournament information")
        print("3. Display information for a specific round")
        print("4. Display registered players' information")
        print("5. Modify general remarks from the tournament director")
        print("6. Quit")


class TournamentController:
    def __init__(self):
        self.tournament = None

    def create_tournament(self):
        name = input("Enter the tournament name: ")
        location = self.get_tournament_location()
        start_date = self.get_tournament_date("start")
        end_date = self.get_tournament_date("end")
        num_rounds, current_round = self.get_round_info()
        general_remarks = input("Enter the general remarks from the tournament director: ")
        registered_players = self.get_registered_players()
        rounds = self.get_rounds_info(num_rounds)

        self.tournament = Tournament(name, location, start_date, end_date, rounds, registered_players,
                                     num_rounds, current_round, general_remarks)
        print("Tournament created successfully.")

    def get_tournament_location(self):
        while True:
            location = input("Enter the tournament location: ")
            if re.match(r'^[a-zA-Z\s]+$', location):
                return location
            else:
                print("Invalid location. Please enter only letters.")

    def get_tournament_date(self, date_type):
        while True:
            date_str = input("Enter the tournament {} date (YYYY-MM-DD): ".format(date_type))
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                return date
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

    def get_round_info(self):
        num_rounds = None
        current_round = None

        while True:
            try:
                num_rounds = int(input("Enter the number of rounds: "))
                current_round = int(input("Enter the current round: "))
                return num_rounds, current_round
            except ValueError:
                print("Invalid input. Please enter only numbers.")

    def get_registered_players(self):
        num_players = self.get_number_input("Enter the number of registered players: ")
        registered_players = []

        for i in range(num_players):
            while True:
                player = input("Enter player {} name: ".format(i + 1))
                if re.match(r'^[a-zA-Z]+$', player):
                    registered_players.append(player)
                    break
                else:
                    print("Player name should contain only letters. Please try again.")

        return registered_players

    def get_number_input(self, message):
        while True:
            try:
                num = int(input(message))
                return num
            except ValueError:
                print("Invalid input. Please enter only numbers.")

    def get_rounds_info(self, num_rounds):
        rounds = []

        for i in range(num_rounds):
            round_number = i + 1
            matches = []
            num_matches = self.get_number_input("Enter the number of matches for round {}: ".format(round_number))
            for j in range(num_matches):
                player1 = input("Enter player 1 for match {}: ".format(j + 1))
                player2 = input("Enter player 2 for match {}: ".format(j + 1))
                matches.append((player1, player2))
            round_info = {
                "number": round_number,
                "matches": matches
            }
            rounds.append(round_info)

        return rounds

    def display_tournament_info(self):
        if self.tournament:
            print("Tournament information:")
            print("Name:", self.tournament.name)
            print("Location:", self.tournament.location)
            print("Start date:", self.tournament.start_date)
            print("End date:", self.tournament.end_date)
            print("Number of rounds:", self.tournament.num_rounds)
            print("Current round:", self.tournament.current_round)
        else:
            print("No tournament created yet.")

    def display_round_info(self):
        if self.tournament:
            round_number = int(input("Enter the round number: "))
            if 1 <= round_number <= self.tournament.num_rounds:
                round = self.tournament.rounds[round_number - 1]
                print("Round information:")
                print("Round number:", round["number"])
                print("Match list:")
                for match in round["matches"]:
                    print(" -", match[0], "vs", match[1])
            else:
                print("Invalid round number.")
        else:
            print("No tournament created yet.")

    def display_registered_players(self):
        if self.tournament:
            print("List of registered players:")
            for player in self.tournament.registered_players:
                print("-", player)
        else:
            print("No tournament created yet.")

    def modify_general_remarks(self):
        if self.tournament:
            remarks = input("Enter the general remarks from the tournament director: ")
            self.tournament.general_remarks = remarks
            print("General remarks modified successfully.")
        else:
            print("No tournament created yet.")


            