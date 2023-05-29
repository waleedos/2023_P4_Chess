# Importation de la fonction  load_db du module database depuis le dossier controller, qui est utilisée pour lire des
# données à partir de la base de données.
from controller.database import load_db

# Importation de la Classe View du module view depuis le dossier views, qui est utilisée comme classe de base pour
# créer d'autres vues.
from views.view import View

# Importation de la fonction itemgetter du module operator qui facilite le tri des éléments dans une collection.
from operator import itemgetter


class Report(View):
    # Déclaration d'une nouvelle classe appelée Report, qui hérite de la classe View.

    def __init__(self):
        self.players = load_db("players")
        self.tournaments = load_db("tournaments")
        # Passage du constructeur de la classe Report. Il est appelé lorsque vous créez une nouvelle instance de cette
        # classe. load_db("players") et load_db("tournaments") sont appelés pour obtenir la liste des joueurs et des
        # tournois à partir de la base de données, et ces listes sont ensuite stockées dans les attributs self.players
        # et self.tournaments.

    def display_players_report(self, players=[]):
        # déclaration d'une méthode appelée display_players_report, qui prend en argument une liste de joueurs.
        # Cette liste est vide par défaut.

        players = players
        # Affectation de la liste de joueurs passée en argument à la variable locale players. Cependant, cette ligne
        # semble redondante, car players est déjà le nom de l'argument de la méthode.

        build_selection = self.build_selection(iterable=players, display_msg="Voir les détails d'un joueur :\n",
                                               assertions=["r"])
        # Ceci appelle la méthode build_selection avec trois arguments : la liste de joueurs, un message à afficher et
        # une liste d'assertions. On suppose que build_selection retourne un dictionnaire contenant une version mise en
        # forme de la liste de joueurs et la liste d'assertions. Ce dictionnaire est stocké dans la variable
        # build_selection.

        while True:
            print("Classement : ")
            # commencement d'une boucle infinie et affichage du message "Classement :".

            user_input = self.get_user_entry(
                msg_display=build_selection['msg'] + "r - Retour\n"
                                                     ">>> ",
                msg_error="Veuillez faire un choix valide",
                value_type="selection",
                assertions=build_selection['assertions']
            )
            # appel de la méthode get_user_entry avec quatre arguments : un message à afficher, un message d'erreur, le
            # type de valeur attendu et une liste d'assertions. On suppose que get_user_entry affiche le message, puis
            # attend une entrée de l'utilisateur. Si l'entrée de l'utilisateur est valide (c'est-à-dire si elle passe
            # toutes les assertions), alors cette entrée est retournée par la méthode. Sinon, le message d'erreur est
            # affiché et l'utilisateur est invité à entrer à nouveau une valeur. L'entrée de l'utilisateur est stockée
            # dans la variable user_input.

            if user_input == "r":
                break
            # Si l'entrée de l'utilisateur est "r", alors la boucle est interrompue et l'exécution de la méthode
            # continue à partir de la ligne suivant la boucle.

            else:
                selected_player = players[int(user_input) - 1]
                # Si l'entrée de l'utilisateur n'est pas "r", alors on suppose qu'elle est un entier sous forme de
                # chaîne de caractères. Cet entier est utilisé comme indice pour sélectionner un joueur dans la liste
                # de joueurs. L'indice est décrémenté de 1 car les indices en Python commencent à 0, alors que la
                # sélection de l'utilisateur commence probablement à 1. Le joueur sélectionné est stocké dans la
                # variable selected_player.

                while True:
                    print(f"Détails du joueur {selected_player['name']}:")
                    print(f"Classement: {selected_player['rating']}\n"
                          f"Score total: {selected_player['total_score']}\n"
                          f"Nom: {selected_player['name']}\n"
                          f"Prénom: {selected_player['firstname']}\n"
                          f"Date de naissance: {selected_player['birthday']}\n"
                          f"Sexe: {selected_player['gender']}\n"
                          )
                    # commence une autre boucle infinie. À chaque itération de la boucle, les détails du joueur
                    # sélectionné sont affichés. Les détails incluent le nom, le classement, le score total, le prénom,
                    # la date de naissance et le sexe du joueur.

                    user_input = self.get_user_entry(
                        msg_display="Que faire ?\n"
                                    "r - Retour\n"
                                    ">>> ",
                        msg_error="Veuillez faire un choix valide",
                        value_type="selection",
                        assertions=["r"]
                    )
                    # Ceci appelle à nouveau la méthode get_user_entry, mais cette fois avec un message différent et
                    # une seule assertion : "r".

                    if user_input == "r":
                        break
                    # Si l'entrée de l'utilisateur est "r", alors la boucle est interrompue et l'exécution de la
                    # méthode continue à partir de la ligne suivant la boucle.

    def display_tournaments_reports(self):
        # déclaration d'une nouvelle méthode appelée display_tournaments_reports, qui ne prend aucun argument.

        build_selection = self.build_selection(
            iterable=self.tournaments,
            display_msg="Voir les détails d'un tournoi :\n",
            assertions=['r']
        )
        # Appel de la méthode build_selection avec la liste de tournois, un message à afficher et une liste
        # d'assertions. Le résultat est stocké dans la variable build_selection.

        while True:
            # Commencement d'une autre boucle infinie.

            if not self.tournaments:
                print("Oups.. Aucun tournoi n'est enregistré dans la base")
                break
            # Si la liste des tournois est vide, alors un message est affiché et la boucle est interrompue.

            print("Tournois :")
            # Si la liste des tournois n'est pas vide, alors le message "Tournois :" est affiché.

            user_input = self.get_user_entry(
                msg_display=build_selection['msg'] + "r - Retour\n"
                                                     ">>> ",
                msg_error="Veuillez faire un choix valide.",
                value_type="selection",
                assertions=build_selection['assertions']
            )
            # Ceci appelle à nouveau la méthode get_user_entry, mais cette fois avec le message de build_selection et
            # ses assertions.

            if user_input == "r":
                break

            else:
                selected_tournament = self.tournaments[int(user_input) - 1]
                # Si l'entrée de l'utilisateur n'est pas "r", l'entrée est convertie en un entier et utilisée comme
                # indice pour sélectionner un tournoi dans la liste des tournois.

                while True:
                    print(f"Détails du tournoi {selected_tournament['name']}\n"
                          f"Nom: {selected_tournament['name']}\n"
                          f"Lieu: {selected_tournament['location']}\n"
                          f"Date: {selected_tournament['date']}\n"
                          f"Contrôle du temps: {selected_tournament['time_control']}\n"
                          f"Nombre de rounds: {selected_tournament['rounds_number']}\n"
                          f"Description: {selected_tournament['description']}\n"
                          )

                    user_input = self.get_user_entry(
                        msg_display="Que faire ?\n"
                                    "0 - Voir les participants\n"
                                    "1 - Voir les tours\n"
                                    "r - Retour\n>>> ",
                        msg_error="Veuillez entrer une sélection valide",
                        value_type="selection",
                        assertions=["0", "1", "2", "r", "R"]
                    )
                    # Un autre message est affiché à l'utilisateur, lui demandant ce qu'il souhaite faire ensuite.
                    # L'utilisateur a la possibilité de voir les participants, les tours ou de revenir au menu
                    # précédent.

                    if user_input == "r" or user_input == "R":
                        break

                    elif user_input == "0":
                        while True:
                            user_input = self.get_user_entry(
                                msg_display="Type de classement:\n"
                                            "0 - Par rang\n"
                                            "1 - Par ordre alphabétique\n"
                                            "r - Retour\n"
                                            ">>> ",
                                msg_error="Veuillez entrer une sélection valide",
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
                            # Si l'utilisateur choisit de voir les participants, un autre message est affiché,
                            # demandant comment afficher les joueurs : par rang ou par ordre alphabétique. En fonction
                            # du choix de l'utilisateur, la liste des joueurs est triée et affichée.

                    elif user_input == "1":
                        self.display_rounds(selected_tournament["list_round"])

    def display_rounds(self, rounds):
        # Nous utilisons cette methode pour afficher les détails des tours. Elle accepte une liste de tours en tant
        # que paramètre.

        build_selection = self.build_selection(
            iterable=rounds,
            display_msg="Voir les détails d'un round:\n",
            assertions=['r']
        )
        # Nous appelons la méthode build_selection avec trois paramètres : la liste des tours, un message à afficher et
        # une liste de valeurs acceptables pour l'entrée utilisateur.

        while True:
            print("Rounds:")
            # Un message "Rounds:" est affiché et une boucle infinie est lancée.

            user_input = self.get_user_entry(
                msg_display=build_selection['msg'] + "r - Retour\n"
                                                     ">>> ",
                msg_error="Veuillez faire un choix valide",
                value_type="selection",
                assertions=build_selection['assertions']
            )
            # Un prompt est affiché pour l'utilisateur, qui peut choisir un tour pour voir plus de détails ou taper "r"
            # pour retourner.

            if user_input == "r":
                break
            # Si l'utilisateur a entré "r", la boucle se termine et l'exécution reprend après la boucle.

            else:
                selected_round = rounds[int(user_input) - 1]
                # Si l'utilisateur a entré un nombre, ce nombre est converti en entier, décrémenté de 1, est utilisé
                # pour indexer la liste des tours pour sélectionner un tour.

                while True:
                    print(f"Détails du round {selected_round['name']}\n"
                          f"Nom: {selected_round['name']}\n"
                          f"Nombre de matchs: {len(selected_round['matchs'])}\n"
                          f"Date de début: {selected_round['start_date']}\n"
                          f"Date de fin: {selected_round['end_date']}\n"
                          )
                    # Une autre boucle infinie est lancée, et des détails sur le tour sélectionné sont affichés.

                    user_input = self.get_user_entry(
                        msg_display="Que faire ?\n"
                                    "0 - Voir les matchs\n"
                                    "r - Retour\n"
                                    ">>> ",
                        msg_error="Veuillez faire un choix valide",
                        value_type="selection",
                        assertions=["0", "r"]
                    )
                    # Un autre prompt est affiché à l'utilisateur, qui peut choisir de voir les détails des matchs du
                    # tour sélectionné ou taper "r" pour revenir.

                    if user_input == "r":
                        break
                        # Si l'utilisateur a entré "r", la boucle se termine et l'exécution reprend après la boucle.

                    else:
                        build_selection = self.build_selection(
                            iterable=selected_round['matchs'],
                            display_msg="Voir les détails d'un match\n",
                            assertions=['r']
                        )
                        # Si l'utilisateur a entré "0", la méthode build_selection est appelée pour préparer le prompt
                        # pour la sélection d'un match à afficher.

                        print("Matchs:")
                        user_input = self.get_user_entry(
                            msg_display=build_selection['msg'] + "r - Retour\n"
                                                                 ">>> ",
                            msg_error="Veuillez faire un choix valide.",
                            value_type="selection",
                            assertions=build_selection['assertions']
                        )
                        # Un message "Matchs:" est affiché et l'utilisateur est invité à choisir un match à voir ou à
                        # taper "r" pour revenir.

                        if user_input == "r":
                            break
                        else:
                            selected_match = selected_round['matchs'][int(user_input) - 1]
                            # Si l'utilisateur a entré un nombre, ce nombre est converti en entier, décrémenté de 1, et
                            # utilisé pour indexer la liste des matchs pour sélectionner un match.

                            while True:
                                print(f"Détails du {selected_match['name']}\n"
                                      f"Joueur 1 : " +
                                      f"{selected_match['player_1']['name']} ({selected_match['score_player_1']} pts)\n"
                                      f"Joueur 2 : " +
                                      f"{selected_match['player_2']['name']} ({selected_match['score_player_2']} pts)\n"
                                      f"Gagnant: {selected_match['winner']}\n"
                                      )
                                # Une autre boucle infinie est lancée, et des détails sur le match sélectionné sont
                                # affichés.

                                user_input = self.get_user_entry(
                                    msg_display="Que faire ?\n"
                                                "r - Retour\n"
                                                ">>> ",
                                    msg_error="Veuillez faire un choix valide",
                                    value_type="selection",
                                    assertions=["r"]
                                )
                                # Un autre prompt est affiché à l'utilisateur, qui peut choisir de retourner en
                                # tapant "r".

                                if user_input == "r":
                                    break

    @staticmethod
    def sort_players(players: list, by_rank: bool) -> list:

        if by_rank:
            sorted_players = sorted(players, key=itemgetter('rating'))
        else:
            sorted_players = sorted(players, key=itemgetter('name'))

        return sorted_players
        # Il s'agit d'une méthode statique qui trie une liste de joueurs par leur classement ou par leur nom, selon la
        # valeur du paramètre by_rank.
