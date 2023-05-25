# player_controller.Player
 
import json
from models.player import Player
from views.player_view import display_players


def add_player(player):
    players = load_players()
    players.append(player)
    save_players(players)
    display_players(players)


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


def create_new_player(player_data):
    player = Player(**player_data)
    add_player(player)


def edit_existing_player(chess_id, new_player_data):
    player = get_player_by_id(chess_id)
    
    if new_player_data["last_name"] != "":
        player.last_name = new_player_data["last_name"]
    if new_player_data["first_name"] != "":
        player.first_name = new_player_data["first_name"]
    if new_player_data["birthdate"] != "":
        player.birthdate = new_player_data["birthdate"]
    if new_player_data["gender"] != "":
        player.gender = new_player_data["gender"]
    if new_player_data["rank"] != "":
        player.rank = int(new_player_data["rank"])
    if new_player_data["ChessId"] != "":
        player.ChessId = new_player_data["ChessId"]
    
    update_player(player)


def delete_player(chess_id):
    players = load_players()
    for i, player in enumerate(players):
        if player.ChessId == chess_id:
            del players[i]
            save_players(players)
            return
    print("Le joueur à supprimer n'a pas été trouvé.")

