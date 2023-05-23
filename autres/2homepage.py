# Fichier /views/homepage.py
from .common import top_bottom, get_choice


class HomepageView:
    @top_bottom
    def menu(self) -> str:
        """display the homepage and get the choice"""

        print("\n                              Home Menu\n")
        print("                              1 -- Player")
        print("                              2 -- Tournament")
        print("                              3 -- Report")
        print("                              4 -- Exit\n")

        return get_choice()
