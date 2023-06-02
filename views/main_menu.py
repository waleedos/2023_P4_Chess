from colorama import Fore, Style, init
from controller.database import save_db, load_tournament
from controller.player import update_rankings, display_players
from controller.tournament import create_tournament, play_tournament
from views.player import CreatePlayer
from views.report import Report
from views.tournament import LoadTournament
from views.view import View

init()


class MainMenu(View):

    def display_main_menu(self):

        while True:
            user_input = self.get_user_entry(
                msg_display=f"\n{Fore.GREEN}************************************\n"
                            "       Faîtes votre choix :\n"
                            "************************************\n"
                            f"{Style.RESET_ALL}"
                            "[0] - Nouveau tournoi\n"
                            "[1] - Charger un tournoi\n"
                            "[2] - Créer des nouveaux joueurs\n"
                            "[3] - Listes (joueurs, tournois)\n"
                            f"{Fore.RED}[Q] - Quitter\n{Style.RESET_ALL}"
                            "\n>>> ",
                msg_error=f"{Fore.RED}Veuillez entrer une valeur valide\n{Style.RESET_ALL}",
                value_type="selection",
                assertions=["0", "1", "2", "3", "Q", "q"]
            )

            if user_input == "0":
                tournament = create_tournament()
                break

            elif user_input == "1":
                serialized_tournament = LoadTournament().display_menu()
                if serialized_tournament:
                    tournament = load_tournament(serialized_tournament)
                    break
                else:
                    print("Aucun tournoi sauvegardé !")
                    continue

            elif user_input == "2":
                user_input = self.get_user_entry(
                    msg_display="Nombre de joueurs à créer:\n"
                                "\n>>> ",
                    msg_error=f"{Fore.RED}Veuillez entrer une valeur valide\n{Style.RESET_ALL}",
                    value_type="numeric"
                )
                for i in range(user_input):
                    serialized_new_player = CreatePlayer().display_menu()
                    save_db("players", serialized_new_player)

            elif user_input == "3":
                while True:
                    user_input = self.get_user_entry(
                        msg_display="0 - Joueurs\n"
                                    "1 - Tournois\n"
                                    f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                    "\n>>> ",
                        msg_error=f"{Fore.RED}Veuillez faire un choix valide.\n{Style.RESET_ALL}",
                        value_type="selection",
                        assertions=["0", "1", "r"]
                    )
                    if user_input == "r":
                        break
                    elif user_input == "0":
                        while True:
                            user_input = self.get_user_entry(
                                msg_display=f"{Fore.GREEN}************************************\n"
                                            "       Voir le classement :\n"
                                            "************************************\n"
                                            f"{Style.RESET_ALL}"
                                            "[0] - Par rang\n"
                                            "[1] - Par ordre alphabétique\n"
                                            "[2] - Par ordre d'enregistrement\n"
                                            f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                            "\n0>>> ",
                                msg_error=f"{Fore.RED}Veuillez faire un choix valide.\n{Style.RESET_ALL}",
                                value_type="selection",
                                assertions=["0", "1", "2", "r", "R"]
                            )
                            if user_input == "r":
                                break
                            elif user_input == "0":
                                sorted_players = Report().sort_players(Report().players, by_rank=True)
                                if not sorted_players:
                                    print("Oups... Aucun joueur n'est enregistré dans la base")
                                    break
                                Report().display_players_report(players=sorted_players)
                            elif user_input == "1":
                                sorted_players = Report().sort_players(Report().players, by_rank=False)
                                if not sorted_players:
                                    print("Oups... Aucun joueur n'est enregistré dans la base")
                                    break
                                Report().display_players_report(players=sorted_players)
                            elif user_input == "2":
                                display_players()
                    elif user_input == "1":
                        Report().display_tournaments_reports()
            else:
                quit()

        user_input = self.get_user_entry(
            msg_display=f"{Fore.GREEN}Que faire ?\n{Style.RESET_ALL}"
                        "[0] - Jouer le tournoi\n"
                        f"{Fore.RED}[q] - Quitter\n{Style.RESET_ALL}"
                        "\n>>> ",
            msg_error=f"{Fore.RED}Veuillez entrer une valeur valide\n{Style.RESET_ALL}",
            value_type="selection",
            assertions=["0", "q", "Q"]
        )

        if user_input == "0":
            rankings = play_tournament(tournament, new_tournament_loaded=True)
        else:
            quit()

        print(f"{Fore.GREEN}  Tournoi {tournament.name} terminé !\n{Style.RESET_ALL}")
        print(f"{Fore.BLUE}      Voici les résultats : \n{Style.RESET_ALL}")

        for i, player in enumerate(rankings):
            print(f"{str(i + 1)} - {player}")

        user_input = self.get_user_entry(
            msg_display=f"\n{Fore.BLUE}  Mise à jour des classements\n{Style.RESET_ALL}"
                        "\n[0] - Automatiquement\n"
                        "[1] - Manuellement\n"
                        f"{Fore.RED}[Q] - Quitter\n{Style.RESET_ALL}"
                        "\n>>> ",
            msg_error=f"{Fore.RED}Veuillez entrer une valeur valide\n{Style.RESET_ALL}",
            value_type="selection",
            assertions=["0", "1", "q", "Q"]
        )
        if user_input == "0":
            for i, player in enumerate(rankings):
                print(player.name)
                update_rankings(player, i + 1)
        elif user_input == "1":
            for player in rankings:
                rank = self.get_user_entry(
                    msg_display=f"Rang de {player}:\n"
                                ">>> ",
                    msg_error="Veuillez entrer un nombre entier.",
                    value_type="numeric"
                )
                update_rankings(player, rank)
        else:
            quit()
