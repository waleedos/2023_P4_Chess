# importation de la classe View depuis le module views.view et la fonction load_db depuis le module
# controller.database.
from views.view import View
from controller.database import load_db


class CreatePlayer(View):
    # Creation d'une nouvelle classe CreatePlayer est définie, qui hérite de la classe View.

    def display_menu(self):
        # Définition de la methode display_menu dans la classe CreatePlayer.
        name = input("Nom du joueur :\n"
                     ">>> ")

        firstname = input("Prénom du joueur :\n"
                          ">>> ")

        birthday = self.get_user_entry(
            msg_display="Date de naissance (format DD/MM/YYYY) :\n"
                        ">>> ",
            msg_error="Veuillez entrer une date au format valide: DD/MM/YYYY",
            value_type="date"
        )

        gender = self.get_user_entry(
            msg_display="Sexe (H ou F) :\n"
                        ">>> ",
            msg_error="Veuillez entrer H ou F",
            value_type="selection",
            assertions=["H", "h", "F", "f"]
        ).upper()

        rating = self.get_user_entry(
            msg_display="Classement :\n"
                        ">>> ",
            msg_error="Veuillez entrer une valeur numérique valide",
            value_type="numeric"
        )
        # Plusieures entrées sont demandées à l'utilisateur pour la création d'un nouveau joueur.

        print(f"{firstname} {name} a été créé")
        # Un message indiquant que le joueur a été créé est affiché.

        return {
            "name": name,
            "firstname": firstname,
            "birthday": birthday,
            "gender": gender,
            "total_score": 0,
            "rating": rating,
        }
        # Un dictionnaire avec les informations du joueur est retourné.


class LoadPlayer(View):
    # Création d'une nouvelle classe LoadPlayer est définie, qui hérite de la classe View.

    def display_menu(self, nb_players_to_load):

        all_players = load_db("players")
        # Chargement de La base de données des joueurs.
        serialized_loaded_players = []
        # Une liste vide pour stocker les joueurs chargés est initialisée.
        for i in range(nb_players_to_load):
            # Une boucle est initiée pour le nombre de joueurs à charger.

            if not all_players:
                print("Oups... Aucun joueur n'est enregistré dans la base")
                break
            # Si la liste de tous les joueurs est vide, un message est affiché et la boucle est interrompue.

            print(f"Plus que {str(nb_players_to_load - i)} joueur(s) à charger")
            display_msg = "Choisir un joueur :\n"
            # Un message indiquant combien de joueurs restent à charger est affiché en invitant l'utilisateur à choisir
            # un joueur à initié.

            assertions = []
            for j, player in enumerate(all_players):
                display_msg = display_msg + f"{str(j + 1)} - {player['firstname']} {player['name']}\n"
                assertions.append(str(j + 1))
                # Un menu de sélection des joueurs est créé.

            user_input = int(self.get_user_entry(
                msg_display=f"{display_msg}\n"
                            ">>> ",
                msg_error="Veuillez entrer un nombre entier.",
                value_type="selection",
                assertions=assertions
            ))
            # L'entrée de l'utilisateur est reçue.

            if all_players[user_input - 1] not in serialized_loaded_players:
                serialized_loaded_players.append(all_players[user_input - 1])
            else:
                print("Joueur déjà chargé. Merci de choisir un autre joueur.")
                nb_players_to_load += 1
                # Si le joueur sélectionné n'a pas encore été chargé, il est ajouté à la liste des joueurs chargés. Si
                # le joueur a déjà été chargé, un message est affiché et le nombre de joueurs à charger est augmenté.

        return serialized_loaded_players
        # La liste des joueurs chargés est retournée.
