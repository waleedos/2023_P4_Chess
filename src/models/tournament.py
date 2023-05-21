""" class Tournaments """

import logging


from tinydb import TinyDB, where
import pandas as pd

from .common import remove_file, round_non_existence, timestamp
from .player import Players
from .round import Rounds


class Tournaments:
    def __init__(
        self,
        name: str,
        place: str,
        start_date=timestamp(),
        end_date="(not finished)",
        status="created",
        description="",
        players_score={},
        number_of_rounds=4,
        current_round=0,
        rounds_list=[],
    ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.description = description
        self.players_score = players_score
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.rounds_list = rounds_list

    def __str__(self):
        """used in print"""

        return f"{self.__dict__}"

    def __repr__(self):
        """used in print"""

        return str(self)

    @classmethod
    def db(self):
        """Create a JSON file as database"""

        return TinyDB("./data/tournaments/tournaments.json")

    @classmethod
    def table(self):
        """Create 'Tournaments' table in database"""

        return self.db().table("Tournaments")

    def create(self):
        """Create a new tournament in Tournaments table"""

        self.table().insert(self.__dict__)

    @classmethod
    def find(self, tournament_name: str) -> list:
        """Look for a tournament in table by its name"""

        return self.table().search(where("name") == tournament_name)

    @classmethod
    def load(self, tournament_name: str):
        """load tournament instance from its name in json"""

        if len(self.find(tournament_name)) > 0:
            tournament = self.find(tournament_name)[0]

            return Tournaments(**tournament)
        else:
            return []

    def update(self):
        """update tournament data in json by its name"""

        self.table().update(
            self.__dict__,
            where("name") == self.name,
        )

    def delete(self):
        """delete a tournament and its rounds in json"""

        [Rounds.load(round_name).delete() for round_name in self.rounds_list]
        self.table().remove(where("name") == self.name)

    @classmethod
    def read(self) -> list:
        """return the tournaments' data list"""

        return self.table().all()

    @classmethod
    def read_names(self) -> list:
        """return the tournaments' name list"""

        return [tournament["name"] for tournament in Tournaments.read()]

    def players(self) -> list:
        """return tournament players list with all its attributes"""

        players = []
        i = 1
        for player in self.players_rank():
            p = Players.find(player)
            players.append(
                {
                    "rank": str(i),
                    "score": self.players_score[player],
                    "last_name": p[0]["last_name"],
                    "first_name": p[0]["first_name"],
                    "birthdate": p[0]["birthdate"],
                    "ine": p[0]["ine"],
                    "tournament": self.name,
                    "status": self.status,
                    "round": self.current_round,
                }
            )
            i += 1

        return sorted(players, key=lambda p: (p["last_name"]))

    def add_players_list(self, players_ine: list) -> int:
        """add a players list to a tournament instance and database

        only, if player exists in 'Players' table and not exists in the tournament

        return the number of players added"""

        if self.status == "created":
            added_players = 0
            players_score = {}
            for ine in players_ine:
                if ine in Players.ine_list():
                    if ine not in self.players_rank():
                        players_score[ine] = 0
                        added_players += 1

            self.players_score = players_score

            return added_players
        else:
            logging.error(
                "It is impossible to add players in a running or finished tournament !"
            )

    def update_match_result(
        self,
        index_of_match: int,
        player1_score: float,
        player2_score: float,
        index_of_round: int = -1,
    ):
        """update a match score of the current round
        update round status if the current round is finished
        update the tournament status if the tournament is finished"""

        try:
            round = Rounds.load(self.rounds_list[index_of_round])
        except IndexError:
            round_non_existence()

        try:
            round.update_match_result(index_of_match, player1_score, player2_score)
            round.state()
            round.update()
            self.state()
        except UnboundLocalError:
            round_non_existence()

    def rounds_status(self) -> bool:
        """check if all created rounds of the tournament are finished

        return a boolean: True if all round are finished, False for the reverse"""

        return Rounds.rounds_status(self.rounds_list)

    def update_players_score(self):
        """update players_score and update database if all created rounds are finished"""

        if self.rounds_status():
            self.players_score = Rounds.update_players_score(
                self.players_rank(), self.rounds_list
            )

            self.update()
        else:
            logging.info(
                "All created rounds must be finished to update the players score !"
            )

    def players_rank(self) -> list:
        """generate players ine list sorted by rank"""

        return [
            p[0]
            for p in sorted(list(self.players_score.items()), key=lambda p: (-p[1]))
        ]

    def state(self) -> bool:
        """Verify the tournament status and update it if it has concluded

        return True if the tournament is finished"""

        if self.rounds_status() and self.current_round == self.number_of_rounds:
            self.status = "finished"
            self.end_date = timestamp()
            self.update()
            return True
        else:
            return False

    def draw_round(self):
        """call 'first_round' class method if tournament is 'created' or current_round >= number of players -1

        call 'next_round' class method if tournament is 'running' and current_round < number of players -1
        """

        if self._first_round_conditions():
            self._first_round()
            logging.info("'first_round' class method is used")

        if self._next_round_conditions():
            self._next_round()
            logging.info("'next_round' class method is used")

    def full_player_ranking(self):
        """return the list of player ranking with all its attributes"""

        return sorted(self.players(), key=lambda p: (p["rank"]))

    def get_matchs_list(self) -> list:
        """return the matchs_list of the current round if there are still onging matchs"""

        round = Rounds.load(self.rounds_list[-1])
        if not round.state():
            matchs_list = round.get_matchs_list()
            return matchs_list
        else:
            return []

    """  class methode for report """

    def players_name_report(self) -> list:
        """Export the tournament players list sorted by last-name as a report (.xlsx)
        and return a list of it."""

        data_to_export = pd.DataFrame.from_records([row for row in self.players()])
        file_path = (
            "./data/exports/tournament_(" + self.name + ")_players_name_report.xlsx"
        )
        remove_file(file_path)
        data_to_export.to_excel(file_path)

        return self.players()

    @classmethod
    def report(self, tournament_name="") -> list:
        """export tournaments data as a report (.xlsx) and return a list of it (tournament_name="")
        else export the tourmanent data as a report (.xlsx) and return a list of it"""

        if (tournament_name == "") or tournament_name in self.read_names():
            data = [tournament for tournament in self._data(tournament_name)]
            if len(tournament_name) > 0:
                file_path = (
                    "./data/exports/tournament_" + data[0]["name"] + "_report_.xlsx"
                )
            else:
                file_path = "./data/exports/tournaments_report.xlsx"
            remove_file(file_path)
            data_to_export = pd.DataFrame.from_records(data)
            data_to_export.to_excel(file_path)

            return self._data(tournament_name)

    def rounds_report(self) -> list:
        """ "Export the tournament's rounds data as a report (.xlsx) and return a list of it."""

        rounds_rapport = []
        i = 1
        for round_name in self.rounds_list:
            round = Rounds.load(round_name)
            for match in round.match_list:
                rounds_rapport.append(
                    [
                        "match_" + str(i),
                        "white",
                        "⚪ " + Players.find(match[0][0])[0]["last_name"],
                        match[0][1],
                        match[1][1],
                        "⚫ " + Players.find(match[1][0])[0]["last_name"],
                        "black",
                        "round_" + str(round.number),
                        round.status,
                        match[0][0],
                        match[1][0],
                        self.name,
                        self.status,
                    ]
                )
                i += 1

        data = [
            {
                "match": p[0],
                "player1_color": p[1],
                "player1_name": p[2],
                "player1_score": p[3],
                "player2_score": p[4],
                "player2_name": p[5],
                "player2_color": p[6],
                "round_number": p[7],
                "round_status": p[8],
                "player1_ine": p[9],
                "player2_ine": p[10],
                "tournament_name": p[11],
                "tournament_status": p[12],
            }
            for p in rounds_rapport
        ]

        data_to_export = pd.DataFrame.from_records(data)
        file_path = (
            "./data/exports/rounds_report_of_tournament_(" + self.name + ").xlsx"
        )
        remove_file(file_path)
        data_to_export.to_excel(file_path)

        return rounds_rapport

    """ class methode for demo """

    @classmethod
    def reboot(self):
        """create a 2 fakes tournaments"""

        Rounds.table().truncate()
        self.table().truncate()

        tournament1 = Tournaments("TOURNOI_1", "LONDON")
        ine_liste = ["AB12345", "AB12346", "AB12347", "AB12348"]
        self.add_players_list(tournament1, ine_liste)
        self.create(tournament1)

        tournament2 = Tournaments("TOURNOI_2", "ROMA")
        ine_liste2 = ["AB12347", "AB12348", "AB12349", "AB12350"]
        self.add_players_list(tournament2, ine_liste2)
        self.create(tournament2)

    """ intern class methode """

    @classmethod
    def _data(self, tournament_name="") -> list:
        """the tournament's data exported in the report"""

        data = []
        if len(tournament_name) == 0:
            tournament_list = self.read()
        if len(tournament_name) > 0 and tournament_name in self.read_names():
            tournament_list = self.find(tournament_name)

        for t in tournament_list:
            data.append(
                {
                    "name": t["name"],
                    "place": t["place"],
                    "description": t["description"],
                    "status": t["status"],
                    "start_date": t["start_date"],
                    "end_date": t["end_date"],
                    "number_of_players": len(list(t["players_score"].keys())),
                    "number_of_rounds": t["number_of_rounds"],
                    "current_round": t["current_round"],
                }
            )

        return data

    def _round_instance(self):
        """instantiate and return the next round"""

        return Rounds(
            self.name,
            self.name + "_round_" + str(self.current_round + 1),
            self.current_round + 1,
        )

    def _update(self, round):
        """update the tournament's data and create the next round"""

        self.current_round += 1
        rounds_list = self.rounds_list
        rounds_list.append(round.name)
        self.rounds_list = rounds_list

        round.create()
        self.update()

    def _test_status(self):
        """test the rounds status and the tournament status
        and register an error message"""

        if not self.rounds_status():
            logging.info("The previous round isn't finished !")

        if self.status == "finished":
            logging.error("The tournament is finished !")

    def _first_round_conditions(self) -> bool:
        """test if the first round can be created"""

        reponse = False
        if self.status == "created" and len(self.players_score) >= 4:
            reponse = True
            return reponse

        if (self.current_round >= len(self.players_score) - 1) and (
            (self.rounds_status()) and (self.status == "running")
        ):
            reponse = True
            return reponse

        if not reponse and (self.current_round < len(self.players_score) - 1):
            logging.info("Please use the 'next_round' class method !")

        if not reponse and len(self.players_score) < 4:
            logging.error(
                "A minimum of 4 players is required to start the tournament !"
            )
        self._test_status()

        return reponse

    def _next_round_conditions(self) -> bool:
        """test if the next round can be created"""

        reponse = False
        if (
            (self.current_round < len(self.players_score) - 1)
            and (self.rounds_status())
            and (self.status == "running")
        ):
            reponse = True
            return reponse

        if ((not reponse) and (self.status == "created")) or (
            (not reponse) and (self.current_round >= len(self.players_score) - 1)
        ):
            logging.error("Please use the 'first_round' class method !")

        self._test_status()

        return reponse

    def _first_round(self):
        """generate a random round from shuffled players list

        used for the first round or if current_round >= number of players -1
        """

        round = self._round_instance()
        round.first_round(self.players_rank())

        self.status = "running"
        self._update(round)

    def _next_round(self):
        """generate a next round from players list sorted by rank
        only if tournament status is 'running' and current_round < number of players -1
        """

        round = self._round_instance()
        played_matchs = Rounds.played_matchs(self.rounds_list)

        if len(self.players_rank()) % 2 != 0:
            unchoised_player = Rounds.unchoised_player(
                self.rounds_list[-1], self.players_rank()
            )
            round.next_round(self.players_rank(), played_matchs, unchoised_player)
        else:
            round.next_round(self.players_rank(), played_matchs)

        self._update(round)
