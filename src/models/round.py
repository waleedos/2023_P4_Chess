""" class Rounds """


from random import shuffle
import logging

from tinydb import TinyDB, where

from .common import round_non_existence, timestamp


SCORE = [0.0, 0.5, 1.0]


class Rounds:
    def __init__(
        self,
        tournament_name: str,
        name: str,
        number: int,
        start_date=timestamp(),
        end_date="(not finished)",
        status="running",
        match_list=[],
    ):
        self.tournament_name = tournament_name
        self.name = name
        self.number = number
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.match_list = match_list

    def __str__(self):
        """used in print"""

        return f"{self.__dict__}"

    def __repr__(self):
        """used in print"""

        return str(self)

    @classmethod
    def db(self):
        """Create a JSON file as database"""

        return TinyDB("./data/rounds/rounds.json")

    @classmethod
    def table(self):
        """Create 'Rounds' table in database"""

        return self.db().table("Rounds")

    def create(self):
        """Create a new round in Rounds table"""

        self.table().insert(self.__dict__)

    @classmethod
    def find(self, round_name: str) -> list:
        """Look for a round in table by its name

        return found result"""

        return self.table().search(where("name") == round_name)[0]

    @classmethod
    def load(self, round_name: str):
        """return round instance from json"""

        if len(self.find(round_name)) == 7:
            round = self.find(round_name)

            return Rounds(**round)
        else:
            return []

    def update(self):
        """update the round's data in json by its name"""

        self.table().update(
            self.__dict__,
            where("name") == self.name,
        )

    def delete(self):
        """delete a round from the Rounds table in json"""

        self.table().remove(where("name") == self.name)

    def first_round(self, players_ine_list: list):
        """generate a random round of matchs from a shuffled players list
        and update the round instance"""

        players_ine = players_ine_list
        shuffle(players_ine)
        number_of_match = len(players_ine) // 2
        match_list = []

        for i in range(number_of_match):
            match = ([players_ine[i], ""], [players_ine[i + 1], ""])
            match_list.append(match)

            players_ine.pop(0)

        self.match_list = match_list

    @classmethod
    def played_matchs(self, tournament_rounds_list: list) -> list:
        """generate a list of played matchs in the tournament."""

        played_matchs = []

        for round_id in tournament_rounds_list:
            round = Rounds.load(round_id)
            for match in round.match_list:
                played_matchs.append((match[0][0], match[1][0]))
                played_matchs.append((match[1][0], match[0][0]))

        return played_matchs

    @classmethod
    def unchoised_player(self, last_round_name: str, players_list: list):
        """Return the player who did not play in the previous round.
        (only if the list of players is odd.)"""

        try:
            round = Rounds.load(last_round_name)
            participants = []
            for match in round.match_list:
                participants.extend([match[0][0], match[1][0]])

            return [p for p in players_list if p not in participants][0]

        except IndexError:
            logging.info("the list of players is not odd !")

    def next_round(
        self, players_rank_list: list, played_matchs: list, unchoised_player=""
    ):
        """generate a next round of matchs from players list sorted by rank
        and update the round instance"""

        players = players_rank_list
        if len(players) % 2 != 0:
            if players[-1] != unchoised_player:
                players.pop(-1)
            else:
                players.pop(-2)

        match_list = []
        participants = []

        for p1 in players:
            for p2 in players:
                if (
                    ((p1, p2) not in played_matchs)
                    and (p1 not in participants)
                    and (p2 not in participants)
                    and (p1 != p2)
                ):
                    match_list.append(([p1, ""], [p2, ""]))
                    participants.extend([p1, p2])

        if len(match_list) == len(players_rank_list) // 2:
            self.match_list = match_list

        else:
            self.first_round(players_rank_list)

    def update_match_result(
        self,
        index_of_match: int,
        player1_score: float,
        player2_score: float,
    ):
        """update the match result"""

        try:
            self.match_list[index_of_match][0][1] = player1_score
            self.match_list[index_of_match][1][1] = player2_score

        except UnboundLocalError:
            round_non_existence()

        except IndexError:
            round_non_existence()

    def state(self) -> bool:
        """check the round's status and update it if it's finished

        return a boolean: True for a finished round, False for an ongoing round"""

        finished = True
        for match in self.match_list:
            if (match[0][1] not in SCORE) or (match[1][1] not in SCORE):
                finished = False
        if finished:
            self.end_date = timestamp()
            self.status = "finished"

        return finished

    @classmethod
    def rounds_status(self, rounds_list: list) -> bool:
        """check if all created rounds of the tournament are finished

        return a boolean: True if all round are finished, False for the reverse"""

        finished = True
        for r in rounds_list:
            round = Rounds.load(r)
            if round.status != "finished":
                finished = False

        return finished

    @classmethod
    def update_players_score(self, players_ine_list: list, rounds_list: list) -> dict:
        """generate an updated players_score dict
        (it works only if all created rounds are finished)"""

        players_score = {}
        for ine in players_ine_list:
            players_score[ine] = 0

        for round_id in rounds_list:
            round = Rounds.load(round_id)
            for match in round.match_list:
                for ine in players_ine_list:
                    if match[0][0] == ine:
                        players_score[ine] += match[0][1]
                    if match[1][0] == ine:
                        players_score[ine] += match[1][1]

        return players_score

    def get_matchs_list(self) -> list:
        """get the matchs list with tuple type"""

        matchs_list = []

        for match in self.match_list:
            matchs_list.append(([match[0][0], match[0][1]], [match[1][0], match[1][1]]))

        return matchs_list
