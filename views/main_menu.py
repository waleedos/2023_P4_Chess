from colorama import Fore, Style, init

# Importation des fonctions save_db et load_tournament à partir du module database.py existant dans le dossier
# "controller". Ces fonctions seront utilisées pour interagir avec la base de données du tournoi, avec les
# joueurs et les classements.
from controller.database import save_db, load_tournament

# Importation de la fonction update_rankings à partir du module player.py existant dans le dossier
# "controller". Cette fonction sera utilisée pour interagir avec la base de données du tournoi, avec les
# joueurs et les classements.
from controller.player import update_rankings

# Importation des fonctions create_tournament et play_tournament à partir du module tournament.py existant dans
# le dossier "controller". Ces fonctions seront utilisées pour interagir avec la base de données du tournoi,
# avec les joueurs et les classements.
from controller.tournament import create_tournament, play_tournament

# Importation de 4 classes spécifiques à partir de différents modules existants dans le dossier"views". Ces classes
# vont fournir des interfaces utilisateur pour l'interaction avec l'utilisateur.
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
                            "0 - Nouveau tournoi\n"
                            "1 - Charger un tournoi\n"
                            "2 - Créer des nouveaux joueurs\n"
                            "3 - Listes (joueurs, tournois)\n"
                            "Q - Quitter\n"
                            ">>> ",
                msg_error=f"{Fore.RED}Veuillez entrer une valeur valide\n{Style.RESET_ALL}",
                value_type="selection",
                assertions=["0", "1", "2", "3", "Q", "q"]
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
                                ">>> ",
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
                        # Une boucle infinie est initiée pour recevoir des entrées utilisateur jusqu'à ce que
                        # l'utilisateur décide de sortir.

                        msg_display="0 - Joueurs\n"
                                    "1 - Tournois\n"
                                    "r - Retour\n"
                                    ">>> ",
                        msg_error=f"{Fore.RED}Veuillez faire un choix valide.\n{Style.RESET_ALL}",
                        value_type="selection",
                        assertions=["0", "1", "r"]
                    )
                    # C'est l'invite qui est affichée à l'utilisateur pour obtenir une entrée. L'utilisateur peut
                    # entrer "0" pour gérer les joueurs, "1" pour gérer les tournois ou "r" pour revenir au menu
                    # précédent.

                    if user_input == "r":
                        break
                    # Si l'entrée de l'utilisateur est "r", la boucle est rompue et l'utilisateur retourne au menu
                    # précédent.

                    elif user_input == "0":
                        while True:
                            user_input = self.get_user_entry(
                                msg_display=f"{Fore.GREEN}************************************\n"
                                            "       Voir le classement :\n"
                                            "************************************\n"
                                            f"{Style.RESET_ALL}"
                                            "0 - Par rang\n"
                                            "1 - Par ordre alphabétique\n"
                                            "r - Retour\n"
                                            ">>> ",
                                msg_error=f"{Fore.RED}Veuillez faire un choix valide.\n{Style.RESET_ALL}",
                                value_type="selection",
                                assertions=["0", "1", "r", "R"]
                            )
                            # Si l'entrée de l'utilisateur est "0", un autre sous-menu sera affiché pour gérer les
                            # joueurs ; Une autre boucle infinie est initiée pour recevoir des entrées utilisateur
                            # jusqu'à ce que l'utilisateur décide de sortir ; C'est l'invite qui est affichée à
                            # l'utilisateur pour obtenir une entrée. L'utilisateur peut entrer "0" pour voir le
                            # classement par rang, "1" pour voir le classement par ordre alphabétique ou "r" pour
                            # revenir au menu précédent.

                            if user_input == "r":
                                break
                            # Si l'entrée de l'utilisateur est "r", la boucle est rompue et l'utilisateur retourne au
                            # menu précédent.
                            elif user_input == "0":
                                sorted_players = Report().sort_players(Report().players, by_rank=True)
                                # Si l'entrée de l'utilisateur est "0", les joueurs sont triés par rang en utilisant la
                                # méthode sort_players.

                                if not sorted_players:
                                    print("Oups... Aucun joueur n'est enregistré dans la base")
                                    break
                                    # Si la liste des joueurs triés est vide, un message d'erreur est affiché et
                                    # l'utilisateur retourne au menu précédent.
                                Report().display_players_report(players=sorted_players)

                            elif user_input == "1":
                                sorted_players = Report().sort_players(Report().players, by_rank=False)
                                if not sorted_players:
                                    print("Oups... Aucun joueur n'est enregistré dans la base")
                                    break
                                Report().display_players_report(players=sorted_players)

                    elif user_input == "1":
                        Report().display_tournaments_reports()
            else:
                quit()
            # Si l'utilisateur entre autre chose que les options proposées, le programme se termine.

        user_input = self.get_user_entry(
            msg_display=f"{Fore.GREEN}Que faire ?\n{Style.RESET_ALL}"
                        "0 - Jouer le tournoi\n"
                        "q - Quitter\n"
                        ">>> ",
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
                        "\n0 - Automatiquement\n"
                        "1 - Manuellement\n"
                        "Q - Quitter\n"
                        ">>> ",
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
