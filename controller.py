class Controller:
    def __init__(self, num_rounds):
        self.num_rounds = num_rounds
        self.rounds = []
        self.players = []
        self.view = View()

    def add_player(self, name):
        player = Player(name)
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


class View:
    def display_tournament_results(self, players):
        players.sort(key=lambda x: x.points, reverse=True)
        print("Tournament results :")
        for i, player in enumerate(players):
            print(f"{i+1}. {player.name} : {player.points} points")

    def display_tournament(self, rounds):
        res = f"Tournament with {len(rounds)} rounds : \n"
        for round in rounds:
            res += f"{round}\n"
        print(res)

    def add_player(self):
        name = input("Player name: ")
        return name

    def add_round(self):
        return int(input("Round number: "))