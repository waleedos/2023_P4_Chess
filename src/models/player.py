""" class Players """

from tinydb import TinyDB, where
import pandas as pd

from .common import remove_file


class Players:
    def __init__(self, last_name: str, first_name: str, birthdate: str, ine: str):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.ine = ine

    def __str__(self):
        """used in print"""

        return f"{self.__dict__}"

    def __repr__(self):
        """used in print"""

        return str(self)

    @classmethod
    def db(self):
        """Create a JSON file as database"""

        return TinyDB("./data/players/players.json")

    @classmethod
    def table(self):
        """Create 'Players' table in database"""

        return self.db().table("Players")

    def create(self):
        """Create player in database"""

        self.table().insert(self.__dict__)

    @classmethod
    def load(self, ine: str):
        """load instance from json"""

        if len(self.find(ine)) > 0:
            player = self.find(ine)[0]

            return Players(**player)
        else:
            return []

    def update(self):
        """update players data in json"""

        self.table().update(
            self.__dict__,
            where("ine") == self.ine,
        )

    def delete(self):
        """delete a player from Players table(json)"""

        self.table().remove(where("ine") == self.ine)

    @classmethod
    def read(self) -> list:
        """Display players table sorted by last_name"""

        def cle(players):
            return players["last_name"]

        return sorted(self.table().all(), key=cle)

    @classmethod
    def ine_list(self) -> list:
        """get players ine list"""

        return [p["ine"] for p in self.read()]

    @classmethod
    def find(self, ine: str) -> list:
        """Look for a player in players table by ine"""

        return self.table().search(where("ine") == ine)

    @classmethod
    def reboot(self):
        """create 6 fake players in database for demo"""

        self.table().truncate()

        player1 = Players(
            last_name="ZIDANE",
            first_name="Zinedine",
            birthdate="23/06/1972",
            ine="AB12345",
        )
        self.create(player1)

        player2 = Players(
            last_name="MARADONA",
            first_name="Diego",
            birthdate="30/10/1960",
            ine="AB12346",
        )
        self.create(player2)

        player3 = Players(
            last_name="RONALDO",
            first_name="Christiano",
            birthdate="05/02/1985",
            ine="AB12347",
        )
        self.create(player3)

        player4 = Players(
            last_name="MESSI",
            first_name="Lionel",
            birthdate="24/06/1987",
            ine="AB12348",
        )
        self.create(player4)

        player5 = Players(
            last_name="INIESTA",
            first_name="Andres",
            birthdate="24/06/1987",
            ine="AB12349",
        )
        self.create(player5)

        player6 = Players(
            last_name="VAN-BASTEN",
            first_name="Marco",
            birthdate="24/06/1987",
            ine="AB12350",
        )
        self.create(player6)

    @classmethod
    def report(self):
        """export system's players to an excel report and read it"""

        data = [player for player in self.read()]

        data_to_export = pd.DataFrame.from_records(data)
        file_path = "./data/exports/system_players_report.xlsx"
        remove_file(file_path)
        data_to_export.to_excel(file_path)
