# /views/player_view.py
from colorama import Fore, Style
from tabulate import tabulate


def display_players(players):
    if len(players) > 0:
        last_player = players[-1]  # Récupérer le dernier joueur ajouté
        player_data = [
            {
                "Nom": last_player.last_name,
                "Prénom": last_player.first_name,
                "Date de naissance": last_player.birthdate,
                "Genre": last_player.gender,
                "Classement": last_player.rank,
                "ChessId": last_player.ChessId
            }
        ]
        headers = {
            "Nom": "Nom",
            "Prénom": "Prénom",
            "Date de naissance": "Date de naissance",
            "Genre": "Genre",
            "Classement": "Classement",
            "ChessId": "ChessId"
        }
        print(Fore.GREEN + tabulate(player_data, headers=headers, tablefmt="fancy_grid"))
        print(Fore.RED + "                        Ce joueur a été ajouté avec succès !" + "\n\n" + Style.RESET_ALL)  # Message en rouge avec deux lignes vides après
    else:
        print("Aucun joueur enregistré.")
