from controllers.player_controller import add_player
from models.player import Player

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
    print("Le joueur a été ajouté avec succès !")

# Menu principal
def main_menu():
    print("===== MENU PRINCIPAL =====")
    print("1. Ajouter un joueur")
    print("2. Quitter")
    choice = input("Choix : ")
    
    if choice == "1":
        add_new_player()
    elif choice == "2":
        print("Au revoir !")
    else:
        print("Choix invalide, veuillez réessayer.")

# Point d'entrée du programme
if __name__ == "__main__":
    main_menu()
