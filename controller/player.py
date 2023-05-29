# Importation des 2 fonctions save_db et update_player_rank du module database situé dans le dossier controller.
from controller.database import save_db, update_player_rank

# Importation de la classe Player du module player situé dans le dossier models.
from models.player import Player

# Importation de la classe CreatePlayer du module player situé dans le dossier views.
from views.player import CreatePlayer


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
    print(serialized_player['name'])
    update_player_rank("players", serialized_player)
    print(f"Modification du rang de {player}:\nScore total: {player.total_score}\nClassement: {player.rating}")
    # La fonction update_rankings est définie. Elle prend les paramètres player, rank et score (avec une valeur par
    # défaut de True). Selon la valeur de score, le score du joueur est ajouté à son score total. Le classement du
    # joueur (rating) est mis à jour avec la valeur rank. L'objet Player est sérialisé en utilisant la méthode
    # get_serialized_player() et le classement du joueur est mis à jour dans la base de données à l'aide de la
    # fonction update_player_rank du module database. Finalement, une confirmation de la modification est affichée
    # avec le nom du joueur, son score total et son classement.
