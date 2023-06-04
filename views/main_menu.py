from colorama import Fore, Style, init
from controller.database import save_db, load_tournament
from controller.player import update_rankings, display_players
from controller.tournament import create_tournament, play_tournament
from views.player import CreatePlayer
from views.report import Report
from views.tournament import LoadTournament
from views.view import View

init()


# Définition d'une nouvelle classe MainMenu, qui hérite de la classe View. Cette classe représente le menu principal
# du programme
class MainMenu(View):

    # Définition de la méthode display_main_menu dans la classe MainMenu. Cette méthode affiche le menu principal et
    # traite les entrées de l'utilisateur.
    def display_main_menu(self):

        while True:
            user_input = self.get_user_entry(
                msg_display=f"\n{Fore.GREEN}************************************\n"
                            "       Faîtes votre choix :\n"
                            "************************************\n"
                            f"{Style.RESET_ALL}"
                            " \n[0] - Nouveau tournoi\n"
                            "[1] - Charger un tournoi\n"
                            "[2] - Créer des nouveaux joueurs\n"
                            "[3] - Listes des joueurs & rapports\n"
                            "[4] - Listes des tournois & rapports\n"
                            f"{Fore.RED}\n[Q] - Quitter\n{Style.RESET_ALL}"
                            "\n>>> ",
                msg_error=f"{Fore.RED}Veuillez entrer une valeur valide\n{Style.RESET_ALL}",
                value_type="selection",
                assertions=["0", "1", "2", "3", "4", "Q", "q"]
            )
            # Un menu est affiché à l'utilisateur avec différentes options. La méthode get_user_entry de la classe
            # parent View est utilisée pour obtenir une entrée de l'utilisateur et pour vérifier si elle est valide.

            if user_input == "0":
                tournament = create_tournament()
                break
            # Si l'utilisateur entre "0", un nouveau tournoi est créé en utilisant la fonction create_tournament.

            elif user_input == "1":
                serialized_tournament = LoadTournament().display_menu()
                if serialized_tournament:
                    tournament = load_tournament(serialized_tournament)
                    break
            # Si l'utilisateur entre "1", le programme tente de charger un tournoi existant. Si un tournoi est
            # trouvé, il est chargé, sinon un message d'erreur est affiché.

                else:
                    print("Aucun tournoi sauvegardé !")
                    continue

            elif user_input == "2":
                user_input = self.get_user_entry(
                    msg_display="Nombre de joueurs à créer:\n"
                                "\n>>> ",
                    # Si l'utilisateur entre "2", il est invité à créer de nouveaux joueurs. L'utilisateur doit
                    # spécifier combien de joueurs il souhaite créer. Pour chaque joueur, un formulaire de création de
                    # joueur est affiché et les données du joueur sont ensuite enregistrées dans la base de données.
                    msg_error=f"{Fore.RED}Veuillez entrer une valeur valide\n{Style.RESET_ALL}",
                    value_type="numeric"
                )
                for i in range(user_input):
                    serialized_new_player = CreatePlayer().display_menu()
                    save_db("players", serialized_new_player)
                    # crée un nouveau joueur pour chaque valeur dans la plage définie par user_input. Pour chaque
                    # nouveau joueur, la méthode display_menu est appelée sur une nouvelle instance de CreatePlayer et
                    # le joueur est sauvegardé dans la base de données.

            elif user_input == "3":
                # Si l'entrée de l'utilisateur est "3", un autre sous-menu sera affiché.

                while True:
                    user_input = self.get_user_entry(
                        msg_display=f"{Fore.GREEN}\n************************************\n"
                                    "       Voir le classement :\n"
                                    "************************************\n"
                                    f"{Style.RESET_ALL}"
                                    "[0] - Par rang\n"
                                    "[1] - Par ordre alphabétique\n"
                                    "[2] - Par ordre d'enregistrement\n"
                                    f"{Fore.YELLOW}[r] - Retour\n{Style.RESET_ALL}"
                                    "\n>>> ",
                        msg_error=f"{Fore.RED}Veuillez faire un choix valide.\n{Style.RESET_ALL}",
                        value_type="selection",
                        assertions=["0", "1", "2", "r", "R"]
                    )
                    # C'est l'invite qui est affichée à l'utilisateur pour obtenir une entrée. L'utilisateur peut
                    # entrer "0" pour gérer les joueurs, "1" pour gérer les tournois ou "r" pour revenir au menu
                    # précédent.

                    if user_input == "r":
                        break
                    # Si l'entrée de l'utilisateur est "r", la boucle est rompue et l'utilisateur retourne au menu
                    # précédent.

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

            elif user_input == "4":
                Report().display_tournaments_reports()

            else:
                quit()
            # Si l'utilisateur entre autre chose que les options proposées, le programme se termine.

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
        # Une fois un tournoi choisi ou créé, l'utilisateur est invité à jouer le tournoi ou à quitter le programme.
        # Si l'utilisateur choisit de jouer, le tournoi commence.

        print(f"{Fore.GREEN}  Tournoi {tournament.name} terminé !\n{Style.RESET_ALL}")
        print(f"{Fore.BLUE}      Voici les résultats : \n{Style.RESET_ALL}")

        for i, player in enumerate(rankings):
            print(f"{str(i + 1)} - {player}")
        # Une fois le tournoi terminé, les résultats sont affichés.

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
        # Enfin, l'utilisateur a le choix de mettre à jour les classements automatiquement ou manuellement. Si
        # l'utilisateur choisit l'option automatique, le programme met à jour les classements pour lui. Si
        # l'utilisateur choisit l'option manuelle, il est invité à entrer les classements pour chaque joueur.

        else:
            quit()
        #    Si l'utilisateur entre autre chose que les options proposées, le programme se termine.
