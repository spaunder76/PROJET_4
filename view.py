import re
import datetime
import json

class View:
    ### DISPLAY ###
    def display_menu():
        print("========================== MENU ==========================\n")
        print("0. Quit")
        print("1. Create a tournament")
        print("2. Display tournament information")
        print("3. Display information for a specific round")
        print("4. Display registered players' information")
        print("5. Modify general remarks from the tournament director")
        print("6. Calculate the scores of the players")
    
    def display_menu_invalid_choice():
        print("Invalid choice. Please try again.")

    def display_tournament_created():
        print("Tournament created successfully.")

    def display_tournament_results(self, players):
        players.sort(key=lambda x: x.points, reverse=True)
        print("Tournament Results:")
        for i, player in enumerate(players):
            print(f"{i+1}. {player.name} : {player.points} points")
    
    def display_tournament_rounds(self, rounds):
        res = f"Tournament with {len(rounds)} rounds: \n"
        for round in rounds:
            res += f"{round}\n"
        print(res)
    
    def display_tournament(self,tournament):
        print(f"{tournament.name} ({tournament.start_date} - {tournament.end_date}) at {tournament.location}")
        print(f"{len(tournament.players)} registered players")
        print(f"Current round: {tournament.current_round}/{tournament.num_rounds}")
        print(f"Notes: {tournament.remarks}\n")
        for round in tournament.rounds:
            print(round)
            for match in round.matches:
                print(match)
            print()
    
    def display_tournament_info(tournament):
        print(tournament)

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
    


    def display_tournament_round_info(self):
        if self.tournament:
            round_number = int(input("Enter the round number: "))
            filename = f"round{round_number}.json"

            try:
                with open(filename, "r") as file:
                    round_data = json.load(file)
                    matches = round_data["matches"]

                    print("Round information:")
                    print("Round number:", round_number)
                    print("Match list:")
                    for match in matches:
                        print(" -", f"{match[0]} vs {match[1]}")
            except FileNotFoundError:
                print(f"No round{round_number}.json file found.")
        else:
            print("No tournament created yet.")

    def display_tournament_registered_players(self):
        if self.tournament:
            print("List of registered players:")
            for player in self.tournament.players:
                print("-", player)
        else:
            print("No tournament created yet.")


    ### ADD ###
    def add_round():
        return int(input("Round number: "))

    def add_player(self, i):
        name = ''
        surname = ''
        birth_date = None
        ranking = 0
        while True:
            name = input("Enter player {} name: ".format(i + 1))
            if re.match(r'^[a-zA-Z]+$', name):
                break
            else:
                print("Player name should contain only letters. Please try again.")
        while True:
            surname = input("Player surname: ")
            if re.match(r'^[a-zA-Z]+$', surname):
                break
            else:
                print("Player surname should contain only letters. Please try again.")
        while True:
            birth_date_str = input("Enter player birth date (YYYY-MM-DD): ")
            try:
                birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        ranking = self.view.set_number_input("Player ranking: ")
        return (name, surname, birth_date, ranking)

    ### SET ###
    def set_menu_choice():
        return input("Choose an option (0-6): ")
    
    def set_tournament_name():
        return input("Enter the tournament name: ")

    def set_tournament_location():
        while True:
            location = input("Enter the tournament location: ")
            if re.match(r'^[a-zA-Z\s]+$', location):
                return location
            else:
                print("Invalid location. Please enter only letters.")
                
    def set_tournament_date(date_type):
        while True:
            date_str = input("Enter the tournament {} date (YYYY-MM-DD): ".format(date_type))
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                return date
            except ValueError:
                print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

    def set_tournament_registered_players(self):
        num_players = self.view.set_number_input("Enter the number of registered players: ")
        registered_players = []
        for i in range(num_players):
            player = self.view.add_player(self, i)
            registered_players.append(player)
        return registered_players
    
    def set_number_input(message):
        while True:
            try:
                num = int(input(message))
                return num
            except ValueError:
                print("Invalid input. Please enter only numbers.")

    def set_tournament_general_remarks():
        return input("Enter the general remarks from the tournament director: ")
    
    def set_tournament_round_info():
        num_rounds = None
        current_round = None
        while True:
            try:
                num_rounds = int(input("Enter the number of rounds: "))
                current_round = int(input("Enter the current round: "))
                return num_rounds, current_round
            except ValueError:
                print("Invalid input. Please enter only numbers.")
                
    def set_tournament_rounds_info(self, num_rounds):
        rounds = []
        for i in range(num_rounds):
            filename = "round"+str(i+1)+".json"
            round_number = i + 1
            matches = []
            num_matches = self.view.set_number_input("Enter the number of matches for round {}: ".format(round_number))
            for j in range(num_matches):
                player1 = input("Enter player 1 for match {}: ".format(j + 1))
                player2 = input("Enter player 2 for match {}: ".format(j + 1))
                matches.append((player1, player2))
            round_info = {
                "number": round_number,
                "matches": matches
            }
            rounds.append(round_info)
            with open(filename, "w") as file:
                json.dump(round_info, file)
        return rounds

    ### MODIFY ###
    def modify_general_remarks(tournament):
        remarks = input("Enter the general remarks from the tournament director: ")
        tournament["general_remarks"] = remarks
        print("General remarks modified successfully.")
    
    def modify_tournament_general_remarks(self):
        if self.tournament:
            remarks = input("Enter the general remarks from the tournament director: ")
            self.tournament.general_remarks = remarks
            print("General remarks modified successfully.")
        else:
            print("No tournament created yet.")
        
