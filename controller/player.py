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
    # La fonction create_player est définie sans arguments. Cette fonction sera utilisée pour créer un nouveau joueur.

    user_entries = CreatePlayer().display_menu()
    # On crée une nouvelle instance de la classe CreatePlayer et on appelle sa méthode display_menu, qui retourne
    # vraisemblablement un dictionnaire contenant des informations saisies par l'utilisateur.

    player = Player(
        user_entries['name'],
        user_entries['firstname'],
        user_entries['birthday'],
        user_entries['gender'],
        user_entries['total_score'],
        user_entries['rating'])
    # On crée une nouvelle instance de la classe Player en utilisant les informations saisies par l'utilisateur.

    serialized_player = player.get_serialized_player()
    # On appelle la méthode get_serialized_player de l'objet player pour obtenir une version sérialisée du joueur.
    # La sérialisation est un processus qui convertit un objet en un format qui peut être facilement stocké ou
    # transmis, puis reconstruit plus tard.

    print(serialized_player)
    # On imprime la version sérialisée du joueur. Cela pourrait être utilisé à des fins de débogage pour s'assurer que
    # la sérialisation a fonctionné correctement.

    save_db("players", serialized_player)
    # On appelle la fonction save_db avec "players" comme nom de la base de données et le joueur sérialisé comme
    # données à enregistrer.

    return player
    # L'instance de Player qui a été créée est renvoyée par la fonction.


def update_rankings(player, rank, score=True):
    # Définition de la fonction update_rankings est définie avec trois paramètres : player (une instance de la classe
    # Player), rank (un entier représentant le nouveau classement du joueur) et score (un booléen indiquant si le score
    # total du joueur doit être mis à jour).

    if score:
        player.total_score += player.tournament_score
        # Si score est True, on ajoute le score du joueur dans le tournoi (player.tournament_score) à son score total
        # (player.total_score).

    player.rating = rank
    # Le classement du joueur (player.rating) est mis à jour avec la nouvelle valeur fournie (rank).

    serialized_player = player.get_serialized_player()
    # On obtient une version sérialisée de l'objet player en appelant sa méthode get_serialized_player.

    update_player_rank("players", serialized_player)
    # On met à jour le classement du joueur dans la base de données en appelant la fonction update_player_rank avec
    # "players" comme nom de la base de données et le joueur sérialisé comme données à mettre à jour.

    print(
        f"Modification du rang de {player.name} {player.firstname}:\n"
        f"{Fore.GREEN}Score total: {player.total_score}\n{Style.RESET_ALL}"
        f"Classement: {player.rating}\n"
    )
    # On imprime un message indiquant que le classement du joueur a été modifié, suivi de son score total et de son
    # nouveau classement. Les couleurs sont utilisées pour mettre en évidence certaines parties du message.

    # EN CONCLUSION,  La fonction update_rankings est définie. Elle prend les paramètres player, rank et score (avec
    # une valeur par défaut de True). Selon la valeur de score, le score du joueur est ajouté à son score total. Le
    # classement du joueur (rating) est mis à jour avec la valeur rank. L'objet Player est sérialisé en utilisant la
    # méthode get_serialized_player() et le classement du joueur est mis à jour dans la base de données à l'aide de la
    # fonction update_player_rank du module database. Finalement, une confirmation de la modification est affichée
    # avec le nom du joueur, son score total et son classement.


def display_players(sort_by="name", ascending=True):
    # La fonction display_players est définie avec deux arguments facultatifs : sort_by (le critère de tri des joueurs,
    # par défaut le nom) et ascending (un booléen indiquant si le tri doit être ascendant ou descendant, par défaut
    # ascendant).

    players = load_db("players")  # Charger les données des joueurs de la base de données.
    # On charge les données des joueurs à partir de la base de données "players" en utilisant la fonction load_db.

    def key_func_name(player):
        return player['name']

    def key_func_rank(player):
        return player['rank']
    # Deux fonctions clés pour le tri sont définies : key_func_name trie par nom de joueur, key_func_rank trie par
    # classement de joueur.

    if sort_by == "name":
        key_func = key_func_name
    elif sort_by == "rank":
        key_func = key_func_rank
    else:
        key_func = None
        # Selon la valeur de sort_by, on sélectionne la fonction clé appropriée. Si sort_by n'est ni "name" ni "rank",
        # key_func est défini à None, ce qui signifie que les joueurs ne seront pas triés.

    if key_func:
        sorted_players = sorted(players, key=key_func, reverse=not ascending)
    else:
        sorted_players = players
        # Si une fonction clé a été sélectionnée, on trie les joueurs en utilisant cette fonction clé. La valeur de
        # reverse est l'opposée de ascending, ce qui signifie que si ascending est True, reverse est False, et vice
        # versa. Si aucune fonction clé n'a été sélectionnée, sorted_players est simplement une copie de players.

    table = [["Name", "First Name", "Birthday", "Gender", "Rating", "Total Score"]]
    # On crée une liste table qui contiendra toutes les lignes de la table à afficher. La première ligne de la table
    # est une liste de noms de colonnes ou entetes.

    for player in sorted_players:
        table.append([
            player.get('name', 'N/A'),
            player.get('firstname', 'N/A'),
            player.get('birthday', 'N/A'),
            player.get('gender', 'N/A'),
            player.get('rating', 'N/A'),
            player.get('total_score', 'N/A')]
            )
        # Pour chaque joueur dans sorted_players, on ajoute une nouvelle ligne à table. Chaque ligne est une liste de
        # valeurs extraites du dictionnaire du joueur, avec 'N/A' comme valeur par défaut si la clé n'est pas présente.

    print(tabulate(table, headers="firstrow", tablefmt="pipe"))  # print the table
    # Enfin, on utilise la fonction tabulate pour convertir table en une chaîne de caractères formatée comme une table,
    # puis on imprime cette chaîne. Le premier argument de tabulate est la liste de lignes à inclure dans la table. Le
    # second argument, headers, est défini à "firstrow", ce qui signifie que la première ligne de table sera utilisée
    # comme en-tête de la table. Le troisième argument, tablefmt, est défini à "pipe", ce qui signifie que les lignes
    # et les colonnes de la table seront séparées par des barres verticales (|).
