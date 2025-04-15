# Application Web de Résolution de Sudoku

Ce projet est une application web permettant de résoudre des grilles de Sudoku. Elle est construite avec Flask et offre une interface interactive pour saisir une grille de Sudoku et obtenir une solution.

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

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <url-du-depot>
   cd sudoku-web-app
   ```

2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

   Les dépendances incluent :
   - Flask
   - Werkzeug
   - numpy
   - pandas
   - python-sat

## Lancer l'Application

Pour lancer l'application, exécutez la commande suivante :
```bash
python src/app.py
```

L'application démarrera un serveur web local. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000` pour utiliser l'interface de résolution de Sudoku.

## Utilisation

1. Saisissez une grille de Sudoku dans la grille fournie. Utilisez `0` pour les cases vides.
2. Cliquez sur le bouton "Solve" pour trouver la solution.
3. La solution sera affichée directement dans la grille.

## Contribuer

Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request pour toute amélioration ou correction de bug.

## Licence

Ce projet est sous licence MIT.