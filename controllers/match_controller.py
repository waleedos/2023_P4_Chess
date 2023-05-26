# Fichier : /controllers/match_controller.py
from models.match import Match
from views.match_view import MatchView

def create_new_match(player1, player2):
    # Initialiser un nouveau match avec les deux joueurs
    new_match = Match(player1, player2)
    
    # Demander à l'utilisateur d'entrer les scores pour chaque joueur
    MatchView.input_scores(new_match)
    
    return new_match

def update_match_score(match, player1_score, player2_score):
    # Mettre à jour les scores pour chaque joueur dans le match
    match.score1 = player1_score
    match.score2 = player2_score

def display_match(match):
    # Afficher le match à l'aide de la vue correspondante
    MatchView.display_match(match)