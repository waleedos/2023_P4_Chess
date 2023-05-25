from controllers.player_controller import add_player, load_players, get_player_by_id, update_player
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
    print("3. Editer un joueur")
    print("4. Quitter")
    choice = input("Choix : ")
    
    if choice == "1":
        add_new_player()
    elif choice == "2":
        display_all_players_menu()
    elif choice == "3":
        edit_player_menu()
    elif choice == "4":
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


def edit_player_menu():
    chess_id = input("Entrez l'ID du joueur à éditer (ChessId) : ")
    player = get_player_by_id(chess_id)
    if player is None:
        print("Aucun joueur trouvé avec cet ID.")
    else:
        print("Veuillez entrer les nouvelles informations pour le joueur (laissez vide pour ne pas changer) :")
        last_name = input("Nom [" + player.last_name + "]: ")
        first_name = input("Prénom [" + player.first_name + "]: ")
        birthdate = input("Date de naissance (jj/mm/aaaa) [" + player.birthdate + "]: ")
        gender = input("Genre (M ou F) [" + player.gender + "]: ")
        rank = input("Classement [" + str(player.rank) + "]: ")
        chess_id_new = input("ChessId (AB12345) [" + player.ChessId + "]: ")
        
        if last_name != "":
            player.last_name = last_name
        if first_name != "":
            player.first_name = first_name
        if birthdate != "":
            player.birthdate = birthdate
        if gender != "":
            player.gender = gender
        if rank != "":
            player.rank = int(rank)
        if chess_id_new != "":
            player.ChessId = chess_id_new

        update_player(player)

        # Confirmation que les informations ont été mises à jour
        print(Fore.RED + "Les nouvelles informations du joueur ont été prises en compte.\n" + Style.RESET_ALL)
        
# Point d'entrée du programme
if __name__ == "__main__":
    main_menu()
