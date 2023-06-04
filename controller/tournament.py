from colorama import Fore, Style, init
from models.tournament import Tournament
from views.view import View
from views.tournament import CreateTournament
from views.player import LoadPlayer
from controller.player import create_player, update_rankings
from controller.database import save_db, update_db, load_player

init()


def create_tournament():
    # La fonction create_tournament est définie. Cette fonction n'a pas de paramètres.

    menu = View()
    # Une instance de la classe View est créée et stockée dans la variable menu. Cela repose sur la classe View qui est
    # déjà définie ailleurs dans le code, plus précisement dans le fichier /views/view.py.

    user_entries = CreateTournament().display_menu()
    # Une instance de la classe CreateTournament est créée et sa méthode display_menu est appelée pour obtenir les
    # entrées de l'utilisateur. Les entrées obtenues sont stockées dans la variable user_entries.

    user_input = menu.get_user_entry(
        # La méthode get_user_entry de l'objet menu est appelée pour obtenir une entrée de l'utilisateur. Cette entrée
        # est stockée dans la variable user_input.

        msg_display=f"{Fore.GREEN}Que faire ?\n{Style.RESET_ALL}"
                    "[0] - Créer des joueurs\n"
                    "[1] - Charger des joueurs\n"
                    "\n>>> ",
        msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
        value_type="selection",
        assertions=["0", "1"]
    )
    # La méthode get_user_entry est appelée avec quatre arguments. msg_display est le message à afficher à
    # l'utilisateur, msg_error est le message d'erreur à afficher en cas de saisie invalide, value_type est le type de
    # valeur attendu, et assertions est une liste de valeurs valides.

    players = []
    # Une liste vide est créée et stockée dans la variable players. Cette liste contiendra les joueurs du tournoi.

    if user_input == "1":
        # Si l'utilisateur a choisi de charger des joueurs (c'est-à-dire si user_input est "1"), alors on exécute le
        # bloc de code qui suit.

        print(f"{Fore.GREEN}Chargement de {str(user_entries['nb_players'])} joueurs\n{Style.RESET_ALL}")
        # Un message est affiché à l'utilisateur pour lui indiquer que les joueurs sont en cours de chargement.

        serialized_players = LoadPlayer().display_menu(
            nb_players_to_load=user_entries['nb_players']
        )
        # Une instance de la classe LoadPlayer est créée et sa méthode display_menu est appelée avec un argument pour
        # obtenir une liste de joueurs sérialisés. Cette liste est stockée dans la variable serialized_players.

        for serialized_player in serialized_players:
            player = load_player(serialized_player)
            players.append(player)
            # Chaque joueur sérialisé dans serialized_players est chargé à l'aide de la fonction load_player, puis
            # ajouté à la liste players.

    else:
        # Si l'utilisateur n'a pas choisi de charger des joueurs (c'est-à-dire si user_input n'est pas "1"), alors on
        # exécute le bloc de code qui suit.

        print(f"{Fore.GREEN}Création de {str(user_entries['nb_players'])} joueurs\n{Style.RESET_ALL}")
        # Un message est affiché à l'utilisateur pour lui indiquer que les joueurs sont en cours de création.

        while len(players) < user_entries['nb_players']:
            players.append(create_player())
            # Des joueurs sont créés en utilisant la fonction create_player jusqu'à ce que le nombre de joueurs dans la
            # liste players atteigne le nombre de joueurs demandé par l'utilisateur.

    if not players:
        # Si la liste players est vide (c'est-à-dire qu'aucun joueur n'a été chargé ou créé), alors on exécute le bloc
        # de code qui suit.

        print(f"{Fore.RED}Il n'y a aucun joueur, veuillez en créer\n{Style.RESET_ALL}")
        # Un message d'erreur est affiché à l'utilisateur pour lui indiquer qu'il n'y a aucun joueur.

        print()
        print(f"{Fore.GREEN}Création de {str(user_entries['nb_players'])} joueurs\n{Style.RESET_ALL}")
        # Un message est affiché à l'utilisateur pour lui indiquer que les joueurs sont en cours de création.

        while len(players) < user_entries['nb_players']:
            players.append(create_player())
            # Des joueurs sont créés en utilisant la fonction create_player jusqu'à ce que le nombre de joueurs dans la
            # liste players atteigne le nombre de joueurs demandé par l'utilisateur.

    tournament = Tournament(
        user_entries['name'],
        user_entries['location'],
        user_entries['date'],
        user_entries['time_control'],
        players,
        user_entries['nb_rounds'],
        user_entries['desc'])
    # Une instance de la classe Tournament est créée avec les informations fournies par l'utilisateur et les joueurs
    # chargés ou créés. Cette instance est stockée dans la variable tournament.

    save_db("tournaments", tournament.get_serialized_tournament())
    # Le tournoi est sérialisé à l'aide de la méthode get_serialized_tournament de l'objet tournament, puis sauvegardé
    # dans la base de données sous le nom "tournaments" en utilisant la fonction save_db.

    return tournament
    # La fonction create_tournament renvoie l'objet tournament créé.


def play_tournament(tournament, new_tournament_loaded=False):
    # Définition de la fonction play_tournament est définie. Elle prend deux paramètres : tournament, qui est une
    # instance d'un tournoi, et new_tournament_loaded, qui est un booléen indiquant si un nouveau tournoi a été chargé.

    menu = View()
    # Une instance de la classe View est créée et stockée dans la variable menu.

    print()
    print(f"{Fore.RED}  Début du tournoi {tournament.name}\n{Style.RESET_ALL}")
    print()
    # Un message est affiché à l'utilisateur pour indiquer le début du tournoi.

    while True:
        # Nous démarrons une boucle while ici, C'est la boucle principale de la fonction.

        a = 0
        if new_tournament_loaded:
            for round in tournament.list_round:
                if round.end_date is None:
                    a += 1
            nb_rounds_to_play = tournament.rounds_number - a
            new_tournament_loaded = False
        else:
            nb_rounds_to_play = tournament.rounds_number
            # Le nombre de tours à jouer est calculé. Si un nouveau tournoi a été chargé, alors on déduit du nombre
            # total de tours le nombre de tours pour lesquels la date de fin n'est pas définie. Sinon, le nombre de
            # tours à jouer est égal au nombre total de tours.

        for i in range(nb_rounds_to_play):
            # Maintenant, une boucle est démarrée pour chaque tour à jouer.

            tournament.create_round(round_number=i+a)
            # Un tour est créé dans le tournoi. Le numéro du tour est égal à l'index de la boucle plus la variable a
            # qui contient le nombre de tours non terminés dans le tournoi chargé.

            current_round = tournament.list_round[-1]
            print(f"{Fore.BLUE}{current_round.start_date} : Début du {current_round.name}\n{Style.RESET_ALL}")
            # Le tour actuel est récupéré et le début du tour est annoncé.

            while True:
                # Une boucle infinie est démarrée. C'est la boucle du menu principal du tour.

                print()
                user_input = menu.get_user_entry(
                    # L'utilisateur est invité à faire un choix. Le choix de l'utilisateur est stocké dans la variable
                    # user_input.

                    msg_display=f"{Fore.GREEN}************************************\n"
                                "       Faîtes votre choix :\n"
                                "************************************\n"
                                f"{Style.RESET_ALL}"
                                "[0] - Round suivant\n"
                                "[1] - Voir les classements\n"
                                "[2] - Mettre à jour les classements\n"
                                "[3] - Sauvegarder le tournoi\n"
                                f"{Fore.RED}[Q] - Quitter\n{Style.RESET_ALL}"
                                "\n>>> ",
                    msg_error=f"{Fore.RED}Veuillez faire un choix.\n{Style.RESET_ALL}",
                    value_type="selection",
                    assertions=["0", "1", "2", "3", "q", "Q"]
                )
                # L'utilisateur est invité à faire un choix parmi les options suivantes : passer au prochain tour, voir
                # les classements, mettre à jour les classements, sauvegarder le tournoi ou quitter.

                if user_input == "0":
                    current_round.mark_as_complete()
                    break
                    # Si l'utilisateur choisit "0", le tour actuel est marqué comme terminé et on sort de la boucle du
                    # menu.

                elif user_input == "1":
                    print(f"{Fore.BLUE}Classement du tournoi {tournament.name} :\n{Style.RESET_ALL}")
                    for j, player in enumerate(tournament.get_rankings()):
                        print(f"{str(j + 1)} - {player}")
                # Si l'utilisateur choisit "1", le classement du tournoi est affiché.

                elif user_input == "2":
                    for player in tournament.players:
                        rank = menu.get_user_entry(
                            msg_display=f"Rang de {player}:\n>>> ",
                            msg_error=f"{Fore.RED}Veuillez entrer un nombre entier\n{Style.RESET_ALL}",
                            value_type="numeric"
                        )
                        update_rankings(player, rank, score=False)
                # Si l'utilisateur choisit "2", il est invité à mettre à jour les classements des joueurs.

                elif user_input == "3":
                    rankings = tournament.get_rankings()
                    for j, player in enumerate(rankings):
                        for t_player in tournament.players:
                            if player.name == t_player.name:
                                t_player.rank = str(j + 1)
                    update_db("tournaments", tournament.get_serialized_tournament(save_rounds=True))
                # Si l'utilisateur choisit "3", le tournoi est sauvegardé dans la base de données.

                elif user_input.upper() == "Q":
                    quit()
                # Si l'utilisateur choisit "Q", le programme se termine.

            if new_tournament_loaded:
                break
            # Si un nouveau tournoi a été chargé, on sort de la boucle du tour.

        if new_tournament_loaded:
            continue

        else:
            break
        # Si un nouveau tournoi a été chargé, on continue à la prochaine itération de la boucle principale. Sinon, on
        # sort de la boucle principale.

    rankings = tournament.get_rankings()
    for i, player in enumerate(rankings):
        for t_player in tournament.players:
            if player.name == t_player.name:
                t_player.total_score += player.tournament_score
                t_player.rating = str(i+1)
    update_db("tournaments", tournament.get_serialized_tournament(save_rounds=True))
    # Après la fin de tous les tours, le classement final est obtenu, les scores totaux et les classements des joueurs
    # sont mis à jour, et le tournoi est sauvegardé dans la base de données.

    return rankings
    # La fonction play_tournament renvoie le classement final du tournoi.
