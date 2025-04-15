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

---

## Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés sur votre système :

1. **Python 3** : Version 3.7 ou supérieure.
2. **pip** : Le gestionnaire de paquets Python.
3. **venv** : Pour créer un environnement virtuel isolé.
4. **git** : pour clonner l'application dans votre répertoire.

---

## Installation

1. **Installer python3 et ses dépendances**
   Pour linux (comme debian) : 
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv build-essential -y
   ```

   Pour MacOS, utilisez `brew` :
   ```bash
   brew install python3
   ```

   Pour Windows : 
   - Ouvrez PowerShell en mode administrateur et exécutez :
     ```bash
     wsl --install
     ```
   - Redémarrez votre ordinateur si nécessaire.
   - Configurez une distribution Linux (comme Ubuntu).
   - Installer Python et les dépendances système dans WSL** :
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv build-essential -y
   ```
   Toute la suite se passe dans WSL pour Windows.

2. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/RMF-0/sudoku-web-app.git
   cd sudoku-web-app
   ```

3. **Créer un environnement virtuel et activer-le** :
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
5. **Lancer l'application** :
   ```bash
   python src/app.py
   ```
6. **Accéder à l'application** :
   Si votre navigateur ne s'ouvre pas automatiquement, ouvrez-le et accédez à `http://127.0.0.1:8080`.
---

## Utilisation

1. Saisissez une grille de Sudoku dans la grille fournie.
2. Cliquez sur le bouton "Résoudre" pour traduire la grille en clauses logiques au format DIMACS et résoudre le problème avec le SAT Solver.
3. La solution sera affichée directement dans la grille. Les valeurs générées par le solveur seront affichées en bleu.
4. Télécharger le fichier DIMACS si nécessaire.

---

## Fonctionnalités

- Traduction des contraintes du Sudoku en logique propositionnelle.
- Génération d'un fichier DIMACS (`sudoku.cnf`) contenant les clauses logiques.
- Résolution des contraintes avec **PySAT**.
- Téléchargement des fichiers DIMACS (`sudoku.cnf`) et solution (`sudoku.out`) dans un fichier ZIP.

---

## Open Source

Ce projet est open source. Vous pouvez consulter, modifier et redistribuer le code selon les termes de la licence.

---

## Licence

Ce projet est sous licence MIT.