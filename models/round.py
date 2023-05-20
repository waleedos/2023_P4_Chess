import json
import datetime
from models.match import Match

class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_time = datetime.datetime.now()
        self.end_time = None

    def to_json(self):
        data = {
            "name": self.name,
            "matches": [match.to_json() for match in self.matches],
            "start_time": self.start_time.strftime("%d/%m/%Y %H:%M:%S"),
            "end_time": self.end_time.strftime("%d/%m/%Y %H:%M:%S") if self.end_time else None
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        round = cls(data["name"])
        round.matches = [Match.from_json(match_json) for match_json in data["matches"]]
        round.start_time = datetime.datetime.strptime(data["start_time"], "%d/%m/%Y %H:%M:%S")
        if data["end_time"]:
            round.end_time = datetime.datetime.strptime(data["end_time"], "%d/%m/%Y %H:%M:%S")
        return round
