import json
from models.tournament import Tournament
from views.tournament_view import display_all_tournaments, display_tournament_creation_success, get_new_tournament_info


def load_tournaments():
    try:
        with open('data/tournaments.json', 'r') as file:
            tournaments_data = json.load(file)
            if "tournaments" in tournaments_data and isinstance(tournaments_data["tournaments"], list):
                return [Tournament(**tournament_info) for tournament_info in tournaments_data["tournaments"]]
            else:
                return []
    except FileNotFoundError:
        return []


def save_tournaments(tournaments):
    data = {"tournaments": [tournament.to_dict() for tournament in tournaments]}
    with open('data/tournaments.json', 'w') as file:
        json.dump(data, file, indent=4)


def add_tournament(tournament):
    tournaments = load_tournaments()
    tournaments.append(tournament)
    save_tournaments(tournaments)
    display_tournament_creation_success(tournament)  # Afficher la phrase de confirmation


def create_new_tournament():
    tournament_data = get_new_tournament_info()
    tournament = Tournament(**tournament_data)
    add_tournament(tournament)
    return tournament
