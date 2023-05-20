from tabulate import tabulate
from colorama import Fore, Style


def display_tournament(tournament):
    tournament_info = [
        ["Name", tournament.name],
        ["Location", tournament.location],
        ["Start Date", tournament.start_date],
        ["End Date", tournament.end_date],
        ["Time Control", tournament.time_control],
        ["Number of Rounds", str(tournament.number_of_rounds)],
        ["Current Round Number", str(tournament.current_round_number)],
        ["Number of Players", len(tournament.players)],
        ["Description", tournament.description[:200]]
    ]

    print(f"{Fore.GREEN}***************************")
    print("       TOURNAMENT CREATED        ")
    print("***************************")
    print(tabulate(tournament_info, tablefmt="fancy_grid", numalign="left"))
    print("***************************")
    print(f"{Style.RESET_ALL}")


def display_tournaments(tournaments):
    for tournament in tournaments:
        tournament_data = [
            ["Name", tournament.name],
            ["Location", tournament.location],
            ["Start Date", tournament.start_date],
            ["End Date", tournament.end_date],
            ["Time Control", tournament.time_control],
            ["Number of Rounds", str(tournament.number_of_rounds)],
            ["Current Round Number", str(tournament.current_round_number)],
            ["Number of Players", len(tournament.players)],
            ["Description", tournament.description[:200]]
        ]

    headers = [
        "Name", 
        "Location", 
        "Start Date", 
        "End Date", 
        "Time Control", 
        "Number of Rounds", 
        "Current Round Number", 
        "Number of Players", 
        "Description"
    ]

    print(
            f"{Fore.GREEN}{tabulate(tournament_data, tablefmt='fancy_grid', numalign='left')}"
        )
    print(f"{Style.RESET_ALL}")
