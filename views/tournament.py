from colorama import Fore, Style, init
from views.view import View
from utils.timestamp import get_timestamp
from controller.database import load_db

init()


class CreateTournament(View):

    def display_menu(self):

        date = get_timestamp()
        print(date + " : Nouveau tournoi")

        name = input("Nom du tournoi :\n"
                     ">>> ")

        location = self.get_user_entry(
            msg_display="Lieu :\n"
                        ">>> ",
            msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
            value_type="string"
        )

        user_selection_time_control = self.get_user_entry(
            msg_display="Contrôle de temps :\n"
                        "0 - Bullet\n"
                        "1 - Blitz\n"
                        "2 - Coup Rapide\n"
                        ">>> ",
            msg_error=f"{Fore.RED}Veuillez entrer 0, 1 ou 2\n{Style.RESET_ALL}",
            value_type="selection",
            assertions=["0", "1", "2"]
        )

        if user_selection_time_control == "0":
            time_control = "Bullet"
        elif user_selection_time_control == "1":
            time_control = "Blitz"
        else:
            time_control = "Coup Rapide"

        nb_players = self.get_user_entry(
            msg_display="Nombre de joueurs :\n"
                        ">>> ",
            msg_error=f"{Fore.RED}Veuillez entrer un nombre entier supérieur ou égal à 2\n{Style.RESET_ALL}",
            value_type="num_superior",
            default_value=2
        )

        nb_rounds = self.get_user_entry(
            msg_display="Nombre de tours (4 par défaut) :\n"
                        ">>> ",
            msg_error=f"{Fore.RED}Veuillez entrer 4 ou plus\n{Style.RESET_ALL}",
            value_type="num_superior",
            default_value=4
        )

        desc = input("Description du tournoi :\n>>> ")

        return {
            "name": name,
            "location": location,
            "date": date,
            "time_control": time_control,
            "nb_players": nb_players,
            "nb_rounds": nb_rounds,
            "desc": desc
        }


class LoadTournament(View):

    def display_menu(self):

        tournaments = load_db("tournaments")

        if tournaments:

            build_selection = self.build_selection(iterable=tournaments, display_msg="Choisir un tournoi :\n",
                                                   assertions=[])

            user_input = int(self.get_user_entry(

                msg_display=build_selection['msg'] + ">>> ",
                msg_error=f"{Fore.RED}Veuillez entrer un nombre entier\n{Style.RESET_ALL}",
                value_type="selection",
                assertions=build_selection['assertions']
            ))

            serialized_loaded_tournament = tournaments[user_input-1]

            return serialized_loaded_tournament

        else:
            return False
