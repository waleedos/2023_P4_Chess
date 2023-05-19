from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament

# Création de deux joueurs
player1 = Player("Doe", "John", "01/01/1980", 1200)
player2 = Player("Smith", "Jane", "05/05/1985", 1300)

# Conversion des joueurs en JSON et retour
player1_json = player1.to_json()
player2_json = player2.to_json()

player1 = Player.from_json(player1_json)
player2 = Player.from_json(player2_json)

print(f"Player 1: {player1.first_name} {player1.last_name}, Score: {player1.score}")
print(f"Player 2: {player2.first_name} {player2.last_name}, Score: {player2.score}")

# Création d'un match entre les deux joueurs
match = Match(player1, player2)

# Conversion du match en JSON et retour
match_json = match.to_json()
match = Match.from_json(match_json)

print(f"Match: {match.player1.last_name} vs {match.player2.last_name}")

# Création d'un round contenant le match
round = Round("Round 1")
round.matches.append(match)

# Conversion du round en JSON et retour
round_json = round.to_json()
round = Round.from_json(round_json)

print(f"{round.name} Matches:")
for match in round.matches:
    print(f" {match.player1.last_name} vs {match.player2.last_name}")

# Création d'un tournoi avec le round
tournament = Tournament("Test Tournament", "Paris", "01/01/2023", "05/01/2023")
tournament.rounds_list.append(round)

# Conversion du tournoi en JSON et retour
tournament_json = tournament.to_json()
tournament = Tournament.from_json(tournament_json)

print(f"Tournament: {tournament.name}")
for round in tournament.rounds_list:
    print(f" {round.name} Matches:")
    for match in round.matches:
        print(f"  {match.player1.last_name} vs {match.player2.last_name}")
