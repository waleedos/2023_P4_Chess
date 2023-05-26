from colorama import init, Fore, Style
from controllers.player_controller import create_new_player, load_players, edit_existing_player, delete_player
from views.player_view import get_new_player_info, get_updated_player_info, get_player_id_to_delete, display_all_players
from controllers.tournament_controller import create_new_tournament, load_tournaments
from views.tournament_view import get_new_tournament_info, display_all_tournaments


def main_menu():
    init()  # Initialisation de colorama
    while True:
        print("===== MENU PRINCIPAL =====")
        print("1. Ajouter un joueur")
        print("2. Afficher tous les joueurs")
        print("3. Editer un joueur")
        print("4. Supprimer un joueur")
        print("5. Créer un nouveau tournoi")
        print("6. Afficher tous les tournois")
        print("7. Quitter")
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
            tournament_data = create_new_tournament()
        elif choice == "6":
            tournaments = load_tournaments()
            display_all_tournaments(tournaments)
        elif choice == "7":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
            

if __name__ == "__main__":
    main_menu()
