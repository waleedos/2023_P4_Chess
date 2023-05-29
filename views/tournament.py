# Importation de la classe View du module view depuis le dossier views, pour qu'elle soit utilisée comme classe de base
# pour d'autres classes dans ce module.
from views.view import View

# Importation de la fonction get_timestamp du module timestamp qui se trouve dans le paquet utils, Cette fonction sera
# utilisée pour obtenir le timestamp actuel.
from utils.timestamp import get_timestamp

# Importation de la fonction load_db du module database depuis le dossier controller et qui servira pour charger les
# données depuis la base de données.
from controller.database import load_db


class CreateTournament(View):
    # Déclaration d'une nouvelle classe CreateTournament qui hérite de la classe View.

    def display_menu(self):
        # Déclaration d'une méthode display_menu à l'intérieur de la classe CreateTournament pour l'affichage d'un menu
        # à l'utilisateur.

        date = get_timestamp()
        print(date + " : Nouveau tournoi")
        # Apres l'appel de la fonction get_timestamp, impression de la date et l'heure actuelles, suivies de la chaîne
        # de caractères " : Nouveau tournoi".

        name = input("Nom du tournoi :\n"
                     ">>> ")

        location = self.get_user_entry(
            msg_display="Lieu :\n"
                        ">>> ",
            msg_error="Veuillez entrer un lieu valide",
            value_type="string"
        )
        # Demande à l'utilisateur de saisir le nom et le lieu du tournoi qui seront ensuite stockés respectivement dans
        # les deux variables nom et location

        user_selection_time_control = self.get_user_entry(
            # Appel de la méthode get_user_entry avec les paramètres spécifiés. La valeur renvoyée est stockée dans la
            # variable user_selection_time_control
            msg_display="Contrôle de temps :\n"
                        "0 - Bullet\n"
                        "1 - Blitz\n"
                        "2 - Coup Rapide\n"
                        ">>> ",
            msg_error="Veuillez entrer 0, 1 ou 2",
            value_type="selection",
            assertions=["0", "1", "2"]
        )
        if user_selection_time_control == "0":
            # vérifie si la valeur de user_selection_time_control est égale à "0". Si c'est le cas, la ligne suivante
            # sera exécutée.
            time_control = "Bullet"
            # affectation de la chaîne de caractères "Bullet" à la variable time_control.
        elif user_selection_time_control == "1":
            time_control = "Blitz"
            # affectation de la chaîne de caractères "Blitz" à la variable time_control.
        else:
            time_control = "Coup Rapide"
            # affectation de la chaîne de caractères "Coup Rapide" à la variable time_control.

        nb_players = self.get_user_entry(
            msg_display="Nombre de joueurs :\n"
                        ">>> ",
            msg_error="Veuillez entrer un nombre entier supérieur ou égal à 2",
            value_type="num_superior",
            default_value=2
        )
        # Appel de la méthode get_user_entry avec les paramètres spécifiés. La valeur renvoyée est stockée dans la
        # variable nb_players.

        nb_rounds = self.get_user_entry(
            msg_display="Nombre de tours (4 par défaut) :\n"
                        ">>> ",
            msg_error="Veuillez entrer 4 ou plus",
            value_type="num_superior",
            default_value=4
        )
        # Appel de la méthode get_user_entry avec les paramètres spécifiés. La valeur renvoyée est stockée dans la
        # variable nb_rounds.

        desc = input("Description du tournoi :\n>>> ")
        #  demande à l'utilisateur de saisir une description pour le tournoi. La description est ensuite stockée dans
        #  la variable desc.

        return {
            "name": name,
            "location": location,
            "date": date,
            "time_control": time_control,
            "nb_players": nb_players,
            "nb_rounds": nb_rounds,
            "desc": desc
        }
        # Fin du retour du dictionnaire qui sera renvoyé par la méthode display_menu.


class LoadTournament(View):
    # Déclaration d'une nouvelle classe LoadTournament qui hérite de la classe View.

    def display_menu(self):
        # Déclaration d'une méthode display_menu à l'intérieur de la classe LoadTournament. Cette méthode sera
        # probablement utilisée pour afficher un menu à l'utilisateur.

        tournaments = load_db("tournaments")
        # Appel de la fonction load_db avec le paramètre "tournaments". La valeur renvoyée est stockée dans la variable
        # tournaments.

        if tournaments:
            # vérifie si la valeur de tournaments est vraie. Si c'est le cas, le bloc de code suivant sera exécuté.

            build_selection = self.build_selection(iterable=tournaments, display_msg="Choisir un tournoi :\n",
                                                   assertions=[])
            # Appell de la méthode build_selection avec les paramètres spécifiés. La valeur renvoyée est stockée dans la
            # variable build_selection.

            user_input = int(self.get_user_entry(
                # Appel de la méthode get_user_entry avec les paramètres spécifiés. La valeur renvoyée est convertie en
                # un entier et stockée dans la variable user_input.

                msg_display=build_selection['msg'] + ">>> ",
                msg_error="Veuillez entrer un nombre entier",
                value_type="selection",
                assertions=build_selection['assertions']
            ))

            serialized_loaded_tournament = tournaments[user_input-1]
            # Accède à l'élément dans tournaments à l'index user_input - 1 et stocke la valeur dans la variable
            # serialized_loaded_tournament.

            return serialized_loaded_tournament
            # renvoie la valeur de serialized_loaded_tournament.

        else:
            return False
