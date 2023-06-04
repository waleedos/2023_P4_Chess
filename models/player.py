class Player:
    # déclaration d'une nouvelle classe appelée Player.

    def __init__(self, name, firstname, birthday, gender, rating, total_score):
        # définition de la méthode d'initialisation, qui est une fonction spéciale appelée chaque fois qu'une
        # nouvelle instance de la classe est créée. Les arguments de cette méthode sont utilisés pour initialiser les
        # attributs de l'objet.

        self.name = name
        # initialisation de l'attribut name de l'objet avec la valeur de l'argument name passé à la méthode
        # d'initialisation. et ainsi de suite pour le reste des attributs avec leur valeures de l'argument.
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.rating = rating
        # Initialise l'attribut rating avec la valeur de l'argument rating. Cela pourrait représenter une sorte de
        # classement ou de note pour le joueur.

        self.total_score = total_score
        # Initialise l'attribut total_score avec la valeur de l'argument total_score. Cela représente le
        # score total du joueur dans tous les matchs et tournois auxquels il a participé.

        self.tournament_score = 0
        # Initialise l'attribut tournament_score à 0. Cela représenter le score du joueur dans le tournoi actuel.

        self.played_with = []
        # Initialise l'attribut played_with avec une liste vide. Cela est utilisé pour garder une trace des autres
        # joueurs avec lesquels ce joueur a joué dans le passé.

    def __str__(self):
        # définition de la méthode def __str__(self) qui opère sur une instance de la classe Player, et qui est une
        # représentation spéciale en Python qui retourne une chaîne de caractères.Lorsque vous essayez d'afficher un
        # objet (par exemple avec print(obj)) Python appelle automatiquement cette méthode.

        return f"{self.firstname} {self.name}"
        # la méthode retourne une chaîne formatée qui est une concaténation du prénom et du nom de l'instance du joueur.
        # Donc si nous avons une instance de Player nommée player, alors print(player) affichera quelque chose comme
        # firstname name.

    def get_serialized_player(self):
        # définition de cette methode qui retourne une représentation "sérialisée" de l'instance du joueur. La
        # sérialisation est le processus de transformation des données en une forme qui peut être facilement stockée ou
        # transmise et ensuite reconstruite.

        serialized_player = {
            "name": self.name,
            "firstname": self.firstname,
            "birthday": self.birthday,
            "gender": self.gender,
            "rating": self.rating,
            "total_score": self.total_score,
            "tournament_score": self.tournament_score,
        }
        # Les lignes suivantes définissent un dictionnaire serialized_player qui contient les attributs clés de
        # l'instance du joueur comme name, firstname, birthday, gender, rating, total_score et tournament_score. Chaque
        # paire clé-valeur est une correspondance entre le nom de l'attribut (comme une chaîne) et la valeur actuelle
        # de l'attribut pour l'instance du joueur.

        return serialized_player
        # La méthode retourne le dictionnaire serialized_player. Cela pourrait être utilisé, par exemple, pour stocker
        # les informations sur le joueur dans une base de données ou pour les envoyer sur un réseau.

    def display_all_info(self):
        return f"Name: {self.name}\nFirstname: {self.firstname}\nBirthday: {self.birthday}\nGender: {self.gender}\
            \nRating: {self.rating}\nTotal Score: {self.total_score}\nTournament Score: {self.tournament_score}"
        # Cette méthode retourne une chaîne de caractères qui représente toutes les informations clés de l'instance du
        # joueur. La chaîne de caractères est construite en utilisant une chaîne formatée (c'est-à-dire une chaîne qui
        # contient des marqueurs de position qui seront remplacés par les valeurs des variables). Ici, les informations
        # du joueur sont structurées en plusieurs lignes, chaque ligne contenant le nom de l'attribut suivi de sa
        # valeur.
