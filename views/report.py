from controller.database import load_db
from views.view import View
from operator import itemgetter
from colorama import Fore, Style, init
init()


class Report(View):

    def __init__(self):
        self.players = load_db("players")
        self.tournaments = load_db("tournaments")

    def display_players_report(self, players=[]):

        players = players

        build_selection = self.build_selection(iterable=players,
                                               display_msg=f"{Fore.BLUE}Voir les détails d'un joueur\
                                               :\n{Style.RESET_ALL}",
                                               assertions=["r"])

        while True:
            print("Classement : ")

            user_input = self.get_user_entry(
                msg_display=build_selection['msg'] + f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                                     "\n>>> ",
                msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
                value_type="selection",
                assertions=build_selection['assertions']
            )

            if user_input == "r":
                break

            else:
                selected_player = players[int(user_input) - 1]

                while True:
                    print(f"{Fore.BLUE}\nDétails du joueur {selected_player['name']}:\n{Style.RESET_ALL}")
                    print(f"Classement: {selected_player['rating']}\n"
                          f"Score total: {selected_player['total_score']}\n"
                          f"Nom: {selected_player['name']}\n"
                          f"Prénom: {selected_player['firstname']}\n"
                          f"Date de naissance: {selected_player['birthday']}\n"
                          f"Sexe: {selected_player['gender']}\n"
                          )

                    user_input = self.get_user_entry(
                        msg_display=f"{Fore.GREEN}Que faire ?\n{Style.RESET_ALL}"
                                    f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                    "\n>>> ",
                        msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
                        value_type="selection",
                        assertions=["r"]
                    )

                    if user_input == "r":
                        break

    def display_tournaments_reports(self):

        build_selection = self.build_selection(
            iterable=self.tournaments,
            display_msg=f"{Fore.BLUE}Voir les détails d'un tournoi :\n{Style.RESET_ALL}",
            assertions=['r']
        )

        while True:

            if not self.tournaments:
                print("Oups.. Aucun tournoi n'est enregistré dans la base")
                break

            print("Tournois :")

            user_input = self.get_user_entry(
                msg_display=build_selection['msg'] + f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                                     "\n>>> ",
                msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
                value_type="selection",
                assertions=build_selection['assertions']
            )

            if user_input == "r":
                break

            else:
                selected_tournament = self.tournaments[int(user_input) - 1]

                while True:
                    print(f"{Fore.BLUE}\nDétails du tournoi {selected_tournament['name']}\n{Style.RESET_ALL}"
                          f"Nom: {selected_tournament['name']}\n"
                          f"Lieu: {selected_tournament['location']}\n"
                          f"Date: {selected_tournament['date']}\n"
                          f"Contrôle du temps: {selected_tournament['time_control']}\n"
                          f"Nombre de rounds: {selected_tournament['rounds_number']}\n"
                          f"Description: {selected_tournament['description']}\n"
                          )

                    user_input = self.get_user_entry(
                        msg_display=f"{Fore.GREEN}Que faire ?\n{Style.RESET_ALL}"
                                    "[0] - Voir les participants\n"
                                    "[1] - Voir les Rounds\n"
                                    f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                    "\n>>> ",
                        msg_error="Veuillez entrer une sélection valide",
                        value_type="selection",
                        assertions=["0", "1", "2", "r", "R"]
                    )

                    if user_input == "r" or user_input == "R":
                        break

                    elif user_input == "0":
                        while True:
                            user_input = self.get_user_entry(
                                msg_display=f"{Fore.GREEN}Type de classement:\n{Style.RESET_ALL}"
                                            "[0] - Par rang\n"
                                            "[1] - Par ordre alphabétique\n"
                                            f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                            "\n>>> ",
                                msg_error=f"{Fore.RED}Veuillez entrer une sélection valide\n{Style.RESET_ALL}",
                                value_type="selection",
                                assertions=["0", "1", "r"]
                            )

                            if user_input == "r":
                                break
                            elif user_input == "0":
                                sorted_players = self.sort_players(selected_tournament["players"],
                                                                   by_rank=True)
                                self.display_players_report(players=sorted_players)
                            elif user_input == "1":
                                sorted_players = self.sort_players(selected_tournament["players"],
                                                                   by_rank=False)
                                self.display_players_report(players=sorted_players)

                    elif user_input == "1":
                        self.display_rounds(selected_tournament["list_round"])

    def display_rounds(self, rounds):

        build_selection = self.build_selection(
            iterable=rounds,
            display_msg=f"{Fore.GREEN}Voir les détails d'un Round:\n{Style.RESET_ALL}",
            assertions=['r']
        )

        while True:
            print(f"{Fore.BLUE} Les Rounds de ce tournoi:\n{Style.RESET_ALL}")

            user_input = self.get_user_entry(
                msg_display=build_selection['msg'] + f"\n{Fore.YELLOW}r - Retour\n{Style.RESET_ALL}"
                                                     ">>> ",
                msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
                value_type="selection",
                assertions=build_selection['assertions']
            )

            if user_input == "r":
                break

            else:
                selected_round = rounds[int(user_input) - 1]

                while True:
                    print(f"{Fore.BLUE}\nDétails du round {selected_round['name']}:\n{Style.RESET_ALL}"
                          f"Nom: {selected_round['name']}\n"
                          f"Nombre de matchs: {len(selected_round['matchs'])}\n"
                          f"Date de début: {selected_round['start_date']}\n"
                          f"Date de fin: {selected_round['end_date']}\n"
                          )

                    user_input = self.get_user_entry(
                        msg_display=f"{Fore.GREEN}Que faire ?\n{Style.RESET_ALL}"
                                    "[0] - Voir les matchs\n"
                                    f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                    "\n>>> ",
                        msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
                        value_type="selection",
                        assertions=["0", "r"]
                    )

                    if user_input == "r":
                        break

                    else:
                        build_selection = self.build_selection(
                            iterable=selected_round['matchs'],
                            display_msg=f"{Fore.BLUE}\nVoir les détails d'un match\n{Style.RESET_ALL}",
                            assertions=['r']
                        )

                        print(f"\n{Fore.GREEN}Les Matchs de ce round:\n{Style.RESET_ALL}")
                        user_input = self.get_user_entry(
                            msg_display=build_selection['msg'] + f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                                                 "\n>>> ",
                            msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
                            value_type="selection",
                            assertions=build_selection['assertions']
                        )

                        if user_input == "r":
                            break
                        else:
                            selected_match = selected_round['matchs'][int(user_input) - 1]

                            while True:
                                print(f"{Fore.BLUE}\nDétails du {selected_match['name']}:\n{Style.RESET_ALL}"
                                      f"Joueur 1 : " +
                                      f"{selected_match['player_1']['name']} ({selected_match['score_player_1']} pts)\n"
                                      f"Joueur 2 : " +
                                      f"{selected_match['player_2']['name']} ({selected_match['score_player_2']} pts)\n"
                                      f"Gagnant: {selected_match['winner']}\n"
                                      )

                                user_input = self.get_user_entry(
                                    msg_display=f"{Fore.GREEN}Que faire ?\n{Style.RESET_ALL}"
                                                f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                                "\n>>> ",
                                    msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
                                    value_type="selection",
                                    assertions=["r"]
                                )

                                if user_input == "r":
                                    break

    @staticmethod
    def sort_players(players: list, by_rank: bool) -> list:

        if by_rank:
            sorted_players = sorted(players, key=itemgetter('rating'))
        else:
            sorted_players = sorted(players, key=itemgetter('name'))

        return sorted_players
