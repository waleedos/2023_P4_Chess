from utils.timestamp import get_timestamp
from models.match import Match


class Round:
    def __init__(self, name, players_pairs, load_match=False):

        self.name = name
        self.players_pairs = players_pairs

        if load_match:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

        self.start_date = get_timestamp()
        self.end_date = None

    def __str__(self):
        return self.name

    def create_matchs(self):
        matchs = []

        for i, players in enumerate(self.players_pairs):
            matchs.append(Match(players[0], players[1], f"Match {i}"))
        return matchs

    def mark_as_complete(self):
        self.end_date = get_timestamp()
        print(f"{self.end_date} : {self.name} terminé.")
        print("Rentrez les résultats des matchs:")
        for match in self.matchs:
            match.play_match()

    def get_serialized_round(self):
        ser_players_pairs = []
        for pair in self.players_pairs:
            ser_players_pairs.append(
                (
                    pair[0].get_serialized_player(),
                    pair[1].get_serialized_player()
                 )
            )

        return {
            "name": self.name,
            "players_pairs": ser_players_pairs,
            "matchs": [match.get_serialized_match() for match in self.matchs],
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
