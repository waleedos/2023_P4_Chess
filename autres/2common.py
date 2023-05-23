# Fichier /views/common.py
def top_bottom(function):
    """design pattern decorator :
    add the top and the bottom to a menu"""

    def wrapper(*args, **kwargs):
        print()
        print("-" * 80)
        print("\n                          ♟️   Chess Tournament Manager  ♟️\n")

        result = function(*args, **kwargs)

        print("-" * 80)
        print()

        return result

    return wrapper


def get_choice() -> str:
    """get user choice on a menu"""

    return input("Your choice > ")


def menu(preview: str):
    """display the menu"""

    print(f" {preview}\n")
    print("                              1 -- List")
    print("                              2 -- Select")
    print("                              3 -- Create")
    print("                              4 -- Edit")
    print("                              5 -- Delete")
    print("                              6 -- Back to Home Menu\n")
