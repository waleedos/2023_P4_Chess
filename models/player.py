class Player:

    def __init__(self, name, firstname, birthday, gender, rating, total_score):
        self.name = name
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.rating = rating
        self.total_score = total_score
        self.tournament_score = 0
        self.played_with = []

    def __str__(self):
        return f"{self.firstname} {self.name}"

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

        return serialized_player

    def display_all_info(self):
        return f"Name: {self.name}\nFirstname: {self.firstname}\nBirthday: {self.birthday}\nGender: {self.gender}\
            \nRating: {self.rating}\nTotal Score: {self.total_score}\nTournament Score: {self.tournament_score}"
