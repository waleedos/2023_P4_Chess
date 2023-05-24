# Fichier : /views/player_view.py

def display_players(players):
    if len(players) > 0:
        last_player = players[-1]  # Récupérer le dernier joueur ajouté
        print("Liste des joueurs :")
        print("═════════════════════════")
        print(f"Nom             : {last_player.last_name}")
        print(f"Prénom          : {last_player.first_name}")
        print(f"Date de naissance       : {last_player.birthdate}")
        print(f"Genre           : {last_player.gender}")
        print(f"Classement      : {last_player.rank}")
        print(f"ChessId         : {last_player.ChessId}")
        print("═════════════════════════")
    else:
        print("Aucun joueur enregistré.")
