import os
import zipfile
from flask import Flask, render_template, request, jsonify, send_file
from sudoku_solver.solver import generer_dimacs, resoudre_sudoku, analyser_solution
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    grid = data['grid']
    
    # Convertir la grille en un format [(i, j, k), ...] sans les valeurs 0
    grille_entree = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:  # Ignorer les cases vides (valeurs 0)
                grille_entree.append((i + 1, j + 1, grid[i][j]))

    # Générer le fichier DIMACS et résoudre le Sudoku
    generer_dimacs(grille_entree)
    solution = resoudre_sudoku()

    # Si aucune solution n'est trouvée
    if solution is None:
        return jsonify({"error": "Aucune solution trouvée"}), 400

    # Analyser la solution et convertir au format attendu
    grille_solution = analyser_solution(solution)
    grille_solution_format = [
        [grille_solution[i][j] for j in range(9)] for i in range(9)
    ]
    return jsonify(grille_solution_format)

@app.route('/download', methods=['GET'])
def download():
    # Chemin absolu pour le fichier ZIP
    zip_filename = os.path.join(os.getcwd(), "sudoku_files.zip")
    
    # Créer un fichier ZIP contenant sudoku.cnf et sudoku.out
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        if os.path.exists("sudoku.cnf"):
            zipf.write("sudoku.cnf", arcname="sudoku.cnf")  # Ajouter au ZIP
        if os.path.exists("sudoku.out"):
            zipf.write("sudoku.out", arcname="sudoku.out")  # Ajouter au ZIP

    # Vérifier si le fichier ZIP a été créé
    if not os.path.exists(zip_filename):
        return jsonify({"error": "Le fichier ZIP n'a pas pu être généré."}), 500

    # Envoyer le fichier ZIP au client
    return send_file(zip_filename, as_attachment=True)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8080/')  # Remplacez par l'adresse et le port de votre application

if __name__ == '__main__':
    Timer(1, open_browser).start()  # Délai de 1 seconde avant d'ouvrir le navigateur
    app.run(host='127.0.0.1', port=8080, debug=True)