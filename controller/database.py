# Ce fichier Python contient plusieurs fonctions pour interagir avec une base de données utilisant TinyDB, un moteur
# de base de données orienté document léger et simple pour Python. Il sert également à convertir les objets
# sauvegardés sous forme sérialisée en leurs objets originaux.

from colorama import Fore, Style, init
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

init()


def save_db(db_name, serialized_data):
    # Définition de la fonction save_db avec deux paramètres : db_name (le nom de la base de données à laquelle Nous
    # voulons sauvegarder les données) et serialized_data (les données que nous voulons sauvegarder).
    Path("data/").mkdir(exist_ok=True)
    # La méthode mkdir de la classe Path de la bibliothèque pathlib est utilisée pour créer un répertoire nommé data.
    # L'argument exist_ok=True signifie que si le répertoire existe déjà, aucune exception ne sera levée.
    try:
        db = TinyDB(f"data/{db_name}.json")
        # Dans le bloc try, on tente d'ouvrir une base de données TinyDB existante dans le dossier data avec le nom
        # donné. Si le fichier n'existe pas, une erreur FileNotFoundError sera levée.
    except FileNotFoundError:
        with open(f"data/{db_name}.json", "w"):
            pass
            # Si l'erreur FileNotFoundError est levée (c'est-à-dire si le fichier n'existe pas), le code dans le bloc
            # except sera exécuté. Il crée un nouveau fichier avec le nom donné dans le répertoire data. L'option "w"
            # signifie que le fichier est ouvert en mode écriture. Le mot-clé pass signifie que rien d'autre n'est fait
            # dans ce bloc de code, il est simplement utilisé pour éviter une erreur de syntaxe.
        db = TinyDB("data/" + db_name + ".json")
        # Après la création du nouveau fichier, une nouvelle instance de TinyDB est créée avec le fichier nouvellement
        # créé.

    db.insert(serialized_data)
    # La méthode insert de l'objet db (qui est une instance de TinyDB) est utilisée pour insérer serialized_data dans
    # la base de données.
    print(f"{Fore.BLUE}{serialized_data['name']} sauvegardé avec succès.\n{Style.RESET_ALL}")
    # Enfin, un message de succès est imprimé à l'écran. Il affiche le nom des données sauvegardées en bleu, suivi d'un
    # message indiquant que les données ont été sauvegardées avec succès.

    # Pour conclure, Implementation de La fonction save_db prend un nom de base de données et des données sérialisées
    # en entrée. Elle crée d'abord un dossier nommé "data" si celui-ci n'existe pas déjà. Ensuite, elle essaie d'ouvrir
    # la base de données spécifiée. Si la base de données n'existe pas, elle la crée. Ensuite, elle insère les données
    # sérialisées dans la base de données et imprime un message de confirmation.


def update_db(db_name, serialized_data):
    # Définition de la fonction python update_db. Elle prend deux arguments : db_name qui est le nom de la base de
    # données que vous voulez mettre à jour, et serialized_data qui est le nouvel ensemble de données que nous
    # voulons ajouter à la base de données.
    db = TinyDB(f"data/{db_name}.json")
    # Ouverture de la base de données spécifiée par db_name dans le répertoire "data". Si la base de données n'existe
    # pas encore, TinyDB la créera pour vous. Cette ligne utilise les f-strings de Python pour insérer le nom de la
    # base de données dans le chemin du fichier.
    db.update(
        serialized_data,
        where('name') == serialized_data['name']
        # Utilisation de la méthode update de l'objet db pour mettre à jour les documents de la base de données. Le
        # premier argument de la méthode update est le nouvel ensemble de données que vous voulez ajouter. Le deuxième
        # argument est une condition qui doit être satisfaite pour qu'un document soit mis à jour. Dans ce cas, la
        # condition est que la valeur
    )


def update_player_rank(db_name, serialized_data):
    # Définition de la fonction update_player_rank avec deux paramètres : db_name (le nom de la base de données où se
    # trouvent les données du joueur à mettre à jour) et serialized_data (les données mises à jour que nous voulons
    # enregistrer).
    db = TinyDB(f"data/{db_name}.json")
    # Une instance de TinyDB est créée pour ouvrir la base de données dans le dossier data avec le nom spécifié. Si le
    # fichier n'existe pas, une erreur FileNotFoundError sera levée (bien que cette erreur ne soit pas traitée dans ce
    # morceau de code).
    db.update(
            {'rating': serialized_data['rating'], 'total_score': serialized_data['total_score']},
            where('name') == serialized_data['name']
    )
    # Cette méthode update de l'objet db (qui est une instance de TinyDB) est utilisée pour mettre à jour certaines
    # entrées dans la base de données. Les champs à mettre à jour sont rating et total_score et leurs nouvelles valeurs
    # sont extraites de serialized_data. L'argument where('name') == serialized_data['name'] est une condition qui
    # détermine quels documents (ou entrées) doivent être mis à jour : seuls les documents dont le champ name est égal
    # à serialized_data['name'] seront mis à jour.

    print(f"{serialized_data['name']} {serialized_data['firstname']} modifié avec succès.")
    # Enfin, un message de confirmation est imprimé à l'écran. Il indique le nom et le prénom du joueur qui a été mis à
    # jour avec succès


def load_db(db_name):
    # La fonction load_db est définie avec un paramètre : db_name. C'est le nom de la base de données à partir de
    # laquelle nous voulions charger les données.
    if not Path("data/").exists():
        Path("data/").mkdir()
        # La méthode exists de la classe Path de la bibliothèque pathlib est utilisée pour vérifier si un répertoire
        # nommé data existe déjà. Si ce n'est pas le cas (if not Path("data/").exists()), la méthode mkdir est utilisée
        # pour créer ce répertoire.
    db = TinyDB(f"data/{db_name}.json")
    # Une instance de TinyDB est créée pour ouvrir la base de données dans le dossier data avec le nom spécifié. Si le
    # fichier n'existe pas, une erreur FileNotFoundError sera levée (bien que cette erreur ne soit pas traitée dans ce
    # morceau de code).
    return db.all()
    # La méthode all de l'objet db (qui est une instance de TinyDB) est utilisée pour récupérer tous les documents
    # (c'est-à-dire toutes les entrées) de la base de données. Ces documents sont retournés par la fonction, de sorte
    # que le code qui a appelé la fonction load_db peut les utiliser.


def load_player(serialized_player, load_tournament_score=False):
    # La fonction load_player est définie avec deux paramètres : serialized_player (un dictionnaire contenant des
    # données sur un joueur) et load_tournament_score (un booléen indiquant si le score du tournoi du joueur doit être
    # chargé). Si load_tournament_score n'est pas spécifié lors de l'appel de la fonction, il sera par défaut égal à
    # False.
    player = Player(
        serialized_player["name"],
        serialized_player["firstname"],
        serialized_player["birthday"],
        serialized_player["gender"],
        serialized_player["rating"],
        serialized_player["total_score"],
    )
    # Une nouvelle instance de la classe Player est créée avec des arguments extraits de serialized_player.
    # serialized_player est supposé être un dictionnaire avec les clés "name", "firstname", "birthday", "gender",
    # "rating" et "total_score".

    if load_tournament_score:
        player.tournament_score = serialized_player["tournament_score"]
        # Si load_tournament_score est True, alors le champ tournament_score de l'objet player est défini à partir de
        # serialized_player. serialized_player est supposé avoir une clé "tournament_score".

    return player
    # L'instance de Player qui a été créée et potentiellement modifiée est renvoyée par la fonction.


def load_tournament(serialized_tournament):
    # La fonction load_tournament est définie avec un seul paramètre : serialized_tournament. C'est un dictionnaire
    # contenant des informations sur un tournoi.
    loaded_tournament = Tournament(
        serialized_tournament["name"],
        serialized_tournament["location"],
        serialized_tournament["date"],
        serialized_tournament["time_control"],
        [load_player(player, load_tournament_score=True) for player in serialized_tournament["players"]],
        serialized_tournament["rounds_number"],
        serialized_tournament["description"]
    )
    # Une nouvelle instance de la classe Tournament est créée avec des arguments extraits de serialized_tournament. Le
    # cinquième argument est une liste de joueurs, qui sont chargés à l'aide de la fonction load_player. Pour chaque
    # joueur dans serialized_tournament["players"], load_player est appelé avec player comme premier argument et True
    # comme deuxième argument.

    loaded_tournament.rounds = load_rounds(serialized_tournament, loaded_tournament)
    # Le champ rounds de loaded_tournament est défini en appelant la fonction load_rounds avec serialized_tournament et
    # loaded_tournament comme arguments. Le code de la fonction load_rounds n'est pas fourni, mais on peut supposer
    # qu'elle prend en compte les données d'un tournoi et un objet Tournament, et renvoie les tours de ce tournoi sous
    # une forme appropriée.

    return loaded_tournament
    # L'instance de Tournament qui a été créée et modifiée est renvoyée par la fonction.


def load_rounds(serialized_tournament, tournament):
    # Définition de cette fonction avec deux paramètres : serialized_tournament (un dictionnaire contenant les données
    # d'un tournoi) et tournament (une instance de la classe Tournament).

    loaded_rounds = []
    # Une nouvelle liste vide est créée pour stocker les rounds chargés.

    for rd in serialized_tournament["list_round"]:
        # On parcourt chaque round dans serialized_tournament["list_round"].
        players_pairs = []
        pair_p1 = None
        pair_p2 = None
        # Pour chaque round, on crée une nouvelle liste vide players_pairs pour stocker les paires de joueurs et deux
        # variables pair_p1 et pair_p2 pour stocker temporairement les joueurs de chaque paire.

        for pair in rd["players_pairs"]:
            for player in tournament.players:
                if player.name == pair[0]["name"]:
                    pair_p1 = player
                elif player.name == pair[1]["name"]:
                    pair_p2 = player
            players_pairs.append((pair_p1, pair_p2))
            # Pour chaque paire de joueurs dans le round, on cherche les objets Player correspondants dans
            # tournament.players et on les ajoute à players_pairs.

        loaded_round = Round(
            rd["name"],
            players_pairs,
            load_match=True
        )
        # Une nouvelle instance de la classe Round est créée avec le nom du round, les paires de joueurs et
        # load_match=True comme arguments.

        loaded_round.matchs = [load_match(match, tournament) for match in rd["matchs"]]
        # Les matchs du round sont chargés en utilisant la fonction load_match et sont attribués au champ matchs de
        # loaded_round.

        loaded_round.start_date = rd["start_date"]
        loaded_round.end_date = rd["end_date"]
        # Les dates de début et de fin du round sont extraites de rd et attribuées aux champs start_date et end_date de
        # loaded_round.

        loaded_rounds.append(loaded_round)
        # Le round chargé est ajouté à loaded_rounds.

    return loaded_rounds
    # La liste loaded_rounds, qui contient tous les rounds chargés, est renvoyée par la fonction.


def load_match(serialized_match, tournament):
    # La fonction load_match est définie avec deux paramètres : serialized_match (un dictionnaire contenant des
    # informations sur un match) et tournament (une instance de la classe Tournament).

    player_1 = None
    player_2 = None
    # On initialise deux variables player_1 et player_2 à None. Ces variables seront utilisées pour stocker les objets
    # Player correspondant aux joueurs du match.

    for player in tournament.players:
        if player.name == serialized_match["player_1"]["name"]:
            player_1 = player
        elif player.name == serialized_match["player_2"]["name"]:
            player_2 = player
            # On parcourt chaque joueur dans tournament.players. Si le nom du joueur correspond au nom du premier ou du
            # deuxième joueur du match (tel qu'il est spécifié dans serialized_match), on affecte ce joueur à player_1
            # ou player_2 respectivement.

    loaded_match = Match(player_1, player_2, serialized_match['name'])
    # Une nouvelle instance de la classe Match est créée avec player_1, player_2, et le nom du match extrait de
    # serialized_match comme arguments.

    loaded_match.score_player_1 = serialized_match["score_player_1"]
    loaded_match.score_player_2 = serialized_match["score_player_2"]
    # Les scores du premier et du deuxième joueur du match sont extraits de serialized_match et attribués aux champs
    # score_player_1 et score_player_2 de loaded_match.

    loaded_match.winner = serialized_match["winner"]
    # Le gagnant du match est extrait de serialized_match et attribué au champ winner de loaded_match.

    return loaded_match
    # L'instance de Match qui a été créée et modifiée est renvoyée par la fonction.
