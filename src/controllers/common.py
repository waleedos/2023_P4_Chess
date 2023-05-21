""" common functions shared between the controllers """

import re


def clean(text: str) -> str:
    return (
        text.lower()
        .replace("é", "e")
        .replace("è", "e")
        .replace("à", "a")
        .replace("ç", "c")
        .replace("#", "")
        .replace("&", "")
        .replace("~", "")
        .replace("@", "")
        .replace("|", "")
        .replace(" ", "_")
        .strip()
        .upper()
    )


def clean_upper(text: str) -> str:
    """Remove special characters and upper()"""

    return re.sub(r"[^\w\s-]+", "", clean(text))


def clean_lower(text: str) -> str:
    """Remove special characters and upper()"""

    return clean_upper(text).lower()


def clean_capitalize(text: str) -> str:
    """Remove special characters and capitalize()"""

    return clean_upper(text).capitalize()


def clean_tournament(tournament_data: list) -> list:
    """clean tournament name, place and description"""

    return [
        clean_upper(tournament_data[0]),
        clean_upper(tournament_data[1]),
        clean_lower(tournament_data[2]),
    ]


def data(tournament):
    """return the tournament data needed in :
    TournamentView().select_round()
    TournamentView().select_match()
    TournamentView().select_end()
    """

    return [
        tournament.name,
        tournament.status,
        str(tournament.current_round) + "/" + str(tournament.number_of_rounds),
    ]


def int_converter(score: float):
    """convert a score in integer if it is possible"""

    if score == 0.0 or score == 1.0:
        return int(score)
    else:
        return 0.5
