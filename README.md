# Application Web de Résolution de Sudoku

Ce projet est une application web open source permettant de résoudre des grilles de Sudoku. Elle est construite avec Flask et offre une interface interactive pour saisir une grille de Sudoku et obtenir une solution. Les contraintes du Sudoku sont traduites en logique propositionnelle au format DIMACS, puis résolues à l'aide de **PySAT**, un SAT Solver.

## Structure du Projet

```
sudoku-web-app
├── src
│   ├── app.py                  # Point d'entrée de l'application
│   ├── templates
│   │   └── index.html          # Structure HTML de l'interface utilisateur
│   ├── static
│   │   ├── css
│   │   │   └── styles.css       # Styles CSS pour l'interface HTML
│   │   └── js
│   │       └── scripts.js       # JavaScript pour gérer les interactions utilisateur
│   ├── sudoku_solver
│   │   ├── __init__.py         # Marque le répertoire comme un package Python
│   │   ├── solver.py           # Logique pour résoudre les grilles de Sudoku
│   │   └── utils.py            # Fonctions utilitaires pour la résolution de Sudoku
├── requirements.txt             # Liste des dépendances nécessaires pour le projet
└── README.md                    # Documentation du projet
```

## Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés sur votre système :

1. **Python 3** : Version 3.7 ou supérieure.
2. **pip** : Le gestionnaire de paquets Python.
3. **venv** : Pour créer un environnement virtuel isolé.

Sur une distribution Linux (comme Debian), vous pouvez les installer avec les commandes suivantes :

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

Sur Windows, téléchargez et installez Python depuis [python.org](https://www.python.org/).

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/RMF-0/sudoku-web-app.git
   cd sudoku-web-app
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Linux/Mac
   venv\Scripts\activate     # Sur Windows
   ```

3. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

   Les dépendances incluent :
   - Flask
   - Werkzeug
   - numpy
   - pandas
   - python-sat (PySAT)

## Lancer l'Application

Pour lancer l'application, exécutez la commande suivante :
```bash
python src/app.py
```

L'application démarrera un serveur web local. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000` pour utiliser l'interface de résolution de Sudoku.

## Utilisation

1. Saisissez une grille de Sudoku dans la grille fournie. Utilisez `0` pour les cases vides.
2. Cliquez sur le bouton "Solve" pour traduire la grille en clauses logiques au format DIMACS et résoudre le problème avec le SAT Solver.
3. La solution sera affichée directement dans la grille. Les valeurs générées par le solveur seront affichées en bleu.

## Fonctionnalités

- Traduction des contraintes du Sudoku en logique propositionnelle.
- Génération d'un fichier DIMACS (`sudoku.cnf`) contenant les clauses logiques.
- Résolution des contraintes avec **PySAT**.
- Téléchargement des fichiers DIMACS (`sudoku.cnf`) et solution (`sudoku.out`) dans un fichier ZIP.

## Open Source

Ce projet est open source. Vous pouvez consulter, modifier et redistribuer le code selon les termes de la licence.

## Contribuer

Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request pour toute amélioration ou correction de bug.

## Licence

Ce projet est sous licence MIT.