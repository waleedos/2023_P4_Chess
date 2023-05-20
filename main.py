from controllers import player_controller, tournament_controller
from views import player_view, tournament_view
from colorama import init, Fore, Style

def main():
    # Initialize colorama
    init()

    while True:
        # Ask the user what they want to do
        print(Fore.BLUE + "**********************************")
        print("Qu'est-ce que vous voulez faire ? :")
        print(Style.RESET_ALL + "**********************************")
        print("1- Ajouter un joueur")
        print("2- Voir les joueurs")
        print("3- Ajouter un tournoi")
        print("4- Voir les tournois")
        print("Q- Quitter")
        print("**********************************")
        action = input()

        # Execute the appropriate action
        if action == "1":
            # Ask the user for player information
            last_name = input("Nom de famille : ")
            first_name = input("Prénom : ")
            date_of_birth = input("Date de naissance (jj/mm/aaaa) : ")
            score = int(input("Score : "))

            # Create the player
            player = player_controller.create_player(last_name, first_name, date_of_birth, score)

            # Add the player to the list of players and save to the JSON file
            player_controller.add_player(player, 'data/players/players.json')

            # Display the player
            player_view.display_player(player)

        elif action == "2":
            # Load players from the JSON file and display
            loaded_players = player_controller.load_players('data/players/players.json')
            player_view.display_players(loaded_players)
        
        elif action == "3":
            # Ask the user for tournament information
            name = input("Nom du tournoi : ")
            location = input("Lieu : ")
            start_date = input("Date de début (jj/mm/aaaa hh:mm) : ")
            end_date = input("Date de fin (jj/mm/aaaa hh:mm) : ")
            time_control = input("Contrôle du temps (0 - Bullet, 1 - Blitz, 2 - Rapide) : ")
            number_of_rounds = int(input("Nombre de tours (par défaut = 4) : ") or "4")
            current_round_number = int(input("Numéro du tour en cours : "))
            players = player_controller.load_players("data/players/players.json")
            rounds = []
            description = input("Description du tournoi (max 200 caractères) : ")

            # Create the tournament
            tournament = tournament_controller.create_tournament(
                name,
                location,
                start_date,
                end_date,
                time_control,
                number_of_rounds,
                current_round_number,
                players,
                rounds,
                description,
            )

            # Add the tournament to the list of tournaments and save to the JSON file
            tournament_controller.add_tournament(
                tournament, "data/tournaments/tournaments.json"
            )

            # Display the tournament
            tournament_view.display_tournament(tournament)

        elif action == "4":
            # Load tournaments from the JSON file and display
            loaded_tournaments = tournament_controller.load_tournaments(
                "data/tournaments/tournaments.json"
            )
            tournament_view.display_tournaments(loaded_tournaments)

        elif action.lower() == "q":
            # Quit the program
            break

        else:
            print("Action non reconnue. Veuillez réessayer.")

    # Reset console colors
    print(Style.RESET_ALL)


if __name__ == "__main__":
    main()
