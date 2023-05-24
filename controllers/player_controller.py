import json

def add_player(player):
    players = load_players()
    players.append(player)
    save_players(players)

def load_players():
    try:
        with open('data/players.json', 'r') as file:
            players_data = json.load(file)
            return players_data["players"]
    except FileNotFoundError:
        return []

def save_players(players):
    data = {"players": players}
    with open('data/players.json', 'w') as file:
        json.dump(data, file, indent=4)
