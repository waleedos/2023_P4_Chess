from models.player import Player

def create_player(last_name, first_name, date_of_birth, score):
    player = Player(last_name, first_name, date_of_birth, score)
    return player
