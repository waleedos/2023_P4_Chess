# importe la classe View à partir du module view. Cette classe est utilisée pour afficher des informations et
# interagir avec l'utilisateur.
from colorama import Fore, Style, init
from views.view import View


init()


class Match:

    def __init__(self, player_1, player_2, name):
        """
        Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant
        deux éléments : une référence à une instance de joueur et un score.
        Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
        """
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.winner = None
        self.name = name
        # définition de la classe Match : La méthode __init__ est le constructeur de la classe Match. Elle prend
        # les paramètres player_1, player_2 et name et initialise les attributs correspondants de l'objet Match.
        # Les attributs player_1 et player_2 font référence aux instances des joueurs impliqués dans le match.
        # Les attributs score_player_1 et score_player_2 sont initialisés à 0 et représentent les scores des joueurs.
        # L'attribut winner est initialisé à None et représente le gagnant du match. L'attribut name stocke le nom
        # du match.

    def player_winner(self, winner):
        if winner == self.player_1:
            return f"Le gagnant est {self.player_1}"
        if winner == self.player_2:
            return f"Le gagnant est {self.player_2}"
        if winner == 'ex aequo':
            return f"{self.player_1} et {self.player_2} ont fait ex aequo"
        # La méthode player_winner prend le paramètre winner et renvoie une chaîne de caractères indiquant le gagnant
        # du match. Selon la valeur de winner, la méthode retourne différentes chaînes de caractères.

    def play_match(self):
        print()
        winner = View().get_user_entry(
            msg_display=f"{Fore.RED}{self.player_1.firstname} VS {self.player_2.firstname}\n{Style.RESET_ALL}"
                        "\nGagnant ?\n"
                        f"0 - {self.player_1.firstname}\n"
                        f"1 - {self.player_2.firstname}\n"
                        "2 - Égalité\n"
                        ">>> ",
            msg_error=f"\n{Fore.YELLOW}Veuillez entrer 0, 1 ou 2.\n{Style.RESET_ALL}",
            value_type="selection",
            assertions=["0", "1", "2"]
        )

        if winner == "0":
            self.winner = self.player_winner(self.player_1)
            self.score_player_1 += 1
        elif winner == "1":
            self.winner = self.player_winner(self.player_2)
            self.score_player_2 += 1
        elif winner == "2":
            self.winner = self.player_winner('ex aequo')
            self.score_player_1 += 0.5
            self.score_player_2 += 0.5

        self.player_1.tournament_score += self.score_player_1
        self.player_2.tournament_score += self.score_player_2
        # La méthode play_match permet de jouer le match. Elle utilise l'objet View pour afficher un message de match
        # et demande à l'utilisateur de saisir le gagnant. En fonction de l'entrée de l'utilisateur, les scores des
        # joueurs et le gagnant du match sont mis à jour en conséquence. De plus, les scores du tournoi pour les
        # joueurs sont également mis à jour.

    def get_serialized_match(self):
        return {
            "player_1": self.player_1.get_serialized_player(),
            "score_player_1": self.score_player_1,
            "player_2": self.player_2.get_serialized_player(),
            "score_player_2": self.score_player_2,
            "winner": self.winner,
            "name": self.name,
        }
        # La méthode get_serialized_match retourne une version sérialisée du match, sous forme d'un dictionnaire.
        # Les informations des joueurs (player_1 et player_2), les scores des joueurs (score_player_1 et
        # score_player_2), le gagnant du match (winner) et le nom du match (name) sont ajoutés au dictionnaire.
