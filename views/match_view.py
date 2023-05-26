class MatchView:
    @staticmethod
    def display_match(match):
        print(f"Match: {match.player1.name} VS {match.player2.name}")
        print(f"Scores: {match.player1.name}: {match.score1}, {match.player2.name}: {match.score2}")

    @staticmethod
    def input_scores(match):
        match.score1 = float(input(f"Entrer le score pour {match.player1.name}: "))
        match.score2 = float(input(f"Entrer le score pour {match.player2.name}: "))
