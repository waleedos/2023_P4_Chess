import json
import datetime

class Player:
    def __init__(self, last_name, first_name, date_of_birth, score):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")
        self.score = score

    def to_json(self):
        data = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth.strftime("%d/%m/%Y"),
            "score": self.score
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data["last_name"], data["first_name"], data["date_of_birth"], data["score"])
