class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.current_round = 0
        self.rounds_list = []
        self.players_list = []
        self.description = ''
