from datetime import datetime

class Player:
    def __init__(self, last_name, first_name, date_of_birth, score):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y").strftime("%d/%m/%Y")
        self.score = score
