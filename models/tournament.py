class Tournament:
    def __init__(self, name, location, start_date, end_date, description="", time_control=1, rounds=4, players=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.rounds = rounds
        self.players = players if players is not None else []

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "rounds": self.rounds,
            "players": self.players,
        }
