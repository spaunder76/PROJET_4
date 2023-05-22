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

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

    def next_round(self):
        self.current_round += 1

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date}) at {self.location} with {len(self.players)} players"

