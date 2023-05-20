from controllers import player_controller
from views import player_view

def main():
    while True:
        # demandez à l'utilisateur ce qu'il veut faire
        action = input("Que voulez-vous faire ? (1 - Ajouter un joueur, 2 - Afficher les joueurs, Q - Quitter) ")

        # exécutez l'action appropriée
        if action == "1":
            # demandez les informations du joueur à l'utilisateur
            last_name = input("Nom de famille : ")
            first_name = input("Prénom : ")
            date_of_birth = input("Date de naissance (jj/mm/aaaa) : ")
            score = int(input("Score : "))

            # créez le joueur
            player = player_controller.create_player(last_name, first_name, date_of_birth, score)

            # ajoutez le joueur à la liste des joueurs et sauvegardez dans le fichier JSON
            player_controller.add_player(player, 'data/players/players.json')

            # affichez le joueur
            player_view.display_player(player)

        elif action == "2":
            # chargement des joueurs à partir du fichier JSON et affichage
            loaded_players = player_controller.load_players('data/players/players.json')
            player_view.display_players(loaded_players)

        elif action.lower() == "q":
            # quittez le programme
            break

        else:
            print("Action non reconnue. Veuillez réessayer.")

if __name__ == "__main__":
    main()
