import json
from models.player import Player

def create_player(last_name, first_name, date_of_birth, score):
    player = Player(last_name, first_name, date_of_birth, score)
    return player

def add_player(player, file_path='data/players/players.json'):
    players = load_players(file_path)
    players.append(player)
    save_players(players, file_path)

def save_players(players, file_path='data/players/players.json'):
    player_data = []
    for player in players:
        player_data.append({
            'last_name': player.last_name,
            'first_name': player.first_name,
            'date_of_birth': player.date_of_birth,
            'score': player.score
        })

    with open(file_path, 'w') as file:
        json.dump(player_data, file)

def load_players(file_path='data/players/players.json'):
    players = []
    try:
        with open(file_path, 'r') as file:
            player_data = json.load(file)

        for data in player_data:
            player = Player(data['last_name'], data['first_name'], data['date_of_birth'], data['score'])
            players.append(player)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return players
