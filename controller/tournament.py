# Importation de laa classe Tournament du module tournament situé dans le dossier models
from models.tournament import Tournament

# Importation de la classe View du module view situé dans le dossier views
from views.view import View

# Importation de la classe CreateTournament du module tournament situé dans le dossier views
from views.tournament import CreateTournament

# Importation de la classe LoadPlayer du module player situé dans le dossier views.
from views.player import LoadPlayer

# Importation des fonctions create_player et update_rankings du module player situé dans le dossier controller
from controller.player import create_player, update_rankings

# Importation des fonctions save_db, update_db et load_player du module database situé dans le dossier controller.
from controller.database import save_db, update_db, load_player


def create_tournament():

    menu = View()
    user_entries = CreateTournament().display_menu()
    # Ici, un objet View est instancié pour interagir avec l'utilisateur et le menu de création de tournoi est
    # affiché pour recueillir les entrées de l'utilisateur.

    user_input = menu.get_user_entry(
        msg_display="Que faire ?\n"
                    "0 - Créer des joueurs\n"
                    "1 - Charger des joueurs\n"
                    ">>> ",
        msg_error="Entrez un choix valide",
        value_type="selection",
        assertions=["0", "1"]
    )
    # Une entrée utilisateur est demandée à l'aide de la méthode get_user_entry de l'objet View. L'utilisateur peut
    # choisir de créer de nouveaux joueurs ou de charger des joueurs existants.

    players = []
    # Une liste vide players est initialisée pour stocker les joueurs du tournoi.

    if user_input == "1":

        print(f"Chargement de {str(user_entries['nb_players'])} joueurs")

        serialized_players = LoadPlayer().display_menu(
            nb_players_to_load=user_entries['nb_players']
        )

        for serialized_player in serialized_players:
            player = load_player(serialized_player)
            players.append(player)
        # Si l'utilisateur a choisi de charger des joueurs existants.., le programme imprime le nombre de joueurs à
        # charger, affiche le menu de chargement de joueurs, et pour chaque joueur sérialisé, il le charge et
        # l'ajoute à la liste players.

    else:
        print(f"Création de {str(user_entries['nb_players'])} joueurs")

        while len(players) < user_entries['nb_players']:
            players.append(create_player())
        # Si l'utilisateur a choisi de créer de nouveaux joueurs, le programme imprime le nombre de joueurs à créer,
        # puis continue à créer des joueurs jusqu'à atteindre le nombre requis.

    if not players:
        print("Il n'y a aucun joueur, veuillez en créer")
        print()
        print(f"Création de {str(user_entries['nb_players'])} joueurs")
        while len(players) < user_entries['nb_players']:
            players.append(create_player())
        # Si aucun joueur n'a été créé ou chargé, le programme informe l'utilisateur qu'il doit en créer, puis crée
        # des joueurs jusqu'à atteindre le nombre requis.

    tournament = Tournament(
        user_entries['name'],
        user_entries['location'],
        user_entries['date'],
        user_entries['time_control'],
        players,
        user_entries['nb_rounds'],
        user_entries['desc'])

    save_db("tournaments", tournament.get_serialized_tournament())
    # Ici, un nouvel objet Tournament est créé avec les entrées de l'utilisateur et les joueurs. Ensuite, le tournoi
    # est sérialisé et sauvegardé dans la base de données. Enfin, l'objet Tournament est renvoyé.

    return tournament
    # Cette fonction create_tournament utilise les objets View, CreateTournament et LoadPlayer pour
    # afficher un menu permettant à l'utilisateur de créer un tournoi. En fonction de l'entrée de l'utilisateur,
    # des joueurs sont créés ou chargés à partir de la base de données. Si aucun joueur n'est créé ou chargé,
    # l'utilisateur est invité à créer des joueurs. Un objet Tournament est créé en utilisant la classe Tournament
    # importée précédemment, et le tournoi est sauvegardé dans la base de données à l'aide de la fonction save_db du
    # module database. Finalement, l'objet Tournament est renvoyé.


def play_tournament(tournament, new_tournament_loaded=False):
    # Cette ligne définit la fonction play_tournament qui prend deux paramètres : un objet tournament et un booléen
    # new_tournament_loaded qui indique si un nouveau tournoi a été chargé.

    menu = View()
    print()
    print(f"Début du tournoi {tournament.name}")
    print()
    # Un nouvel objet View est instancié pour interagir avec l'utilisateur. Ensuite, le nom du tournoi est affiché
    # pour indiquer le début du tournoi.

    while True:
        # Une boucle infinie commence. Cela permet au tournoi de continuer à tourner jusqu'à ce qu'il soit explicitement
        # arrêté.

        a = 0
        if new_tournament_loaded:
            for round in tournament.list_round:
                if round.end_date is None:
                    a += 1
            nb_rounds_to_play = tournament.rounds_number - a
            new_tournament_loaded = False
        else:
            nb_rounds_to_play = tournament.rounds_number
        # Si un nouveau tournoi a été chargé, le programme compte le nombre de rounds sans date de fin (qui sont donc
        # encore en cours) et déduit ce nombre du nombre total de rounds pour obtenir le nombre de rounds à jouer. Si
        # aucun nouveau tournoi n'a été chargé, le nombre de rounds à jouer est simplement le nombre total de rounds.

        for i in range(nb_rounds_to_play):

            tournament.create_round(round_number=i+a)

            current_round = tournament.list_round[-1]
            print(f"{current_round.start_date} : Début du {current_round.name}")
        # Pour chaque round à jouer, un nouveau round est créé et le round actuel est récupéré. Ensuite, le début du
        # round est annoncé.

            while True:
                print()
                user_input = menu.get_user_entry(
                    msg_display="Faîtes votre choix :\n"
                                "0 - Round suivant\n"
                                "1 - Voir les classements\n"
                                "2 - Mettre à jour les classements\n"
                                "3 - Sauvegarder le tournoi\n"
                                "Q - Quitter\n"
                                ">>> ",
                    msg_error="Veuillez faire un choix.",
                    value_type="selection",
                    assertions=["0", "1", "2", "3", "q", "Q"]
                )

                if user_input == "0":
                    current_round.mark_as_complete()
                    break
                # Dans cette boucle interne infinie, l'utilisateur est invité à faire un choix parmi les options
                # affichées ; Si l'utilisateur choisit "0", le round actuel est marqué comme terminé et la boucle
                # interne se termine, passant au round suivant.

                elif user_input == "1":
                    print(f"Classement du tournoi {tournament.name} :\n")
                    for j, player in enumerate(tournament.get_rankings()):
                        print(f"{str(j + 1)} - {player}")
                # Si l'utilisateur choisit "1", le classement du tournoi est affiché.

                elif user_input == "2":
                    for player in tournament.players:
                        rank = menu.get_user_entry(
                            msg_display=f"Rang de {player}:\n>>> ",
                            msg_error="Veuillez entrer un nombre entier.",
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
            # Si un nouveau tournoi a été chargé pendant la lecture du tournoi actuel, la boucle des rounds se termine
            # pour permettre au nouveau tournoi d'être lu.

        if new_tournament_loaded:
            continue
        # Si un nouveau tournoi a été chargé, la boucle principale du tournoi continue pour charger le nouveau
        # tournoi.

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
    # En conclusion, la fonction play_tournament est définie. Elle prend les paramètres tournament (l'objet Tournament
    # à jouer) et new_tournament_loaded (un booléen indiquant si un nouveau tournoi a été chargé). La fonction utilise
    # l'objet View pour afficher des messages et interagir avec l'utilisateur. Elle itère sur les rounds du tournoi en
    # utilisant la méthode create_round de l'objet Tournament. Elle affiche les informations du round en cours et
    # invite l'utilisateur à faire un choix parmi plusieurs options (marquer le round comme terminé, afficher les
    # classements, mettre à jour les classements, sauvegarder le tournoi ou quitter). Selon l'entrée de
    # l'utilisateur, différentes actions sont effectuées, telles que marquer le round comme terminé, afficher les
    # classements, mettre à jour les classements ou sauvegarder le tournoi. Une fois que tous les rounds ont été
    # joués, les classements finaux sont obtenus à l'aide de la méthode get_rankings de l'objet Tournament, et le
    # tournoi est mis à jour dans la base de données à l'aide de la fonction update_db du module database.
    # Finalement, les classements finaux sont renvoyés.
