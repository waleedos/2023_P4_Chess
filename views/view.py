# importation de la fonction check_date du module check_date depuis le dossier utils. Nous utiliserons Cette fonction*
# pour vérifier si une chaîne de caractères correspond à un format de date valide.
from utils.check_date import check_date


class View:
    # Définition d'une classe nommée View. C'est une classe générale qui peut être utilisée comme base pour
    # d'autres classes.

    @staticmethod
    # un décorateur qui indique que la méthode suivante est une méthode statique: c.a.d qu'elle appartient à une classe
    # plutôt qu'à une instance de la classe. Elle peut être appelée sur la classe elle-même, sans créer une instance de
    # la classe. Les méthodes statiques ne peuvent pas accéder à aucun attribut d'instance ou de classe, sauf si ces
    # attributs sont passés en tant que paramètres.
    def get_user_entry(msg_display, msg_error, value_type, assertions=None, default_value=None):
        # Définition d'une méthode statique nommée get_user_entry. Cette méthode accepte cinq paramètres : msg_display
        # (message à afficher à l'utilisateur lors de la demande d'entrée), msg_error (message à afficher en cas
        # d'erreur), value_type (type de valeur attendu), assertions (une liste de valeurs acceptables), et
        # default_value (valeur par défaut si l'utilisateur ne fournit pas de valeur).

        while True:
            # Démarrage d'une boucle infinie. Cette boucle continuera jusqu'à ce qu'une instruction return ou break
            # soit rencontrée.

            value = input(msg_display)
            # Demande à l'utilisateur d'entrer une valeur. Le message à afficher à l'utilisateur est fourni par le
            # paramètre msg_display.

            if value_type == "numeric":
                # Vérifie si le value_type est "numeric". Si c'est le cas, le bloc de code suivant sera exécuté.

                if value.isnumeric():
                    # Vérifie si la valeur entrée par l'utilisateur est numérique. Si c'est le cas, le bloc de code
                    # suivant sera exécuté.

                    value = int(value)
                    return value
                    # Convertit la valeur en un entier, puis Renvoie la valeur et termine la boucle et la méthode

                else:
                    print(msg_error)
                    # Si la valeur n'est pas numérique, le bloc de code suivant sera exécuté, et Affiche le message
                    # d'erreur fourni par le paramètre msg_error.

                    continue
                    # Continue à la prochaine itération de la boucle.

            if value_type == "num_superior":
                # Vérifie si le value_type est "num_superior". Si c'est le cas, le bloc de code suivant sera exécuté.

                if value.isnumeric():
                    value = int(value)
                    if value >= default_value:
                        return value
                    else:
                        print(msg_error)
                        continue
                else:
                    print(msg_error)
                    continue
            if value_type == "string":
                # Vérifie si le value_type est "string". Si c'est le cas, le bloc de code suivant sera exécuté.

                try:
                    float(value)
                    print(msg_error)
                    continue
                except ValueError:
                    return value

            elif value_type == "date":
                # Vérifie si le value_type est "string". Si c'est le cas, le bloc de code suivant sera exécuté.

                if check_date(value):
                    return value
                else:
                    print(msg_error)
                    continue

            elif value_type == "selection":
                # Vérifie si le value_type est "selection". Si c'est le cas, le bloc de code suivant sera exécuté.

                if value in assertions:
                    return value
                else:
                    print(msg_error)
                    continue

    @staticmethod
    # décorateur qui indique que la méthode suivante est une méthode statique
    def build_selection(iterable, display_msg, assertions):
        # définition d'une méthode statique nommée build_selection qui accepte trois paramètres : iterable (un objet
        # itérable, probablement une liste ou un tuple), display_msg (un message à afficher à l'utilisateur), et
        # assertions (une liste d'affirmations ou de contraintes).

        display_msg = display_msg
        assertions = assertions
        # Ces deux lignes semblent redondantes, car elles assignent les valeurs à elles-même. En général, ces ligne ne
        # sont pas nécessaires.
        for i, data in enumerate(iterable):
            # Commencement d'une boucle for qui itère sur iterable. enumerate(iterable) renvoie un couple d'index et de
            # valeur pour chaque élément dans iterable. i est l'index et data est la valeur.
            display_msg = display_msg + f"{i + 1} - {data['name']}\n"
            # ajout à display_msg une chaîne formatée qui contient l'index (augmenté de 1) et la valeur de name de
            # l'élément courant dans iterable.
            assertions.append(str(i + 1))
            # ajoute la chaîne de l'index (augmenté de 1) à la liste assertions.

        return {
            "msg": display_msg,
            "assertions": assertions
        }
        # terminaison de la méthode et renvoie un dictionnaire contenant display_msg et assertions sous les clés "msg"
        # et "assertions" respectivement.
