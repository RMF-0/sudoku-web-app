
from pysat.solvers import Solver  # PySAT pour résoudre les problèmes SAT


def indice(i, j, k):
    """Retourne l'index DIMACS pour la variable X(i,j,k)."""
    return 81 * (i - 1) + 9 * (j - 1) + k


def generer_contraintes():
    """Génère toutes les contraintes en FNC pour le Sudoku."""
    clauses = []

    # Contrainte d'existence: chaque case contient au moins un chiffre
    for i in range(1, 10):
        for j in range(1, 10):
            clauses.append([indice(i, j, k) for k in range(1, 10)])

    # Contrainte d'unicité: une case ne contient pas deux chiffres
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for k2 in range(k + 1, 10):
                    clauses.append([-indice(i, j, k), -indice(i, j, k2)])

    # Contrainte de ligne: un chiffre apparaît une seule fois par ligne
    for j in range(1, 10):
        for k in range(1, 10):
            for i1 in range(1, 10):
                for i2 in range(i1 + 1, 10):
                    clauses.append([-indice(i1, j, k), -indice(i2, j, k)])

    # Contrainte de colonne: un chiffre apparaît une seule fois par colonne
    for i in range(1, 10):
        for k in range(1, 10):
            for j1 in range(1, 10):
                for j2 in range(j1 + 1, 10):
                    clauses.append([-indice(i, j1, k), -indice(i, j2, k)])

    # Contrainte de région 3x3
    for k in range(1, 10):
        for a in [1, 4, 7]:
            for b in [1, 4, 7]:
                cellules = [(i, j) for i in range(a, a + 3) for j in range(b, b + 3)]
                for (i1, j1) in cellules:
                    for (i2, j2) in cellules:
                        if (i1, j1) < (i2, j2):
                            clauses.append([-indice(i1, j1, k), -indice(i2, j2, k)])
    
    return clauses

def generer_dimacs(grille_entree, nom_fichier_dimacs="sudoku.cnf"):
    """Lit les valeurs initiales depuis un fichier texte et génère le fichier DIMACS."""
    clauses = generer_contraintes()
    nb_vars = 9 * 9 * 9  # 729 variables



    # Ajouter les clauses pour les valeurs initiales
    for (i, j, k) in grille_entree:
        clauses.append([indice(i, j, k)])

    nb_clauses_total = len(clauses)

    # Écrire le fichier DIMACS
    with open(nom_fichier_dimacs, "w") as f:
        f.write(f"p cnf {nb_vars} {nb_clauses_total}\n")
        for clause in clauses:
            f.write(" ".join(map(str, clause)) + " 0\n")
    print(f"Fichier DIMACS '{nom_fichier_dimacs}' généré")


def resoudre_sudoku(fichier_dimacs = "sudoku.cnf", fichier_sortie="sudoku.out"):
    """Utilise PySAT pour résoudre le Sudoku à partir d'un fichier DIMACS et génère un fichier .out."""
    solver = Solver(name='minisat22')  # Utilise le solveur MiniSat intégré à PySAT

    # Charger les clauses depuis le fichier DIMACS
    with open(fichier_dimacs, "r") as f:
        for line in f:
            if line.startswith("p") or line.startswith("c"):
                continue  # Ignorer les lignes de commentaire et l'en-tête
            clause = list(map(int, line.strip().split()))[:-1]  # Supprimer le 0 final
            solver.add_clause(clause)

    # Résoudre le problème SAT
    sat = solver.solve()
    with open(fichier_sortie, "w") as f_out:
        if not sat:
            f_out.write("UNSAT\n")
            return None  # Retourne None si le problème est insatisfaisable

        # Écrire la solution SAT dans le fichier .out
        f_out.write("SAT\n")
        solution = solver.get_model()
        f_out.write(" ".join(map(str, solution)) + " 0\n")

    return solution  # Retourne le modèle satisfaisant


def analyser_solution(solution):
    """Analyse la solution PySAT et reconstruit la grille Sudoku."""
    grille = [[0] * 9 for _ in range(9)]
    
    for val in solution:
        if val > 0:  # Seules les variables positives sont vraies
            k = (val - 1) % 9 + 1
            j = ((val - 1) // 9) % 9 + 1
            i = (val - 1) // 81 + 1
            grille[i - 1][j - 1] = k
    
    return grille

