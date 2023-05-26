from colorama import Fore, Style
from tabulate import tabulate


def get_new_tournament_info():
    name = input("Nom du tournoi : ")
    location = input("Lieu du tournoi : ")
    description = input("Description du tournoi : ")
    start_date = input("Début du tournoi (jj/mm/aaaa) : ")
    end_date = input("Fin du tournoi (jj/mm/aaaa) : ")
    time_control = int(input("Contrôle du temps (1=bullet, 2=blitz, 3=coup rapide) : "))
    change_rounds = input("Voulez-vous changer le nombre de tours (4 par défaut) ? (O/N) : ")

    if change_rounds.lower() == "o":
        rounds = int(input("Entrez le nombre de tours : "))
    else:
        rounds = 4

    tournament_data = {
        "name": name,
        "location": location,
        "description": description,
        "start_date": start_date,
        "end_date": end_date,
        "time_control": time_control,
        "rounds": rounds,
        "players": [],  # Initialiser la liste des joueurs à vide
    }

    return tournament_data


def display_all_tournaments(tournaments):
    if len(tournaments) > 0:
        tournament_data = [
            {
                "Nom": tournament.name,
                "Lieu": tournament.location,
                "Début du tournoi": tournament.start_date,
                "Fin du tournoi": tournament.end_date,
                "Description": tournament.description,
                "Contrôle du temps": tournament.time_control,
                "Nombre de tours": tournament.rounds,
                "Joueurs participants": ", ".join(tournament.players)
            } for tournament in tournaments
        ]
        headers = {
            "Nom": "Nom",
            "Lieu": "Lieu",
            "Début du tournoi": "Début du tournoi",
            "Fin du tournoi": "Fin du tournoi",
            "Description": "Description",
            "Contrôle du temps": "Contrôle du temps",
            "Nombre de tours": "Nombre de tours",
            "Joueurs participants": "Joueurs participants"
        }
        print(Fore.GREEN + tabulate(tournament_data, headers=headers, tablefmt="fancy_grid"))
        print(Fore.RED + "Liste des tournois existants" + "\n\n" + Style.RESET_ALL)
    else:
        print("Aucun tournoi enregistré.")


def display_tournament_creation_success(tournament):
    tournament_data = [
        {
            "Nom": tournament.name,
            "Lieu": tournament.location,
            "Début du tournoi": tournament.start_date,
            "Fin du tournoi": tournament.end_date,
            "Description": tournament.description,
            "Contrôle du temps": tournament.time_control,
            "Nombre de tours": tournament.rounds,
            "Joueurs participants": ", ".join(tournament.players)
        }
    ]
    headers = {
        "Nom": "Nom",
        "Lieu": "Lieu",
        "Début du tournoi": "Début du tournoi",
        "Fin du tournoi": "Fin du tournoi",
        "Description": "Description",
        "Contrôle du temps": "Contrôle du temps",
        "Nombre de tours": "Nombre de tours",
        "Joueurs participants": "Joueurs participants"
    }
    print(Fore.GREEN + tabulate(tournament_data, headers=headers, tablefmt="fancy_grid"))
    print(Fore.RED + "Ce tournoi a été créé avec succès !" + "\n\n" + Style.RESET_ALL)
