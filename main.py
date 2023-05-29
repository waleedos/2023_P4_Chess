# Voici le point d'entrée principal pour exécuter le programme CHESS TOURNAMENT

from views.main_menu import MainMenu
# Importation de la classe MainMenu depuis le fichier main_menu.py qui se trouve dans le dossier views.


def run():
    MainMenu().display_main_menu()
    # Cela est le corps de la fonction run. Elle crée une nouvelle instance de la classe MainMenu, et ensuite appelle
    # la méthode display_main_menu sur cette instance. On suppose que la méthode display_main_menu est définie dans la
    # classe MainMenu et qu'elle permet de démarrer l'interaction avec l'utilisateur (par exemple en affichant le menu
    # principal de l'application).


if __name__ == "__main__":
    # Le constructeur commune en Python. Lorsqu'un fichier Python est exécuté directement (et non importé comme un
    # module), la variable spéciale __name__ est définie à "__main__". Par conséquent, cette condition vérifie si le
    # script est en cours d'exécution directement.
    run()
    # Appel la fonction run définie précédemment. C'est ce qui déclenche l'exécution de l'application
