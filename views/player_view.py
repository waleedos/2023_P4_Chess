from tabulate import tabulate
from colorama import Fore, Back, Style

def display_player(player):
    player_info = [
        ["Nom", player.last_name],
        ["Prénom", player.first_name],
        ["Né(e) le", player.date_of_birth],
        ["Score", str(player.score)]
    ]
    print(Fore.GREEN + "************************************")
    print("            CE JOUEUR EST CRÉÉ       ")
    print("************************************")
    print(tabulate(player_info, tablefmt="fancy_grid", numalign="left"))
    print("************************************")
    print(Style.RESET_ALL)

def display_players(players):
    player_data = []
    for player in players:
        player_data.append([
            player.last_name,
            player.first_name,
            player.date_of_birth,
            player.score
        ])

    headers = ["Nom", "Prénom", "Né(e) le", "Score"]
    print(Fore.GREEN + tabulate(player_data, headers=headers, tablefmt="fancy_grid", numalign="left"))
    print(Style.RESET_ALL)
