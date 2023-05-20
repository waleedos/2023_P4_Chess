from tabulate import tabulate
from colorama import Fore, Style


def display_tournament(tournament):
    tournament_info = [
        ["Name", tournament.name],
        ["Location", tournament.location],
        ["Start Date", tournament.start_date],
        ["End Date", tournament.end_date],
        ["Time Control", get_time_control_label(int(tournament.time_control))],
        ["Number of Rounds", str(tournament.number_of_rounds)],
        ["Current Round Number", str(tournament.current_round_number)],
        ["Number of Players", str(len(tournament.players))],
        ["Description", tournament.description[:200]]
    ]

    print(f"{Fore.GREEN}***************************")
    print("       TOURNAMENT CREATED        ")
    print("***************************")
    print(tabulate(tournament_info, tablefmt="fancy_grid", numalign="left"))
    print("***************************")
    print(f"{Style.RESET_ALL}")


def display_tournaments(tournaments):
    tournament_data = []
    for i, tournament in enumerate(tournaments, start=1):
        time_control = get_time_control_label(int(tournament.time_control))
        tournament_info = [
            [f"{Fore.RED if i == 1 or i == 2 else ''}Tournament {i}{Style.RESET_ALL}"],
            ["Name", tournament.name],
            ["Location", tournament.location],
            ["Start Date", tournament.start_date],
            ["End Date", tournament.end_date],
            ["Time Control", time_control],
            ["Number of Rounds", str(tournament.number_of_rounds)],
            ["Current Round Number", str(tournament.current_round_number)],
            ["Number of Players", str(len(tournament.players))],
            ["Description", tournament.description[:200]]
        ]
        tournament_data.append(tournament_info)

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

    print(f"{Fore.GREEN}**********************************")
    print("          TOURNAMENTS LIST          ")
    print("**********************************")
    for data in tournament_data:
        print(tabulate(data, headers=headers, tablefmt="fancy_grid", numalign="left"))
        print()
    print(f"{Style.RESET_ALL}")


def get_time_control_label(time_control):
    time_controls = {
        0: "Bullet",
        1: "Blitz",
        2: "Coup rapide"
    }
    return time_controls.get(time_control, "Unknown")
