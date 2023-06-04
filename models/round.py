from colorama import Fore, Style, init
from utils.timestamp import get_timestamp
from models.match import Match

init()


class Round:
    def __init__(self, name, players_pairs, load_match=False):
        # définition de la méthode spéciale __init__ qui est le constructeur appelée lorsqu'un nouvel objet de la
        # classe Round est créé. Elle initialise les attributs de l'objet Round. Les paramètres de la méthode __init__
        # sont self (qui fait référence à l'instance de l'objet Round lui-même), name (le nom du tour), players_pairs
        # (une liste de paires de joueurs) et load_match (une valeur booléenne optionnelle qui indique si les matchs
        # doivent être chargés ou non).

        self.name = name
        # Assignation de la valeur du paramètre name à l'attribut name de l'objet Round.

        self.players_pairs = players_pairs
        # Assignation de la valeur du paramètre players_pairs à l'attribut players_pairs de l'objet Round.

        if load_match:
            # Vérification de si load_match est évalué à True.

            self.matchs = []
            # Si load_match est évalué à True, cette ligne initialise l'attribut matchs de l'objet Round en tant que
            # liste vide.

        else:
            # Si load_match est évalué à False, cette ligne est exécutée.

            self.matchs = self.create_matchs()
            # Appel de la méthode create_matchs() pour créer les matchs du tour et assigne le résultat à l'attribut
            # matchs de l'objet Round.

        self.start_date = get_timestamp()
        # Assignation de la valeur de l'appel de la fonction get_timestamp() à l'attribut start_date de l'objet Round.
        # Il s'agit eb fait d'une fonction qui renvoie la date et l'heure actuelles.

        self.end_date = None
        # Assignation de la valeur None à l'attribut end_date de l'objet Round, indiquant que la date de fin n'a pas
        # encore été définie.

    def __str__(self):
        # Création de la méthode spéciale __str__ qui est appelée lorsqu'une représentation en chaîne de caractères de
        # l'objet Round est demandée. Elle renvoie simplement le nom du tour.

        return self.name
        # Renvoie le nom du tour

    def create_matchs(self):
        # définit une méthode create_matchs qui est utilisée pour créer les matchs du tour. Elle ne prend pas de
        # paramètres autres que self, qui fait référence à l'instance de l'objet Round lui-même.

        matchs = []
        # Initialisation d'une liste vide appelée matchs

        for i, players in enumerate(self.players_pairs):
            # Itèration sur les paires de joueurs (players) dans l'attribut players_pairs de l'objet Round. L'index de
            # l'itération est également stocké dans la variable i.

            matchs.append(Match(players[0], players[1], f"Match {i}"))
            # création d'un nouvel objet Match en utilisant les joueurs de la paire actuelle et un nom de match généré
            # dynamiquement. Cet objet Match est ensuite ajouté à la liste matchs.

        return matchs
        # Renvoie la liste des matchs créés

    def mark_as_complete(self):
        # définit une méthode mark_as_complete qui est utilisée pour marquer le tour comme terminé.

        self.end_date = get_timestamp()
        # Assignation de la valeur de l'appel de la fonction get_timestamp() à l'attribut end_date de l'objet Round.
        # Cela enregistre la date de fin du tour.

        print(f"{Fore.BLUE}{self.end_date} : {self.name} terminé.\n{Style.RESET_ALL}")
        print(" Rentrez les résultats des matchs:")
        # Affichage de la date de fin du tour et son nom dans la console avec une mise en forme en bleu avec
        # l'affichage d'un message dans la console demandant à l'utilisateur d'entrer les résultats des matchs.

        for match in self.matchs:
            # Itèration sur les matchs de l'objet Round.

            match.play_match()
            # Appel de la méthode play_match() de chaque objet Match pour permettre à l'utilisateur d'entrer les
            # résultats du match.

    def get_serialized_round(self):
        # Définition de la méthode get_serialized_round qui est utilisée pour obtenir une représentation sérialisée du
        # tour.

        ser_players_pairs = []
        # Initialisation d'une liste vide appelée ser_players_pairs.

        for pair in self.players_pairs:
            #  Itèration sur les paires de joueurs (pair) dans l'attribut players_pairs de l'objet Round.

            ser_players_pairs.append(
                (
                    pair[0].get_serialized_player(),
                    pair[1].get_serialized_player()
                    # Création d'un tuple contenant les représentations sérialisées des joueurs de la paire actuelle en
                    # appelant la méthode get_serialized_player() de chaque joueur.
                 )
            )
        return {
            "name": self.name,
            "players_pairs": ser_players_pairs,
            "matchs": [match.get_serialized_match() for match in self.matchs],
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
        # Renvoie un dictionnaire contenant les informations sérialisées du tour, y compris le nom, les paires de
        # joueurs, les matchs, les dates de début et de fin.
