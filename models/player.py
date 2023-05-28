class Player:
    # Création de la class "joueur" classe représente un joueur avec des informations telles que le nom, le prénom,
    # la date de naissance, le sexe, le score total, la cote, le score du tournoi et les personnes avec lesquelles
    # le joueur a joué

    def __init__(self, name, firstname, birthday, gender, rating, total_score):
        self.name = name
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.rating = rating
        self.total_score = total_score
        self.tournament_score = 0
        self.played_with = []
        # La définition de cette méthode __init__ est le constructeur de la classe. Elle est appelée lorsqu'un nouvel
        # objet Player est créé. Elle prend les paramètres name, firstname, birthday, gender, rating et total_score
        # et initialise les attributs correspondants de l'objet Player. De plus, elle initialise tournament_score à 0
        # et played_with à une liste vide

    def __str__(self):
        return f"{self.firstname} {self.name}"
        # La méthode __str__ est une méthode spéciale qui est appelée lorsque l'objet Player est converti en une
        # représentation sous forme de chaîne de caractères. Elle retourne une chaîne de la forme "prénom nom".

    def get_serialized_player(self):
        serialized_player = {
            "name": self.name,
            "firstname": self.firstname,
            "birthday": self.birthday,
            "gender": self.gender,
            "rating": self.rating,
            "total_score": self.total_score,
            "tournament_score": self.tournament_score,
        }
        # La méthode get_serialized_player retourne une version sérialisée du joueur, sous forme d'un dictionnaire.
        # Les différentes informations du joueur (nom, prénom, date de naissance, sexe, cote, score total, score du
        # tournoi) sont ajoutées au dictionnaire serialized_player, puis ce dictionnaire est renvoyé.

        return serialized_player
