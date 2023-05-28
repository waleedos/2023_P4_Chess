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

        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.rating, reverse=True)

        else:
            sorted_players = []
            score_sorted_players = sorted(self.players, key=lambda x: x.total_score, reverse=True)

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

        first_half_players = sorted_players[len(sorted_players) // 2:]
        second_half_players = sorted_players[:len(sorted_players) // 2]

        players_pairs = []

        for i, player in enumerate(first_half_players):
            a = 0
            while True:
                try:
                    player_2 = second_half_players[i + a]

                except IndexError:
                    player_2 = second_half_players[i]
                    players_pairs.append((player, player_2))

                    player.played_with.append(player_2)
                    player_2.played_with.append(player)
                    break

                if player in player_2.played_with:
                    a += 1
                    continue

                else:
                    players_pairs.append((player, player_2))
                    player.played_with.append(player_2)
                    player_2.played_with.append(player)
                    break

        return players_pairs
        # La méthode create_players_pairs est utilisée pour créer les paires de joueurs pour un tour spécifique
        # (current_round). La méthode utilise une logique complexe pour trier les joueurs en fonction de leur score
        # total et de leur cote. Elle génère ensuite des paires de joueurs en s'assurant qu'ils n'ont pas déjà joué
        # l'un contre l'autre. Les paires de joueurs sont renvoyées sous forme de liste.

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
