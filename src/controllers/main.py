"""class MainController"""

import sys

from src.models.player import Players
from src.models.tournament import Tournaments
from src.models.round import Rounds

from src.controllers.homepage import HomepageController
from src.controllers.player import PlayerController
from src.controllers.report import ReportController
from src.controllers.tournament import TournamentController


class MainController:
    def __init__(
        self,
        homepage=HomepageController(),
        player=PlayerController(),
        report=ReportController(),
        tournament=TournamentController(),
    ):
        self.homepage = homepage
        self.player = player
        self.report = report
        self.tournament = tournament

    def run(self):
        running = True
        while running:
            """homepage controller"""

            choice = self.homepage.run()

            if choice == "1":
                """player controller"""

                if self.player.run() == "exit":
                    self.run()

            if choice == "2":
                """tournament controller"""

                if self.tournament.run() == "exit":
                    self.run()

            if choice == "3":
                """report controller"""

                if self.report.run() == "exit":
                    self.run()

            elif choice == "4":
                """exit game"""

                Players.db().close()
                Tournaments.db().close()
                Rounds.db().close()
                running = False
                sys.exit()

            else:
                """invalid choice"""

                self.run()
