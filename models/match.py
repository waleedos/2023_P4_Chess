from views.view import View


class Match:

    def __init__(self, player_1, player_2, name):
        """
        Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant
        deux éléments : une référence à une instance de joueur et un score.
        Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
        """
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.winner = None
        self.name = name

    def player_winner(self, winner):
        if winner == self.player_1:
            return f"Le gagnant est {self.player_1}"
        if winner == self.player_2:
            return f"Le gagnant est {self.player_2}"
        if winner == 'ex aequo':
            return f"{self.player_1} et {self.player_2} ont fait ex aequo"

    def play_match(self):
        print()
        winner = View().get_user_entry(
            msg_display=f"{self.player_1.firstname} VS {self.player_2.firstname}\n"
                        "Gagnant ?\n"
                        f"0 - {self.player_1.firstname}\n"
                        f"1 - {self.player_2.firstname}\n"
                        "2 - Égalité\n"
                        ">>> ",
            msg_error="Veuillez entrer 0, 1 ou 2.",
            value_type="selection",
            assertions=["0", "1", "2"]
        )

        if winner == "0":
            self.winner = self.player_winner(self.player_1)
            self.score_player_1 += 1
        elif winner == "1":
            self.winner = self.player_winner(self.player_2)
            self.score_player_2 += 1
        elif winner == "2":
            self.winner = self.player_winner('ex aequo')
            self.score_player_1 += 0.5
            self.score_player_2 += 0.5

        self.player_1.tournament_score += self.score_player_1
        self.player_2.tournament_score += self.score_player_2

    def get_serialized_match(self):
        return {
            "player_1": self.player_1.get_serialized_player(),
            "score_player_1": self.score_player_1,
            "player_2": self.player_2.get_serialized_player(),
            "score_player_2": self.score_player_2,
            "winner": self.winner,
            "name": self.name,
        }
