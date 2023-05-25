from controllers.player_controller import add_player, load_players
from models.player import Player
from colorama import init, Fore, Style  # Assurez-vous que cette ligne est présente
from views.player_view import display_all_players

# Ajout d'un joueur
def add_new_player():
    last_name = input("Nom : ")
    first_name = input("Prénom : ")
    birthdate = input("Date de naissance (jj/mm/aaaa) : ")
    gender = input("Genre (M ou F) : ")
    rank = int(input("Classement : "))
    ChessId = input("ChessId (AB12345) : ")
    
    player_data = {
        "last_name": last_name,
        "first_name": first_name,
        "birthdate": birthdate,
        "gender": gender,
        "rank": rank,
        "ChessId": ChessId
    }
    
    player = Player(**player_data)  # Création d'une instance de la classe Player
    add_player(player)


# Menu principal
def main_menu():
    init()  # Initialisation de colorama
    print("===== MENU PRINCIPAL =====")
    print("1. Ajouter un joueur")
    print("2. Afficher tous les joueurs")
    print("3. Quitter")
    choice = input("Choix : ")
    
    if choice == "1":
        add_new_player()
    elif choice == "2":
        display_all_players_menu()
    elif choice == "3":
        print("Au revoir !")
    else:
        print("Choix invalide, veuillez réessayer.")


def display_all_players_menu():
    players = load_players()
    if players:
        print("Voici tous les joueurs enregistrés :")
        display_all_players(players)
    else:
        print("Aucun joueur enregistré.")


# Point d'entrée du programme
if __name__ == "__main__":
    main_menu()
