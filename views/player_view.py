from colorama import Fore, Back, Style

def display_player(player):
    print(Fore.YELLOW)
    print("****************************")
    print("     CE JOUEUR EST CRÉÉ     ")
    print("****************************")
    print("  Nom       : {: <18}  ".format(player.last_name))
    print("  Prénom    : {: <18}  ".format(player.first_name))
    print("  Né(e) le  : {: <18}  ".format(player.date_of_birth))
    print("  Score     : {: <18}  ".format(str(player.score)))
    print("****************************")
    print(Style.RESET_ALL)