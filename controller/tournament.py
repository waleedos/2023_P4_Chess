from colorama import Fore, Style, init
from models.tournament import Tournament
from views.view import View
from views.tournament import CreateTournament
from views.player import LoadPlayer
from controller.player import create_player, update_rankings
from controller.database import save_db, update_db, load_player

init()


def create_tournament():

    menu = View()
    user_entries = CreateTournament().display_menu()

    user_input = menu.get_user_entry(
        msg_display=f"{Fore.GREEN}Que faire ?\n{Style.RESET_ALL}"
                    "[0] - Créer des joueurs\n"
                    "[1] - Charger des joueurs\n"
                    "\n>>> ",
        msg_error=f"{Fore.RED}Veuillez faire un choix valide\n{Style.RESET_ALL}",
        value_type="selection",
        assertions=["0", "1"]
    )

    players = []

    if user_input == "1":

        print(f"{Fore.GREEN}Chargement de {str(user_entries['nb_players'])} joueurs\n{Style.RESET_ALL}")

        serialized_players = LoadPlayer().display_menu(
            nb_players_to_load=user_entries['nb_players']
        )

        for serialized_player in serialized_players:
            player = load_player(serialized_player)
            players.append(player)
    else:
        print(f"{Fore.GREEN}Création de {str(user_entries['nb_players'])} joueurs\n{Style.RESET_ALL}")

        while len(players) < user_entries['nb_players']:
            players.append(create_player())

    if not players:
        print(f"{Fore.RED}Il n'y a aucun joueur, veuillez en créer\n{Style.RESET_ALL}")
        print()
        print(f"{Fore.GREEN}Création de {str(user_entries['nb_players'])} joueurs\n{Style.RESET_ALL}")
        while len(players) < user_entries['nb_players']:
            players.append(create_player())

    tournament = Tournament(
        user_entries['name'],
        user_entries['location'],
        user_entries['date'],
        user_entries['time_control'],
        players,
        user_entries['nb_rounds'],
        user_entries['desc'])

    save_db("tournaments", tournament.get_serialized_tournament())

    return tournament


def play_tournament(tournament, new_tournament_loaded=False):

    menu = View()
    print()
    print(f"{Fore.RED}  Début du tournoi {tournament.name}\n{Style.RESET_ALL}")
    print()

    while True:

        a = 0
        if new_tournament_loaded:
            for round in tournament.list_round:
                if round.end_date is None:
                    a += 1
            nb_rounds_to_play = tournament.rounds_number - a
            new_tournament_loaded = False
        else:
            nb_rounds_to_play = tournament.rounds_number

        for i in range(nb_rounds_to_play):

            tournament.create_round(round_number=i+a)

            current_round = tournament.list_round[-1]
            print(f"{Fore.BLUE}{current_round.start_date} : Début du {current_round.name}\n{Style.RESET_ALL}")
        # Pour chaque round à jouer, un nouveau round est créé et le round actuel est récupéré. Ensuite, le début du
        # round est annoncé.

            while True:
                print()
                user_input = menu.get_user_entry(
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

                if user_input == "0":
                    current_round.mark_as_complete()
                    break
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

        if new_tournament_loaded:
            continue

        else:
            break

    rankings = tournament.get_rankings()
    for i, player in enumerate(rankings):
        for t_player in tournament.players:
            if player.name == t_player.name:
                t_player.total_score += player.tournament_score
                t_player.rating = str(i+1)
    update_db("tournaments", tournament.get_serialized_tournament(save_rounds=True))

    return rankings
