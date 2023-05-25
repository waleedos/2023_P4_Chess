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


def display_all_players(players):
    if len(players) > 0:
        player_data = [
            {
                "Nom": player.last_name,
                "Prénom": player.first_name,
                "Date de naissance": player.birthdate,
                "Genre": player.gender,
                "Classement": player.rank,
                "ChessId": player.ChessId
            } for player in players
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
        print(Fore.RED + "                        Voici tous les joueurs enregistrés!" + "\n\n" + Style.RESET_ALL)
    else:
        print("Aucun joueur enregistré.")


def get_new_player_info():
    last_name = input("Nom : ")
    first_name = input("Prénom : ")
    birthdate = input("Date de naissance (jj/mm/aaaa) : ")
    gender = input("Genre (M ou F) : ")
    rank = int(input("Classement : "))
    ChessId = input("ChessId (AB12345) : ")
    
    player_data = {
        "last_name": last_name,
        "first_name": first_name,
        "birthdate": birthdate,
        "gender": gender,
        "rank": rank,
        "ChessId": ChessId
    }
    
    return player_data


def get_updated_player_info(player):
    last_name = input("Nom [" + player.last_name + "]: ")
    first_name = input("Prénom [" + player.first_name + "]: ")
    birthdate = input("Date de naissance (jj/mm/aaaa) [" + player.birthdate + "]: ")
    gender = input("Genre (M ou F) [" + player.gender + "]: ")
    rank = input("Classement [" + str(player.rank) + "]: ")
    chess_id_new = input("ChessId (AB12345) [" + player.ChessId + "]: ")
    
    new_player_data = {
        "last_name": last_name,
        "first_name": first_name,
        "birthdate": birthdate,
        "gender": gender,
        "rank": rank,
        "ChessId": chess_id_new
    }
    
    return new_player_data


def display_all_players_menu(players):
    if players:
        print("Voici tous les joueurs enregistrés :")
        display_all_players(players)
    else:
        print("Aucun joueur enregistré.")


def display_update_confirmation():
    print(Fore.RED + "\nLes nouvelles informations du joueur ont été prises en compte.\n" + Style.RESET_ALL)


def get_player_id_to_delete():
    chess_id = input("Entrez l'ID du joueur à supprimer (ChessId) : ")
    return chess_id


def display_delete_confirmation():
    print(Fore.RED + "\nLe joueur séléctionné vient d'être supprimé.\n" + Fore.RESET)

