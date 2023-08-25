class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points

    def __str__(self):
        return self.name


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def play_match(self, result):
        self.result = result

        if result == 0.5:
            self.player1.add_points(0.5)
            self.player2.add_points(0.5)
        elif result == 1:
            self.player1.add_points(1)
        elif result == 2:
            self.player2.add_points(1)

    def __str__(self):
        return f"{self.player1} vs {self.player2} : {self.result}"


class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds=None, players=None, num_rounds=4, current_round=1, remarks=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = rounds if rounds else []
        self.players = players if players else []
        self.remarks = remarks if remarks else ""

    def add_round(self, round):
        self.rounds.append(round)

    def next_round(self):
        self.current_round += 1

    def __str__(self):
        tournament_info = (
            f"{self.name} ({self.start_date} - {self.end_date}) at {self.location}\n"
            f"{len(self.players)} registered players\nCurrent round: {self.current_round}/{self.num_rounds}\nNotes: {self.remarks}\n"
        )
        for round in self.rounds:
            tournament_info += f"\n{round}"
            for match in round.matches:
                tournament_info += f"\n{match}"
        return tournament_info


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
        round_info = f"Round {self.round_number} : \n"
        for match in self.matches:
            round_info += f"{match}\n"
        return round_info
