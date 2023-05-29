# Ce fichier Python contient plusieurs fonctions pour interagir avec une base de données utilisant TinyDB, un moteur
# de base de données orienté document léger et simple pour Python. Il sert également à convertir les objets
# sauvegardés sous forme sérialisée en leurs objets originaux.


from pathlib import Path
from tinydb import TinyDB
from tinydb import where
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
# Importation des modules et des classes nécessaires. Path est une classe de pathlib qui est utilisée pour manipuler
# les chemins de fichiers et de dossiers. TinyDB et where sont des modules de TinyDB utilisés pour interagir avec la
# base de données. Les classes Player, Tournament, Round, et Match sont les modèles de données.


def save_db(db_name, serialized_data):
    Path("data/").mkdir(exist_ok=True)
    try:
        db = TinyDB(f"data/{db_name}.json")
    except FileNotFoundError:
        with open(f"data/{db_name}.json", "w"):
            pass
        db = TinyDB("data/" + db_name + ".json")

    db.insert(serialized_data)
    print(f"{serialized_data['name']} sauvegardé avec succès.")
    # Implementation de La fonction save_db prend un nom de base de données et des données sérialisées en entrée.
    # Elle crée d'abord un dossier nommé "data" si celui-ci n'existe pas déjà. Ensuite, elle essaie d'ouvrir la
    # base de données spécifiée. Si la base de données n'existe pas, elle la crée. Ensuite, elle insère les données
    # sérialisées dans la base de données et imprime un message de confirmation.


def update_db(db_name, serialized_data):
    db = TinyDB(f"data/{db_name}.json")
    db.update(
        serialized_data,
        where('name') == serialized_data['name']
    )
    print(f"{serialized_data['name']} modifié avec succès.")
    # Définition de la fonction update_db met à jour un enregistrement existant dans la base de données. Elle
    # recherche l'enregistrement par son nom et met à jour les données correspondantes.


def update_player_rank(db_name, serialized_data):
    db = TinyDB(f"data/{db_name}.json")
    db.update(
            {'rating': serialized_data['rating'], 'total_score': serialized_data['total_score']},
            where('name') == serialized_data['name']
    )
    print(f"{serialized_data['name']} modifié avec succès.")
    # Implementation de la fonction update_player_rank est similaire à update_db, mais elle met uniquement à jour
    # le classement et le score total d'un joueur.


def load_db(db_name):
    if not Path("data/").exists():
        Path("data/").mkdir()
    db = TinyDB(f"data/{db_name}.json")
    return db.all()
    # Création de la fonction load_db charge toutes les données de la base de données spécifiée et les retourne.
    # Elle crée le dossier "data" si celui-ci n'existe pas déjà.


def load_player(serialized_player, load_tournament_score=False):
    player = Player(
        serialized_player["name"],
        serialized_player["firstname"],
        serialized_player["birthday"],
        serialized_player["gender"],
        serialized_player["rating"],
        serialized_player["total_score"],
    )
    if load_tournament_score:
        player.tournament_score = serialized_player["tournament_score"]
    return player
    # Création de la fonction load_player convertit des données sérialisées en un objet Player. Elle peut également
    # charger le score du tournoi d'un joueur si l'option correspondante est activée.


def load_tournament(serialized_tournament):
    loaded_tournament = Tournament(
        serialized_tournament["name"],
        serialized_tournament["location"],
        serialized_tournament["date"],
        serialized_tournament["time_control"],
        [load_player(player, load_tournament_score=True) for player in serialized_tournament["players"]],
        serialized_tournament["rounds_number"],
        serialized_tournament["description"]
    )
    loaded_tournament.rounds = load_rounds(serialized_tournament, loaded_tournament)

    return loaded_tournament
    # La fonction load_tournament convertit des données sérialisées en un objet Tournament. Elle charge également les
    # joueurs du tournoi et les rounds.


def load_rounds(serialized_tournament, tournament):

    loaded_rounds = []

    for rd in serialized_tournament["list_round"]:
        players_pairs = []
        pair_p1 = None
        pair_p2 = None
        for pair in rd["players_pairs"]:
            for player in tournament.players:
                if player.name == pair[0]["name"]:
                    pair_p1 = player
                elif player.name == pair[1]["name"]:
                    pair_p2 = player
            players_pairs.append((pair_p1, pair_p2))
        loaded_round = Round(
            rd["name"],
            players_pairs,
            load_match=True
        )
        loaded_round.matchs = [load_match(match, tournament) for match in rd["matchs"]]
        loaded_round.start_date = rd["start_date"]
        loaded_round.end_date = rd["end_date"]
        loaded_rounds.append(loaded_round)

    return loaded_rounds
    # La fonction load_rounds convertit une liste de données sérialisées en une liste d'objets Round. Pour chaque
    # round, elle charge les paires de joueurs, les matchs, et les dates de début et de fin.


def load_match(serialized_match, tournament):

    player_1 = None
    player_2 = None

    for player in tournament.players:
        if player.name == serialized_match["player_1"]["name"]:
            player_1 = player
        elif player.name == serialized_match["player_2"]["name"]:
            player_2 = player

    loaded_match = Match(player_1, player_2, serialized_match['name'])
    loaded_match.score_player_1 = serialized_match["score_player_1"]
    loaded_match.score_player_2 = serialized_match["score_player_2"]
    loaded_match.winner = serialized_match["winner"]

    return loaded_match
    # La fonction load_match convertit des données sérialisées en un objet Match. Elle charge également les joueurs
    # du match et leur score.
