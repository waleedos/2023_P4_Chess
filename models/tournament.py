import json
from datetime import datetime
from models.round import Round


class Tournament:
    DATE_FORMAT = "%d/%m/%Y"

    def __init__(self, name, location, start_date, end_date, rounds=4):
        self.name = name
        self.location = location
        self.start_date = datetime.strptime(start_date, self.DATE_FORMAT)
        self.end_date = datetime.strptime(end_date, self.DATE_FORMAT)
        self.rounds = rounds
        self.current_round = 0
        self.rounds_list = []
        self.players_list = []
        self.description = ''

    def to_json(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime(self.DATE_FORMAT),
            "end_date": self.end_date.strftime(self.DATE_FORMAT),
            "rounds": self.rounds,
            "current_round": self.current_round,
            "rounds_list": [round.to_json() for round in self.rounds_list],
            "players_list": [player.to_json() for player in self.players_list],
            "description": self.description,
        }

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        data["start_date"] = datetime.strptime(data["start_date"], cls.DATE_FORMAT)
        data["end_date"] = datetime.strptime(data["end_date"], cls.DATE_FORMAT)
        data["rounds_list"] = [Round.from_json(round) for round in data["rounds_list"]]
        data["players_list"] = [Player.from_json(player) for player in data["players_list"]]
        return cls(**data)
