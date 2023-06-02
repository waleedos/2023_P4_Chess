![Chess Master](https://raw.githubusercontent.com/waleedos/2023_P4_Chess/main/Documents/chess.png)

# Développez un programme logiciel en Python : Chess Tournament

## Préambule
Étant un développeur junior depuis deux mois et travaillant en freelance pour écrire des scripts simples afin d’aider les petites entreprises locales à gérer leur inventaire, une amie me suggère d’écrire un outil qui permette de gérer les tournois pour aider un club d’Échecs Local, mais qui fonctionne hors ligne

## Scénario
Il faut utiliser la programmation orientée objet pour créer et améliorer les classes qui représentent les entités dans le programme : joueurs, tournois et tours.

Il faut suivre la conception Modèle-Vue-Contrôleur (MVC), Créer des classes qui serviront de modèles pour le tournoi, les joueurs, les matchs et les rondes.

Utiliser des vues pour afficher les classements, les appariements et d'autres statistiques.

Écrire des contrôleurs pour accepter les données de l'utilisateur, produire les résultats des matchs, lancer de nouveaux tournois, etc.

Le code doit être propre et maintenable, assuré  donc qu’il suit les directives de style de code – la PEP 8 en particulier.

Utilisation du format JSON pour les fichiers de données.

Voici les spécifications Techniques de ce projet :  [CHESS MASTER](https://github.com/waleedos/2023_P4_Chess/blob/main/Documents/3-Specifications_techniques.pdf).


## Les Compétences visées et évaluées
* Structurer le code d'un programme Python en utilisant un design pattern
* Écrire un code Python robuste en utilisant la PEP 8
* Utiliser la programmation orientée objet pour développer un programme Python

## Capture d'un exemple des Rapports générés:

![Chess Master](https://raw.githubusercontent.com/waleedos/2023_P4_Chess/main/Documents/Comprehension.png)


## Prerequisites (les versions utilisées sont dans requirements.txt)
* colorama
* flake8
* flake8-html
* Jinja2
* MarkupSafe
* mccabe
* pycodestyle
* pyflakes
* Pygments
* tabulate
* tabulate-expwidth
* tinydb


## Instructions générales

### Clonage ou téléchargement
Clonez cette repositoire    : https://github.com/waleedos/2023_P4_Chess/tree/main
Ou bien 
Télécharger le zip          : https://github.com/waleedos/2023_P4_Chess/archive/refs/heads/main.zip

### Création d'un nouvel environnement virtuel :
Une fois dézippé, et quand vous etes dans votre environnement, mettez vous dans ce dossier sur la racine

Ouvrez un terminal et créez votre environnement virtuel à l'aide de la commande suivante : 
```
python -m venv env
```
### Activation de votre nouvel environnement virtuel :
Activer votre nouvel environnement virtuel à l'aide de la commande suivante :
```
source env/bin/activate
```
### Mise à jour de votre environnement :
Remplire et installer les modules prerequis à partir de du fichier "requirements.txt" par la commande suivante:
```
pip install -r requirements.txt
```
## Fonctionnement :
Mettez vous a la racine du repertoire du projet et Démarrez :
```
cd ..
```

Démarrez le scrypt avec la commande :
```
python main.py
```
Ou bien
```
python3 main.py
```
## Générer le rapport flake8 : 
  ```
  flake8 --format=html --htmldir=flake-report
  ```

### Powered by EL-WALID EL-KHABOU
