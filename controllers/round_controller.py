# Fichier : /controllers/round_controller.py
from models.round import Round
from views.round_view import RoundView
from controllers.match_controller import create_new_match, display_match

def create_new_round(name, player_pairs):
    # Initialiser un nouveau tour avec le nom fourni et une liste de matches vide
    new_round = Round(name)
    
    # Créer un match pour chaque paire de joueurs et l'ajouter à la liste des matches du tour
    for player1, player2 in player_pairs:
        match = create_new_match(player1, player2)
        new_round.matches.append(match)
    
    # Demander à l'utilisateur d'entrer les heures de début et de fin du tour
    RoundView.input_start_and_end_times(new_round)
    
    return new_round

def display_round(round):
    # Afficher le tour à l'aide de la vue correspondante
    RoundView.display_round(round)
    
    # Afficher chaque match du tour
    for match in round.matches:
        display_match(match)