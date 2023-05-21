""" class TournamentView"""

from .common import top_bottom, get_choice, menu
from .player import PlayerView
from src.models.match import Matchs


class TournamentView:
    @top_bottom
    def menu(self, preview: str) -> str:
        """display the tournament menu and get the choice"""

        print("\n                              Tournament menu\n")
        menu(preview)
        print("                              tournament name* must be unique")
        print(
            "                              tournament name* is deletable but not editable\n"
        )

        return get_choice()

    def list_tournaments(self, tournaments_list: list, action: str):
        """diplay the tournaments list created in the system"""

        if len(tournaments_list) == 0:
            print(f"\n 0 tournament {action} in the system.\n")
        if len(tournaments_list) == 1:
            print(f"\n 1 tournament {action} in the system :\n")
        if len(tournaments_list) > 1:
            print(f"\n {len(tournaments_list)} tournaments {action} in the system :\n")

        if len(tournaments_list) > 0:
            print(
                " Tournament name      | Place           | Status          | Start_date      | End_date"
            )
            print(
                "______________________|_________________|_________________|_________________|_________________"
            )
            for y in tournaments_list:
                name = y["name"].ljust(20, " ")
                place = y["place"].ljust(15, " ")
                status = y["status"].ljust(15, " ")
                start_date = y["start_date"].ljust(15, " ")
                end_date = y["end_date"].ljust(15, " ")
                print(f" {name} | {place} | {status} | {start_date} | {end_date}")
            print()

    def create(self) -> list:
        """get the tournament's data"""

        print("\nTournament name* must be unique.\n")
        print("Please enter the tournament's values now :\n")

        response1 = self._get_name()
        response2 = self._get_place()
        response3 = self._get_description()

        return [response1, response2, response3]

    def create_response1(self):
        """used if the number of players registered in system < 4"""

        print(
            "\n🛑🚫 It is necessary to have a minimum of 4 players registered in system !\n"
        )
        print(
            "Please go to players menu to create players in system to be able to add them in the tournament.\n"
        )

    def create_response2(self, response1: bool, response2: bool):
        """used if the tournament name is not unique or to confirm the creation"""

        if response1 and response2:
            print("\n🟢 Tournament created successfully !\n")

        if response1 and not response2:
            print(
                "\n🛑🚫 A minimum of 4 valid player ine's is required to create a tournament.\n"
            )
            print("\nPlease retry with correct values.\n")
        if not response1 and not response2:
            print("\n🛑🚫 The tournament name is not unique !\n")
            print("\nPlease try again with a different tournament name.\n")

    def list_players(self, players_list: list):
        """list players in system"""

        PlayerView().list_players(players_list, "registered", "system")

    def add_player1(self, number_of_players: int) -> str:
        """get the number of players to add"""

        print("\nA minimum of 4 players is required to create a tournament.")
        print(
            f"\nBut don't exceed the number of players in the system, which is {number_of_players}.\n"
        )

        return input("How many players would you like to add ? (4 min.)> ")

    def add_player2(self, number_of_players: int):
        """get players ine list"""

        return [input(f"Player {p+1}'s ine > ") for p in range(number_of_players)]

    def add_player_response1(self):
        """used if the number of players entered by the user is incorrect"""

        print("\n🛑🚫 Incorrect value !\n")

    def add_player_response2(
        self, reponse1: bool, reponse2: bool, added_players: int, player_to_add: int
    ) -> list:
        """return the number of players added in a tournament"""

        if reponse1 and reponse2:
            print(f"\n🟢 {added_players}/{player_to_add} players added successfully !\n")

        elif reponse1 and not reponse2:
            if added_players > 0:
                print(
                    f"\n🛑🚫 Only {added_players}/{player_to_add} players added successfully !\n"
                )

            if added_players == 0:
                print(f"\n🛑🚫 0/{player_to_add} players added... \n")
            print("Please check the players' ine that haven't been added.\n")
            print(
                "All players ine must exist in the system before they can be added to a tournament.\n"
            )
        elif not reponse1:
            self._inexistent_tournament()

    def edit(self) -> list:
        """get the new tournament's data to edit"""

        print("\nWhich tournament would you like to edit ?\n")
        response1 = self._get_name()
        print("\nPlease enter the tournament's new values now :\n")
        response2 = self._get_place()
        response3 = self._get_description()

        return [response1, response2, response3]

    def edit_response(self, response: bool):
        """display response"""

        if response:
            print("\n 🟢 Tournament edited successfully !\n")
        else:
            self._inexistent_tournament()

        return response

    def delete(self) -> str:
        """get the tournament name to delete"""

        print("\nWhich tournament would you like to delete ?\n")
        print("🟠 The tournament's data will be definitevely lost...\n")

        return self._get_name()

    def delete_response1(self) -> str:
        """ask the deletion's confirmation"""

        print("\nDo you confirm the deletion ?\n")

        return self._get_user_choice()

    def delete_response2(self):
        """the deletion's confirmation"""

        print("\n 🟢 Tournament deleted successfully !\n")

    def select1(self) -> str:
        """get the tournament name"""

        print("\nThe tournament must be created in the system.\n")
        print("\nWhich tournament would you like to select ?\n")

        return self._get_name()

    def select_round(
        self, tournament_data: list, player_ranking: list, current_round: int
    ) -> str:
        """display the tournament's data when the current round is finished
        or when the tournament status is 'created'"""

        self._select_view1(tournament_data)
        self._select_view2(player_ranking)

        if current_round > 0:
            print(f"The round {current_round} is finished.\n")
        print("Would you like to run the next round?\n")

        return self._get_user_choice()

    def select_end(self, tournament_data: list, player_ranking: list):
        """display the tournament's data when it has conclued"""

        self._select_view1(tournament_data)

        j = 1
        for p in player_ranking:
            if j == 1:
                print(f" {p['rank']}  {p['last_name'].ljust(10,' ')} {p['score']} pt 🥇")
                j += 1
                continue
            elif j == 2:
                print(f" {p['rank']}  {p['last_name'].ljust(10,' ')} {p['score']} pt 🥈")
                j += 1
                continue
            elif j == 3:
                print(f" {p['rank']}  {p['last_name'].ljust(10,' ')} {p['score']} pt 🥉")
                j += 1
                continue
            else:
                print(f" {p['rank']}  {p['last_name'].ljust(10,' ')} {p['score']} pt")
                j += 1

    def select_match(
        self, tournament_data: list, player_ranking: list, match_list: list
    ) -> str:
        """display the tournament's data when the current round is ruuning"""

        self._select_view1(tournament_data)
        self._select_view2(player_ranking)

        i = 1
        for m in match_list:
            print(Matchs(i, m))
            i += 1

        print("\nWould you like to enter the result of a match ?\n")

        return self._get_user_choice()

    def select_result(self) -> list:
        """get the match result"""

        print("\nThe winner gets 1 point and the loser gets 0 point,")
        print("both players get 0.5 point if they draw.")
        print("\nFor wich match would you like to enter the result ?\n")

        response1 = input("\nThe match number (ex : 1) > ")
        response2 = input("The score of the player in white (ex : 1) > ")
        response3 = input("The score of the player in black (ex : 0) > ")

        return [response1, response2, response3]

    def select_result_response(self, response1: bool, response2: bool) -> list:
        """get the match result"""

        if response1 and response2:
            print("\n 🟢 Match updated successfully !\n")
        if response1 and not response2:
            print("\n🛑🚫 Invalid result entered !\n")
            print("\nPlease try again with a valid result")
        if not response1:
            print("\n🛑🚫 Invalid match number !\n")
            print("\nPlease try again with a valid match number")

    def _get_name(self) -> str:
        """get the tournament's name"""

        return input("Tournament's name* > ")

    def _get_place(self) -> str:
        """get the tournament's place"""

        return input("Tournament's place > ")

    def _get_description(self) -> str:
        """get the tournament's description"""

        return input("Tournament's description > ")

    def _get_user_choice(self) -> str:
        """get the user's choice"""

        return input("y/n > \n")

    def _inexistent_tournament(self):
        """used if the tournament is not registered"""

        print("\n 🛑🚫 This tournament name does not exist in the system !\n")
        print("Please try again with a registered tournament name.\n")

    def _select_view1(self, tournament_data: list):
        """diplay the tournament's data when it is selected"""

        print()
        print("-" * 80)
        print("\n __________________________________________________________________")
        print("| Tournament name                | Status         | Current round  |")
        print("|________________________________|________________|________________|")
        print("|                                |                |                |")
        name = tournament_data[0].ljust(30, " ")
        status = tournament_data[1].ljust(14, " ")
        round = tournament_data[2].ljust(14, " ")

        print(f"| {name} | {status} | {round} |")
        print("|________________________________|________________|________________|\n")

    def _select_view2(self, player_ranking: list):
        """diplay the tournament's players when it is selected"""

        if len(player_ranking) > 0:
            for p in player_ranking:
                print(f" {p['rank']}  {p['last_name'].ljust(10,' ')} {p['score']} pt")
            print()
