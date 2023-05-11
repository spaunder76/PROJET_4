class View:
    def display_tournament_results(self, players):
        players.sort(key=lambda x: x.points, reverse=True)
        print("Tournament Results:")
        for i, player in enumerate(players):
            print(f"{i+1}. {player.name} : {player.points} points")
    
    def display_tournament(self, rounds):
        res = f"Tournament with {len(rounds)} rounds: \n"
        for round in rounds:
            res += f"{round}\n"
        print(res)

class TournamentView:
    def display_tournament(self, tournament):
        print(f"{tournament.name} ({tournament.start_date} - {tournament.end_date}) at {tournament.location}")
        print(f"{len(tournament.players)} registered players")
        print(f"Current round: {tournament.current_round}/{tournament.number_of_rounds}")
        print(f"Notes: {tournament.notes}\n")
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