"""class PlayerController"""

from .common import clean_capitalize, clean_upper, clean

from src.models.player import Players
from src.views.player import PlayerView


class PlayerController:
    def __init__(self, view=PlayerView()):
        self.view = view

    def run(self):
        """player menu"""

        if len(Players.read()) < 2:
            preview = str(len(Players.read())) + " player registered in system."
        else:
            preview = str(len(Players.read())) + " players registered in system."
        choice = self.view.menu(preview)

        if choice == "1":
            """1. diplay players list"""

            self.view.list_players(Players.read(), "registered", "system")
            self.run()

        elif choice == "2":
            """2. select a player"""

            choice_2 = clean_upper(self.view.select())
            self.view.select_response(Players.find(choice_2))
            self.run()

        elif choice == "3":
            """3. create a new player"""

            choice_3 = self.view.add_player()
            if (len(choice_3[3]) == 7) and (
                len(Players.find(clean_upper(choice_3[3]))) == 0
            ):
                Players(
                    clean_upper(choice_3[0]),
                    clean_capitalize(choice_3[1]),
                    clean(choice_3[2]),
                    clean_upper(choice_3[3]),
                ).create()
                self.view.add_response(True)
            else:
                self.view.add_response(False)
            self.run()

        elif choice == "4":
            """4. edit player"""

            choice_4 = self.view.edit_player()
            if len(Players.find(clean_upper(choice_4[3]))) == 1:
                player = Players.load(clean_upper(choice_4[3]))
                player.last_name = clean_upper(choice_4[0])
                player.first_name = clean_capitalize(choice_4[1])
                player.birthdate = clean(choice_4[2])
                player.update()
                self.view.edit_response(True)
            else:
                self.view.edit_response(False)
            self.run()

        elif choice == "5":
            """5. delete player"""

            choice_5 = clean_upper(self.view.delete())
            if len(Players.find(choice_5)) == 1:
                Players.load(choice_5).delete()
                self.view.delete_reponse(True)
            else:
                self.view.delete_reponse(False)
            self.run()

        elif choice == "6":
            """6. Return to Home menu"""

            return "exit"

        else:
            """invalid choice"""

            self.run()
