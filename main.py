from controllers import player_controller, tournament_controller
from views import player_view, tournament_view

def main():
    while True:
        # Ask the user what they want to do
        action = input(
            "What do you want to do? (1 - Add a player, 2 - View players, 3 - Add a tournament, 4 - View tournaments, Q - Quit) "
        )

        # Execute the appropriate action
        if action == "1":
            # Ask the user for player information
            last_name = input("Last Name: ")
            first_name = input("First Name: ")
            date_of_birth = input("Date of Birth (dd/mm/yyyy): ")
            score = int(input("Score: "))

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
            name = input("Tournament Name: ")
            location = input("Location: ")
            start_date = input("Start Date (dd/mm/yyyy hh:mm): ")
            end_date = input("End Date (dd/mm/yyyy hh:mm): ")
            time_control = input("Time Control (0 - Bullet, 1 - Blitz, 2 - Rapid): ")
            number_of_rounds = int(input("Number of Rounds (default = 4): ") or "4")
            current_round_number = int(input("Current Round Number: "))
            players = player_controller.load_players("data/players/players.json")
            rounds = []
            description = input("Tournament Description (max 200 characters): ")

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
            print("Unrecognized action. Please try again.")


if __name__ == "__main__":
    main()
