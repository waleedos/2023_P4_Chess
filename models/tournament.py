class Tournament:
    def __init__(self, name, location, start_date, end_date, time_control, number_of_rounds=4, current_round_number=1, players=[], rounds=[], description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.number_of_rounds = number_of_rounds
        self.current_round_number = current_round_number
        self.players = players
        self.rounds = rounds
        self.description = description
