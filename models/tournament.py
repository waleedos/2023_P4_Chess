import json
import datetime

class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds=4):
        self.name = name
        self.location = location
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
        self.rounds = rounds
        self.current_round = 0
        self.rounds_list = []
        self.players_list = []
        self.description = ''

    def to_json(self):
        data = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime("%d/%m/%Y"),
            "end_date": self.end_date.strftime("%d/%m/%Y"),
            "rounds": self.rounds,
            "current_round": self.current_round,
            "rounds_list": [round.to_json() for round in self.rounds_list],
            "players_list": [player.to_json() for player in self.players_list],
            "description": self.description
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        tournament = cls(data["name"], data["location"], data["start_date"], data["end_date"], data["rounds"])
        tournament.current_round = data["current_round"]
        tournament.rounds_list = [Round.from_json(round_json) for round_json in data["rounds_list"]]
        tournament.players_list = [Player.from_json(player_json) for player_json in data["players_list"]]
        tournament.description = data["description"]
        return tournament
