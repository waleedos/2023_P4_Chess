from models.round import Round

ROUNDS_NUMBER = 4


class Tournament:
    def __init__(self, name, location, date, time_control, players, rounds_number=ROUNDS_NUMBER, description=""):
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.players = players
        self.rounds_number = rounds_number
        self.description = description
        self.list_round = []

    def __str__(self):
        return f"{self.name} qui a eu lieu le {self.date}"

    def create_round(self, round_number):
        players_pairs = self.create_players_pairs(current_round=round_number)
        round = Round("Round " + str(round_number + 1), players_pairs)
        self.list_round.append(round)

    def create_players_pairs(self, current_round):

        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.rating, reverse=True)

        else:
            sorted_players = []
            score_sorted_players = sorted(self.players, key=lambda x: x.total_score, reverse=True)

            for i, player in enumerate(score_sorted_players):
                try:
                    sorted_players.append(player)
                except player.total_score == score_sorted_players[i + 1].total_score:
                    if player.rating > score_sorted_players[i + 1].rating:
                        hi_player = player
                        lo_player = score_sorted_players[i + 1]
                    else:
                        hi_player = score_sorted_players[i + 1]
                        lo_player = player
                    sorted_players.append(hi_player)
                    sorted_players.append(lo_player)
                except IndexError:
                    sorted_players.append(player)

        first_half_players = sorted_players[len(sorted_players) // 2:]
        second_half_players = sorted_players[:len(sorted_players) // 2]

        players_pairs = []

        for i, player in enumerate(first_half_players):
            a = 0
            while True:
                try:
                    player_2 = second_half_players[i + a]

                except IndexError:
                    player_2 = second_half_players[i]
                    players_pairs.append((player, player_2))

                    player.played_with.append(player_2)
                    player_2.played_with.append(player)
                    break

                if player in player_2.played_with:
                    a += 1
                    continue

                else:
                    players_pairs.append((player, player_2))
                    player.played_with.append(player_2)
                    player_2.played_with.append(player)
                    break

        return players_pairs

    def get_rankings(self, by_score=True):

        if by_score:
            sorted_players = sorted(self.players, key=lambda x: x.tournament_score, reverse=True)
        else:
            sorted_players = sorted(self.players, key=lambda x: x.rank, reverse=True)

        return sorted_players

    def get_serialized_tournament(self, save_rounds=False):

        serialized_tournament = {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "time_control": self.time_control,
            "players": [player.get_serialized_player() for player in self.players],
            "rounds_number": self.rounds_number,
            "list_round": [rd.get_serialized_round() for rd in self.list_round],
            "description": self.description
        }

        if save_rounds:
            serialized_tournament["list_round"] = [round.get_serialized_round() for round in self.list_round]

        return serialized_tournament
