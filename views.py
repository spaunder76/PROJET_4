class View:
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

    def add_player(self):
        name = input("Player name: ")
        return name

    def add_round(self):
        return int(input("Round number: "))
    

class TournamentView:
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

    def add_player(self):
        name = input("Player name: ")
        surname = input("Player surname: ")
        birth_date = input("Player birth date: ")
        ranking = input("Player ranking: ")
        return (name, surname, birth_date, ranking)

    def add_round(self):
        return int(input("Round number: "))
    
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

    def modify_general_remarks(tournament):
        remarks = input("Enter the general remarks from the tournament director: ")
        tournament["general_remarks"] = remarks
        print("General remarks modified successfully.")
        
