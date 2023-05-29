# importation de la classe Round du module round situé dans le dossier models
from models.round import Round

# Définition de La variable ROUNDS_NUMBER avec la valeur 4. Elle représente le nombre de tours par défaut pour le
# tournoi.
ROUNDS_NUMBER = 4


class Tournament:
    def __init__(self, name, location, date, time_control, players, rounds_number=ROUNDS_NUMBER, description=""):
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.players = players
        self.rounds_number = rounds_number
        self.description = description
        self.list_round = []
        """
        Création de la classe "Tournament" avec le constructeur __init__. Il prend les paramètres name, location,
        date, time_control, players, rounds_number et description. Les attributs de l'objet Tournament sont
        initialisés avec les valeurs correspondantes fournies en paramètre. La liste list_round est initialisée
        comme une liste vide.
        """

    def __str__(self):
        return f"{self.name} qui a eu lieu le {self.date}"
        # Utilisation de La méthode __str__ est une méthode spéciale qui est appelée lorsque l'objet Tournament est
        # converti en une représentation sous forme de chaîne de caractères. Elle retourne une chaîne formatée avec
        # le nom du tournoi et la date.

    def create_round(self, round_number):
        players_pairs = self.create_players_pairs(current_round=round_number)
        round = Round("Round " + str(round_number + 1), players_pairs)
        self.list_round.append(round)
        # Définition de La méthode create_round qui est utilisée pour créer un nouveau tour (Round) dans le tournoi.
        # Elle prend le paramètre round_number qui représente le numéro du tour actuel. La méthode utilise la méthode
        # create_players_pairs pour créer les paires de joueurs pour le tour actuel, puis crée un nouvel objet Round
        # en utilisant la classe Round importée précédemment. Le nouvel objet Round est ajouté à la liste list_round
        # du tournoi.

    def create_players_pairs(self, current_round):
        # définit la fonction create_players_pairs, qui prend deux paramètres : l'instance actuelle (représentée par
        # self) et le round actuel (current_round).

        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.rating, reverse=True)
            # Si nous sommes au premier tour (current_round est 0), la liste des joueurs est triée par classement
            # (rating) en ordre décroissant.

        else:
            sorted_players = []
            score_sorted_players = sorted(self.players, key=lambda x: x.total_score, reverse=True)
            # Si nous ne sommes pas au premier tour, une nouvelle liste vide sorted_players est créée, et les joueurs
            # sont triés par leur score total (total_score) en ordre décroissant.

            for i, player in enumerate(score_sorted_players):
                try:
                    sorted_players.append(player)
                except player.total_score == score_sorted_players[i + 1].total_score:
                    if player.rating > score_sorted_players[i + 1].rating:
                        hi_player = player
                        lo_player = score_sorted_players[i + 1]
                    else:
                        hi_player = score_sorted_players[i + 1]
                        lo_player = player
                    sorted_players.append(hi_player)
                    sorted_players.append(lo_player)
                except IndexError:
                    sorted_players.append(player)
                    # Cela parcourt chaque joueur dans la liste triée par score. Si deux joueurs ont le même score
                    # total, le joueur avec le classement le plus élevé est ajouté en premier à la liste
                    # sorted_players. Cela garantit que les joueurs avec le même score total sont classés par
                    # classement.

        first_half_players = sorted_players[len(sorted_players) // 2:]
        second_half_players = sorted_players[:len(sorted_players) // 2]
        # Les joueurs sont ensuite divisés en deux moitiés : la première moitié (first_half_players) et la seconde
        # moitié (second_half_players).

        players_pairs = []
        # Une nouvelle liste vide players_pairs est créée pour stocker les paires de joueurs.

        for i, player in enumerate(first_half_players):
            a = 0
            while True:
                try:
                    player_2 = second_half_players[i + a]
                    # Pour chaque joueur de la première moitié, un autre joueur de la seconde moitié est choisi pour
                    # former une paire. Si le joueur choisi a déjà joué avec le joueur actuel, un autre joueur de la
                    # seconde moitié est choisi.

                except IndexError:
                    player_2 = second_half_players[i]
                    players_pairs.append((player, player_2))

                    player.played_with.append(player_2)
                    player_2.played_with.append(player)
                    break
                    # Si un IndexError est déclenché (ce qui signifie que nous avons dépassé les limites de la liste
                    # second_half_players), le joueur initial de la seconde moitié est choisi, et une paire est formée
                    # et ajoutée à la liste players_pairs. Chaque joueur est ensuite ajouté à la liste des joueurs
                    # avec lesquels l'autre joueur a joué.

                if player in player_2.played_with:
                    a += 1
                    continue
                    # Si le joueur de la première moitié a déjà joué avec le joueur de la seconde moitié, un autre
                    # joueur est choisi dans la seconde moitié.

                else:
                    players_pairs.append((player, player_2))
                    player.played_with.append(player_2)
                    player_2.played_with.append(player)
                    break
                    # Si le joueur de la première moitié n'a pas joué avec le joueur de la seconde moitié, une paire
                    # est formée et ajoutée à la liste players_pairs. Chaque joueur est ensuite ajouté à la liste des
                    # joueurs avec lesquels l'autre joueur a joué.

        return players_pairs
        # Enfin, la liste players_pairs contenant toutes les paires de joueurs est renvoyée.
        # Pour conclusion, La méthode create_players_pairs est utilisée pour créer les paires de joueurs pour un tour
        # spécifique (current_round). La méthode utilise une logique complexe pour trier les joueurs en fonction de
        # leur score total et de leur cote. Elle génère ensuite des paires de joueurs en s'assurant qu'ils n'ont pas
        # déjà joué l'un contre l'autre. Les paires de joueurs sont renvoyées sous forme de liste.

    def get_rankings(self, by_score=True):

        if by_score:
            sorted_players = sorted(self.players, key=lambda x: x.tournament_score, reverse=True)
        else:
            sorted_players = sorted(self.players, key=lambda x: x.rank, reverse=True)

        return sorted_players
        # Nous implémentons La méthode get_rankings pour etre utilisée pour obtenir le classement des joueurs dans le
        # tournoi. Elle prend le paramètre optionnel by_score, qui détermine si le classement est basé sur le score du
        # tournoi (True par défaut) ou sur le classement du joueur. Les joueurs sont triés en fonction du critère
        # choisi et renvoyés sous forme de liste.

    def get_serialized_tournament(self, save_rounds=False):

        serialized_tournament = {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "time_control": self.time_control,
            "players": [player.get_serialized_player() for player in self.players],
            "rounds_number": self.rounds_number,
            "list_round": [rd.get_serialized_round() for rd in self.list_round],
            "description": self.description
        }

        if save_rounds:
            serialized_tournament["list_round"] = [round.get_serialized_round() for round in self.list_round]

        return serialized_tournament
        # Nous utilisons enfin La méthode get_serialized_tournament qui retourne une version sérialisée du tournoi,
        # sous forme d'un dictionnaire. Les attributs du tournoi tels que name, location, date, time_control,
        # players, rounds_number et description sont ajoutés au dictionnaire. De plus, si le paramètre save_rounds
        # est True, les rounds (list_round) sont également sérialisés en utilisant la méthode get_serialized_round()
        # sur chaque objet Round dans la liste list_round.
