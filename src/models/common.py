""" common functions shared between the models and the main """

from os import path, remove, mkdir
from datetime import datetime
import logging


def round_non_existence():
    logging.error("There is no round at this index in the tournament !")


def timestamp():
    """generate timestamp"""

    return str(datetime.now())[0:10]


def remove_file(file_path: str):
    """remove an existant old report"""

    if path.exists(file_path):
        remove(file_path)


def create_folder(folder_path: str):
    """Check if the folders exists; if it does not, create it"""

    if not path.exists(folder_path):
        mkdir(folder_path)


def create_file(file_path: str):
    """Check if the file '.flake8' exists; if it does not, create it"""
    if not path.exists(file_path):
        file = open(file_path, "w")
        file.write(
            """[flake8]
exclude = env, data, .git, .vscode, __pycache__
max-line-length = 119

# Format de sortie en HTML
format = html
htmldir = flake8_report"""
        )
        file.close()


def folders_check():
    """check if the folders/file exists, if it does not, create it"""

    create_folder("./data/")
    create_folder("./data/exports/")
    create_folder("./data/players/")
    create_folder("./data/tournaments/")
    create_folder("./data/rounds/")
    create_folder("./flake8_report")
    create_file("./.flake8")
