class Player:
    def __init__(self, last_name, first_name, birthdate, gender, rank=0, ChessId="", tournament_points=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.ChessId = ChessId
        self.tournament_points = tournament_points


    def __str__(self):
        return f"Nom: {self.last_name}, Prénom: {self.first_name}, Date de naissance: {self.birthdate}, Genre: {self.gender}, Classement: {self.rank}, ChessId: {self.ChessId}"    
    
    
    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "rank": self.rank,
            "ChessId": self.ChessId,
            "tournament_points": self.tournament_points
        }
