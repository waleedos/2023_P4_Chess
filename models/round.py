from colorama import Fore, Style, init

# importation de la fonction get_timestamp du module timestamp situé dans le dossier utils. Cette fonction est
# utilisée pour obtenir le timestamp actuel.
from utils.timestamp import get_timestamp

# importation de la classe Match du module match situé dans le dossier models.
from models.match import Match

init()


class Round:
    def __init__(self, name, players_pairs, load_match=False):

        self.name = name
        self.players_pairs = players_pairs

        if load_match:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

        self.start_date = get_timestamp()
        self.end_date = None
        # Définition de la class "Round" avec La méthode __init__ qui est le constructeur de la classe Round. Elle
        # prend les paramètres name, players_pairs et load_match. L'attribut name est initialisé avec la valeur de
        # name fournie en paramètre. L'attribut players_pairs est initialisé avec la valeur de players_pairs fournie
        # en paramètre. L'attribut load_match est utilisé pour déterminer si les matchs doivent être chargés (dans
        # le cas où un tour précédent est en cours) ou créés à partir des paires de joueurs. En fonction de la valeur
        # de load_match, les matchs sont initialisés soit comme une liste vide ([]) soit à partir de la méthode
        # create_matchs(). Les attributs start_date et end_date sont initialisés à l'aide de la fonction
        # get_timestamp(). L'attribut end_date est initialement défini sur None

    def __str__(self):
        return self.name
        # La méthode __str__ est une méthode spéciale qui est appelée lorsque l'objet Round est converti en une
        # représentation sous forme de chaîne de caractères. Elle retourne simplement la valeur de l'attribut name.

    def create_matchs(self):
        matchs = []

        for i, players in enumerate(self.players_pairs):
            matchs.append(Match(players[0], players[1], f"Match {i}"))
        return matchs
        # La méthode create_matchs est utilisée pour créer les matchs à partir des paires de joueurs (players_pairs).
        # Elle itère sur les paires de joueurs et crée un nouvel objet Match en utilisant la classe Match importée
        # précédemment. Les objets Match sont ajoutés à la liste matchs. Finalement, la méthode retourne la liste
        # matchs.

    def mark_as_complete(self):
        self.end_date = get_timestamp()
        print(f"{Fore.BLUE}{self.end_date} : {self.name} terminé.\n{Style.RESET_ALL}")
        print(" Rentrez les résultats des matchs:")
        for match in self.matchs:
            match.play_match()
        # Cette méthode mark_as_complete est utilisée pour marquer le tour comme terminé. Elle met à jour l'attribut
        # end_date en utilisant la fonction get_timestamp() pour obtenir la date de fin actuelle. Ensuite, elle
        # affiche un message indiquant la date de fin et le nom du tour. Elle invite ensuite l'utilisateur à saisir
        # les résultats des matchs en appelant la méthode play_match() sur chaque objet Match dans la liste matchs.

    def get_serialized_round(self):
        ser_players_pairs = []
        for pair in self.players_pairs:
            ser_players_pairs.append(
                (
                    pair[0].get_serialized_player(),
                    pair[1].get_serialized_player()
                 )
            )
        return {
            "name": self.name,
            "players_pairs": ser_players_pairs,
            "matchs": [match.get_serialized_match() for match in self.matchs],
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
        # Nous utilisons cette méthode get_serialized_round car elle retourne une version sérialisée du tour, sous
        # forme d'un dictionnaire. Les paires de joueurs (players_pairs) sont sérialisées en utilisant les méthodes
        # get_serialized_player() sur chaque joueur. Les matchs (matchs) sont sérialisés en utilisant la méthode
        # get_serialized_match() sur chaque objet Match. Le dictionnaire résultant contient les attributs name,
        # players_pairs, matchs, start_date et end_date du tour.
