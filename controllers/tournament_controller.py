import json
from models.tournament import Tournament
from models.player import Player

def create_tournament(name, location, start_date, end_date, time_control, number_of_rounds, current_round_number, players, rounds, description):
    tournament = Tournament(name, location, start_date, end_date, time_control, number_of_rounds, current_round_number, players, rounds, description)
    return tournament

def add_tournament(tournament, file_path='data/tournaments/tournaments.json'):
    tournaments = load_tournaments(file_path)
    tournaments.append(tournament)
    save_tournaments(tournaments, file_path)

def save_tournaments(tournaments, file_path='data/tournaments/tournaments.json'):
    tournament_data = []
    for tournament in tournaments:
        tournament_data.append({
            'name': tournament.name,
            'location': tournament.location,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'time_control': tournament.time_control,
            'number_of_rounds': tournament.number_of_rounds,
            'current_round_number': tournament.current_round_number,
            'players': [player.__dict__ for player in tournament.players],
            'rounds': [round.__dict__ for round in tournament.rounds],
            'description': tournament.description,
        })

    with open(file_path, 'w') as file:
        json.dump(tournament_data, file)

def load_tournaments(file_path='data/tournaments/tournaments.json'):
    tournaments = []
    try:
        with open(file_path, 'r') as file:
            tournament_data = json.load(file)

        for data in tournament_data:
            tournament = Tournament(
                data['name'], data['location'], data['start_date'], data['end_date'], data['time_control'], 
                data['number_of_rounds'], data['current_round_number'], 
                [Player(player['last_name'], player['first_name'], player['date_of_birth'], player['score']) for player in data['players']], 
                [Round(**round) for round in data['rounds']], 
                data['description'])
            tournaments.append(tournament)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return tournaments

def display_tournaments(tournaments):
    for tournament in tournaments:
        print("Tournament Name:", tournament.name)
        print("Location:", tournament.location)
        print("Start Date:", tournament.start_date)
        print("End Date:", tournament.end_date)
        print("Time Control:", tournament.time_control)
        print("Number of Rounds:", tournament.number_of_rounds)
        print("Current Round Number:", tournament.current_round_number)
        print("Players:")
        for player in tournament.players:
            print("- Name:", player.first_name, player.last_name)
            print("  Date of Birth:", player.date_of_birth)
            print("  Score:", player.score)
        print("Rounds:")
        for i, round in enumerate(tournament.rounds):
            print("- Round", i + 1)
            print("  Start Date:", round.start_date)
            print("  End Date:", round.end_date)
            # Print other round details
        print("Description:", tournament.description)
        print()
