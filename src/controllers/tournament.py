"""class TournamentController"""

from .common import clean_lower, clean_upper, clean_tournament, data, int_converter
from src.views.tournament import TournamentView
from src.models.player import Players
from src.models.tournament import Tournaments
from src.models.round import SCORE


class TournamentController:
    def __init__(self, view=TournamentView()):
        self.view = view

    def run(self):
        """tournament menu"""

        if len(Tournaments.read()) < 2:
            preview = str(len(Tournaments.read())) + " tournament created in system."
        else:
            preview = str(len(Tournaments.read())) + " tournaments created in system."

        choice = self.view.menu(preview)

        if choice == "1":
            """list"""

            self.view.list_tournaments(Tournaments.read(), "created")
            self.run()

        elif choice == "2":
            """select"""

            choice_2_1 = clean_upper(self.view.select1())
            if choice_2_1 in Tournaments.read_names():
                while True:
                    tournament2 = Tournaments.load(choice_2_1)

                    """run the next round"""

                    if tournament2.rounds_status() and tournament2.status != "finished":
                        choice_2_2 = self.view.select_round(
                            data(tournament2),
                            tournament2.full_player_ranking(),
                            tournament2.current_round,
                        )
                        if clean_lower(choice_2_2) == "y":
                            tournament2.draw_round()
                        else:
                            break

                    """ update match result """

                    if (
                        not tournament2.rounds_status()
                        and tournament2.status != "finished"
                    ):
                        """display the running round"""

                        choice_2_3 = self.view.select_match(
                            data(tournament2),
                            tournament2.full_player_ranking(),
                            tournament2.get_matchs_list(),
                        )
                        if clean_lower(choice_2_3) == "y":
                            """get the number of match and the score"""

                            choice_2_4 = self.view.select_result()
                            """ check the number of match """

                            if (
                                (choice_2_4[0].isdigit())
                                and (0 < int(choice_2_4[0]))
                                and (
                                    int(choice_2_4[0])
                                    <= len(tournament2.get_matchs_list())
                                )
                            ):
                                choice_2_4[0] = int(choice_2_4[0])
                                """ check the score """

                                if (choice_2_4[1].replace(".", "").isdigit()) and (
                                    choice_2_4[2].replace(".", "").isdigit()
                                ):
                                    choice_2_4[1] = float(choice_2_4[1])
                                    choice_2_4[2] = float(choice_2_4[2])
                                    if (
                                        (choice_2_4[1] in SCORE)
                                        and (choice_2_4[2] in SCORE)
                                        and (choice_2_4[1] + choice_2_4[2] == 1)
                                    ):
                                        choice_2_4[1] = int_converter(choice_2_4[1])
                                        choice_2_4[2] = int_converter(choice_2_4[2])

                                        """ update the match result and the player ranking """

                                        tournament2.update_match_result(
                                            choice_2_4[0] - 1,
                                            choice_2_4[1],
                                            choice_2_4[2],
                                        )
                                        tournament2.update_players_score()

                                    else:
                                        self.view.select_result_response(True, False)

                                else:
                                    self.view.select_result_response(True, False)

                            else:
                                self.view.select_result_response(False, False)

                        else:
                            break

                    """ finished tournament """

                    if tournament2.status == "finished":
                        self.view.select_end(
                            data(tournament2), tournament2.full_player_ranking()
                        )
                        break

            else:
                self.view.edit_response(False)

            self.run()

        elif choice == "3":
            """create"""

            while True:
                """check the number of players in the system"""

                if len(Players.read()) >= 4:
                    choice_3_1 = self.view.create()
                    choice_3_1 = clean_tournament(choice_3_1)
                else:
                    self.view.create_response1()
                    break

                """get and check the unicity of the tournament name"""

                if choice_3_1[0] not in Tournaments.read_names():
                    tournament = Tournaments(choice_3_1[0], choice_3_1[1])
                    tournament.description = choice_3_1[2]
                else:
                    self.view.create_response2(False, False)
                    break

                """ get and check the number of players to add """

                choice_3_2 = clean_upper(self.view.add_player1(len(Players.read())))
                if (
                    choice_3_2.isdigit()
                    and (4 <= int(choice_3_2))
                    and (int(choice_3_2) <= len(Players.read()))
                ):
                    choice_3_2 = int(choice_3_2)
                    self.view.list_players(Players.read())
                else:
                    self.view.add_player_response1()
                    break

                """ get the players ine list to add and check how many of them have been added """

                choice_3_3 = self.view.add_player2(choice_3_2)

                added_players = tournament.add_players_list(list(set(choice_3_3)))
                if added_players >= 4:
                    if added_players == choice_3_2:
                        self.view.add_player_response2(
                            True,
                            True,
                            added_players,
                            choice_3_2,
                        )
                    elif added_players < choice_3_2:
                        self.view.add_player_response2(
                            True,
                            False,
                            added_players,
                            choice_3_2,
                        )
                    tournament.create()
                    self.view.create_response2(True, True)
                    break
                else:
                    self.view.create_response2(True, False)
                    break

            self.run()

        elif choice == "4":
            """edit"""

            choice_4_1 = self.view.edit()
            choice_4_1 = clean_tournament(choice_4_1)
            if choice_4_1[0] in Tournaments.read_names():
                tournament4 = Tournaments.load(choice_4_1[0])
                tournament4.place = choice_4_1[1]
                tournament4.description = choice_4_1[2]
                tournament4.update()
                self.view.edit_response(True)
            else:
                self.view.edit_response(False)

            self.run()

        elif choice == "5":
            """delete"""

            choice_5_1 = clean_upper(self.view.delete())
            if choice_5_1 in Tournaments.read_names():
                choice_5_2 = clean_lower(self.view.delete_response1())

                if choice_5_2 == "y":
                    tournament5 = Tournaments.load(choice_5_1)
                    tournament5.delete()
                    self.view.delete_response2()

            else:
                self.view.edit_response(False)

            self.run()

        elif choice == "6":
            """Back to Home Menu"""

            return "exit"

        else:
            """invalid choice"""

            self.run()
