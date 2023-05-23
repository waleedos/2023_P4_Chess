from src.views.homepage import HomepageView
from src.views.player import PlayerView


def main():
    homepage_view = HomepageView()
    player_view = PlayerView()

    while True:
        choice = homepage_view.menu()

        if choice == "1":
            while True:
                player_choice = player_view.menu("Player menu")

                if player_choice == "1":  # Lister les joueurs
                    player_view.list_players(player_view.players, "registered", "system")
                elif player_choice == "2":  # Sélectionner un joueur
                    player_chess_id = player_view.select()
                    player_view.select_response(player_view.get_player(player_chess_id))

                elif player_choice == "3":  # Créer un joueur
                    player_data = player_view.add_player()
                
                elif player_choice == "4":  # Modifier un joueur
                    player_data = player_view.edit_player()
                
                elif player_choice == "5":  # Supprimer un joueur
                    player_chess_id = player_view.delete()
                    response = player_view.delete_player(player_chess_id)
                    player_view.delete_response(response)
                
                elif player_choice == "6":  # Retourner au menu principal
                    break
             
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == "2":
            # Traiter le choix du menu Tournament
            pass
        elif choice == "3":
            # Traiter le choix du menu Report
            pass
        elif choice == "4":
            # Quitter l'application
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
