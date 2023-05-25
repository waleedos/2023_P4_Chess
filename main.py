# main.py
from controllers.player_controller import create_new_player, load_players, edit_existing_player, get_player_by_id, delete_player
from views.player_view import get_new_player_info, get_updated_player_info, display_all_players, display_update_confirmation, display_delete_confirmation, get_player_id_to_delete
from colorama import init

# Menu principal
def main_menu():
    init()  # Initialisation de colorama
    while True:
        print("===== MENU PRINCIPAL =====")
        print("1. Ajouter un joueur")
        print("2. Afficher tous les joueurs")
        print("3. Editer un joueur")
        print("4. Supprimer un joueur")
        print("5. Quitter")
        choice = input("Choix : ")
        
        if choice == "1":
            player_data = get_new_player_info()
            create_new_player(player_data)
        elif choice == "2":
            players = load_players()
            display_all_players(players)
        elif choice == "3":
            chess_id = input("Entrez l'ID du joueur à éditer (ChessId) : ")
            player = get_player_by_id(chess_id)
            if player is not None:
                new_player_data = get_updated_player_info(player)
                edit_existing_player(chess_id, new_player_data)
                display_update_confirmation()
            else:
                print("Aucun joueur trouvé avec cet ID.")
        elif choice == "4":
            chess_id = get_player_id_to_delete()
            delete_player(chess_id)
            display_delete_confirmation()
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


# Point d'entrée du programme
if __name__ == "__main__":
    main_menu()
