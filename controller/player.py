from colorama import Fore, Style, init
from tabulate import tabulate

# Importation des 2 fonctions save_db et update_player_rank du module database situé dans le dossier controller.
from controller.database import save_db, update_player_rank, load_db


# Importation de la classe Player du module player situé dans le dossier models.
from models.player import Player

# Importation de la classe CreatePlayer du module player situé dans le dossier views.
from views.player import CreatePlayer

init()


def create_player():
    user_entries = CreatePlayer().display_menu()
    player = Player(
        user_entries['name'],
        user_entries['firstname'],
        user_entries['birthday'],
        user_entries['gender'],
        user_entries['total_score'],
        user_entries['rating'])
    serialized_player = player.get_serialized_player()
    print(serialized_player)
    save_db("players", serialized_player)
    return player
    # Définition de la fonction create_player qui utilise l'objet CreatePlayer pour afficher un menu permettant à
    # l'utilisateur de saisir les informations d'un joueur. En utilisant les entrées de l'utilisateur, un nouvel objet
    # Player est créé en utilisant la classe Player importée précédemment. L'objet Player est sérialisé en utilisant
    # la méthode get_serialized_player() et sauvegardé dans la base de données à l'aide de la fonction save_db du
    # module database. Finalement, l'objet Player est renvoyé.


def update_rankings(player, rank, score=True):
    if score:
        player.total_score += player.tournament_score
    player.rating = rank
    serialized_player = player.get_serialized_player()
    update_player_rank("players", serialized_player)
    print(
        f"Modification du rang de {player.name} {player.firstname}:\n"
        f"{Fore.GREEN}Score total: {player.total_score}\n{Style.RESET_ALL}"
        f"Classement: {player.rating}\n"
    )
    # La fonction update_rankings est définie. Elle prend les paramètres player, rank et score (avec une valeur par
    # défaut de True). Selon la valeur de score, le score du joueur est ajouté à son score total. Le classement du
    # joueur (rating) est mis à jour avec la valeur rank. L'objet Player est sérialisé en utilisant la méthode
    # get_serialized_player() et le classement du joueur est mis à jour dans la base de données à l'aide de la
    # fonction update_player_rank du module database. Finalement, une confirmation de la modification est affichée
    # avec le nom du joueur, son score total et son classement.


"""def display_players():
    players = load_db("players")  # Charger les données des joueurs de la base de données.
    for serialized_player in players:  # Parcourir chaque joueur sérialisé dans les données chargées.
        player = load_player(serialized_player)  # Désérialiser le joueur.
        print(player.display_all_info())  # Afficher toutes les informations du joueur."""


def display_players(sort_by="name", ascending=True):
    players = load_db("players")  # Charger les données des joueurs de la base de données.

    def key_func_name(player):
        return player['name']

    def key_func_rank(player):
        return player['rank']

    if sort_by == "name":
        key_func = key_func_name
    elif sort_by == "rank":
        key_func = key_func_rank
    else:
        key_func = None

    if key_func:
        sorted_players = sorted(players, key=key_func, reverse=not ascending)
    else:
        sorted_players = players

    table = [["Name", "First Name", "Birthday", "Gender", "Rating", "Total Score"]]  # Column names

    for player in sorted_players:
        table.append([
            player.get('name', 'N/A'),
            player.get('firstname', 'N/A'),
            player.get('birthday', 'N/A'),
            player.get('gender', 'N/A'),
            player.get('rating', 'N/A'),
            player.get('total_score', 'N/A')]
            )

    print(tabulate(table, headers="firstrow", tablefmt="pipe"))  # print the table
