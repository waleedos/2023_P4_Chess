# /controllers/player_controller.py
import json
from models.player import Player
from views.player_view import display_players


def add_player(player_info):
    player = Player(
        last_name=player_info.last_name,
        first_name=player_info.first_name,
        birthdate=player_info.birthdate,
        gender=player_info.gender,
        rank=player_info.rank,
        ChessId=player_info.ChessId
    )
    players = load_players()
    players.append(player)
    save_players(players)
    display_player_table(players)


def load_players():
    try:
        with open('data/players.json', 'r') as file:
            players_data = json.load(file)
            if "players" in players_data and isinstance(players_data["players"], list):
                return [Player(**player_info) for player_info in players_data["players"]]
            else:
                return []
    except FileNotFoundError:
        return []


def save_players(players):
    data = {"players": [player.to_dict() for player in players]}
    with open('data/players.json', 'w') as file:
        json.dump(data, file, indent=4)


def display_player_table(players):
    display_players(players)


def get_player_by_id(chess_id):
    players = load_players()
    for player in players:
        if player.ChessId == chess_id:
            return player
    return None


def update_player(updated_player):
    players = load_players()
    for i, player in enumerate(players):
        if player.ChessId == updated_player.ChessId:
            players[i] = updated_player
            save_players(players)
            return
    print("Le joueur à mettre à jour n'a pas été trouvé.")

