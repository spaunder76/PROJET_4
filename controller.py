from models import Tournament
import re
import datetime

class Controller:
    def __init__(self, num_rounds,View):
        self.num_rounds = num_rounds
        self.rounds = []
        self.players = []
        self.view = View()

    def add_player(self, name):
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


class Round:
    def __init__(self, round_number, players):
        self.round_number = round_number
        self.matches = []
        self.players = players

    def add_match(self, match):
        self.matches.append(match)

    def play_round(self):
        for match in self.matches:
            result = int(input(f"Score of {match.player1} ({match.player2}) : "))
            match.play_match(result)

    def __str__(self):
        res = f"Round {self.round_number} : \n"
        for match in self.matches:
            res += f"{match}\n"
        return res

class TournamentController:
    def __init__(self):
        self.tournament = None

    def create_tournament(self):
        name = input("Enter the tournament name: ")

        valid_location = False
        while not valid_location:
            location = input("Enter the tournament location: ")
            if re.match(r'^[a-zA-Z\s]+$', location):
                valid_location = True
            else:
                print("Invalid location. Please enter only letters.")

        print("Tournament location:", location)

        while True:
            start_date_str = input("Enter the tournament start date (YYYY-MM-DD): ")
            try:
                start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

        print("Tournament start date:", start_date)

        while True:
            end_date_str = input("Enter the tournament end date (YYYY-MM-DD): ")
            try:
                end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

        print("Tournament end date:", end_date)

        num_rounds = None
        current_round = None

        while True:
            try:
                num_rounds = int(input("Enter the number of rounds: "))
                current_round = int(input("Enter the current round: "))
                break
            except ValueError:
                print("Invalid input. Please enter only numbers.")

        print("Number of rounds:", num_rounds)
        print("Current round:", current_round)

        general_remarks = input("Enter the general remarks from the tournament director: ")
        registered_players = []

        while True:
            try:
                num_players = int(input("Enter the number of registered players: "))
                break
            except ValueError:
                print("Invalid input. Please enter only numbers.")

        print("Number of registered players:", num_players)  
         
        registered_players = []
        for i in range(num_players):
            while True:
                player = input("Enter player {} name: ".format(i + 1))
                if re.match(r'^[a-zA-Z]+$', player):
                    registered_players.append(player)
                    break
                else:
                    print("Le nom du joueur ne doit contenir que des lettres. Veuillez réessayer.")


        rounds = []
        for i in range(num_rounds):
            round_number = i + 1
            matches = []
            num_matches = int(input("Enter the number of matches for round {}: ".format(round_number)))
            for j in range(num_matches):
                player1 = input("Enter player 1 for match {}: ".format(j + 1))
                player2 = input("Enter player 2 for match {}: ".format(j + 1))
                matches.append((player1, player2))
            round_info = {
                "number": round_number,
                "matches": matches
            }
            rounds.append(round_info)

        self.tournament = Tournament(name, location, start_date, end_date, rounds, registered_players,
                                     num_rounds, current_round, general_remarks)
        print("Tournament created successfully.")
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