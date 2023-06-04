from colorama import Fore, Style, init
from views.view import View

init()


class Match:
    # Déclaration d'une classe appelée Match.

    def __init__(self, player_1, player_2, name):
        # On définit la méthode __init__, qui est la méthode d'initialisation de la classe. Elle est appelée lorsque
        # vous créez une nouvelle instance de la classe. Elle prend quatre paramètres : self, player_1, player_2
        # et name.

        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.winner = None
        self.name = name
        # Ces lignes initialisent les attributs de la classe. self.player_1 et self.player_2 représentent les joueurs
        # du match, self.score_player_1 et self.score_player_2 représentent les scores de chaque joueur pour ce match,
        # self.winner représentera le gagnant du match, et self.name est le nom du match.

    def player_winner(self, winner):
        # Déclaration de la méthode player_winner prend en paramètre self et winner : winner comme comme arguments qui
        # est supposé être le gagnant d'un match et self fait référence à l'instance actuelle de la classe

        if winner == self.player_1:
            return f"Le gagnant est {self.player_1}"
            # vérification de si winner est le même que self.player_1. Si c'est le cas, cela signifie que player_1 est
            # le gagnant du match. / si cela est est vraie, cette ligne renvoie une chaîne formatée qui dit "Le gagnant
            # est {self.player_1}", où {self.player_1} serait remplacé par la représentation de l'objet player_1.

        if winner == self.player_2:
            return f"Le gagnant est {self.player_2}"
            # vérifie si winner est le même que self.player_2. Si c'est le cas, cela signifie que player_2 est le
            # gagnant du match. et si Si cette condition est vraie, alors renvoie d'une chaîne formatée qui dit
            # "Le gagnant est {self.player_2}", où {self.player_2} serait remplacé par la représentation de l'objet
            # player_2.

        if winner == 'ex aequo':
            return f"{self.player_1} et {self.player_2} ont fait ex aequo"
            # vérifie si winner est égal à la chaîne 'ex aequo', ce qui signifie que le match s'est terminé par une
            # égalité. Si cette condition est vraie, alors renvoi d'une chaîne formatée qui dit "{self.player_1} et
            # {self.player_2} ont fait ex aequo", indiquant que les deux joueurs ont terminé le match à égalité.

    def play_match(self):
        # définition de la méthode play_match. Le paramètre self fait référence à l'instance actuelle de la classe
        # Match.

        print()

        winner = View().get_user_entry(
            # utilisation de l'objet View qui est une class importée depuis le fichier /views/view.py pour demander une
            # entrée à l'utilisateur. L'entrée de l'utilisateur est ensuite affectée à la variable winner.

            # Les lignes suivantes fournissent le message affiché à l'utilisateur et les options qu'il peut choisir :
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
        # message d'erreur qui est affiché si l'utilisateur n'entre pas une valeur valide : 0, 1, ou 2.

        if winner == "0":
            self.winner = self.player_winner(self.player_1)
            self.score_player_1 += 1
            # Vérification de si l'utilisateur a entré "0", ce qui signifie que le premier joueur a gagné, donc si
            # c'est le cas alors on appelle la méthode player_winner avec self.player_1 comme argument et affecte le
            # résultat à self.winner. et donc le score du premier joueur est augmenté de 1.

        elif winner == "1":
            self.winner = self.player_winner(self.player_2)
            self.score_player_2 += 1
            # Nous faisons exactement la meme chose, mais pour le joueur N°2

        elif winner == "2":
            self.winner = self.player_winner('ex aequo')
            self.score_player_1 += 0.5
            self.score_player_2 += 0.5
            # si le match s'est soldé par une égalité (auquel cas chaque joueur reçoit un demi-point).

        self.player_1.tournament_score += self.score_player_1
        self.player_2.tournament_score += self.score_player_2
        # ajout du score du match au score du tournoi du premier et deuxieme joueur.

    def get_serialized_match(self):
        # définition de la méthode get_serialized_match. avec le paramètre self pour faire référence à l'instance
        # actuelle de la classe.

        return {
            # définition d'un dictionnaire Python qui sera renvoyé par la méthode. et pour rappel, Les dictionnaires
            # Python sont des collections de paires clé-valeur.

            "player_1": self.player_1.get_serialized_player(),
            # Ajout d'une entrée au dictionnaire avec la clé "player_1". La valeur associée est le résultat de l'appel
            # de la méthode get_serialized_player() sur l'objet player_1 de l'instance actuelle. Cela suggère que les
            # objets Player ont également une méthode pour se préparer à la sérialisation.

            "score_player_1": self.score_player_1,
            # Ajoute une entrée au dictionnaire avec la clé "score_player_1". La valeur associée est le score du
            # premier joueur dans le match.

            "player_2": self.player_2.get_serialized_player(),
            "score_player_2": self.score_player_2,
            # Similaires aux deux premières, mais concernent le deuxième joueur du match.

            "winner": self.winner,
            "name": self.name,
        }
        # fermeture du dictionnaire.

        # Lorsque cette méthode est appelée, elle renvoie un dictionnaire contenant des informations sur l'instance
        # actuelle de Match. Cela pourrait être utile pour sauvegarder l'état actuel du match etc.
