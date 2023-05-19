import json

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score = {self.player1: 0, self.player2: 0}

    def to_json(self):
        data = {
            "player1": self.player1.to_json(),
            "player2": self.player2.to_json(),
            "score": self.score
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        player1 = Player.from_json(data["player1"])
        player2 = Player.from_json(data["player2"])
        match = cls(player1, player2)
        match.score = data["score"]
        return match
