"""class PlayerView"""

from .common import top_bottom, get_choice, menu


class PlayerView:
    @top_bottom
    def menu(self, preview: str) -> str:
        """display the player menu and get the choice"""

        print("\n                              Player menu\n")
        menu(preview)
        print(
            "                              ine* is the National Chess ID and, it must be unique"
        )
        print("                              ine* is deletable but not editable\n")

        return get_choice()

    def list_players(self, players_list: list, status: str, location: str):
        """display the players list sorted by name"""

        if len(players_list) == 0:
            print(f"\n0 player {status} in the {location}.\n ")
        if len(players_list) == 1:
            print(f"\n1 player {status} in the {location} :\n ")
        if len(players_list) > 1:
            print(f"\n{len(players_list)} players {status} in the {location} :\n ")
        if len(players_list) > 0:
            print("\n Last-Name       | First-Name      | Birthdate       | Ine")
            print("_________________|_________________|_________________|________")
            for p in players_list:
                last_name = p["last_name"].ljust(15, " ")
                first_name = p["first_name"].ljust(15, " ")
                birthdate = p["birthdate"].ljust(15, " ")
                ine = p["ine"]
                print(f" {last_name} | {first_name} | {birthdate} | {ine}")
            print()

    def select(self) -> str:
        """get the player's ine"""

        print("\nPlease enter the player's ine* to select it from the system\n")

        return self._get_ine()

    def select_response(self, result: list):
        """display the found player if there is a result"""

        if len(result) == 0:
            self._unfound_ine()

        if len(result) > 0:
            self.list_players(result, "selected", "system")

    def add_player(self) -> list:
        """get the player's data"""

        print("\nPlease enter the player's values now")
        print("ine* is unique to each player\n")
        response1 = self._get_last_name()
        response2 = self._get_first_name()
        response3 = self._get_birthdate()
        response4 = self._get_ine()

        return [response1, response2, response3, response4]

    def add_response(self, response: bool):
        """display a response after adding a player"""

        if response:
            print("\n🟢 player registered successfully !\n")
        else:
            print(
                "\n🛑🚫 This ine* is already in the system or is in an incorrect format !\n"
            )
            print("Please retry with a different valid ine*\n")

    def edit_player(self) -> list:
        """get the player's new values"""

        print("\nPlease enter the player's ine* to edit\n")

        response4 = self._get_ine()

        print("\nPlease enter the new player's values now\n")
        response1 = self._get_last_name()
        response2 = self._get_first_name()
        response3 = self._get_birthdate()

        return [response1, response2, response3, response4]

    def edit_response(self, response: bool):
        """display the response after adding a player"""

        if response:
            print("\n🟢 player edited successfully !\n")
        else:
            self._unfound_ine()

    def delete(self) -> str:
        """get the player's ine"""

        print("\nEnter the player's ine* to delete from the system\n")

        return self._get_ine()

    def delete_reponse(self, response: bool):
        """display a response after deleting a player"""

        if response:
            print("\n🟢 player deleted successfully !\n")
        else:
            self._unfound_ine()

    def _get_ine(self) -> str:
        """get the player's ine"""

        return input("Player's ine* > ")

    def _get_last_name(self) -> str:
        """get the player's last name"""

        return input("Player's last-name > ")

    def _get_first_name(self) -> str:
        """get the player's first name"""

        return input("Player's first-name > ")

    def _get_birthdate(self) -> str:
        """get the player's birthdate"""

        return input("Player's birthdate > ")

    def _unfound_ine(self):
        """display a message if the ine is incorrect"""

        print(
            "\n🛑🚫 This ine* is not in the system ! Please retry with a registered ine*.\n"
        )
