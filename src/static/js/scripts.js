document.addEventListener("DOMContentLoaded", function() {
    const solveButton = document.getElementById("solve-button");
    const resetButton = document.getElementById("reset-button");
    const downloadButton = document.getElementById("download-button");
    const grid = document.getElementById("sudoku-grid");

    // Mémoriser les cases où l'utilisateur a saisi une valeur
    const userInputs = new Set();

    // Ajouter un événement pour suivre les saisies utilisateur
    grid.addEventListener("input", function(event) {
        const cell = event.target;
        if (cell.tagName === "INPUT" && cell.value) {
            userInputs.add(cell.id); // Mémoriser l'ID de la cellule
        }
    });

    solveButton.addEventListener("click", function() {
        const values = [];
        for (let i = 0; i < 9; i++) {
            const row = [];
            for (let j = 0; j < 9; j++) {
                const cell = grid.rows[i].cells[j].querySelector("input");
                row.push(cell.value ? parseInt(cell.value) : 0);
            }
            values.push(row);
        }

        fetch("/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ grid: values })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("No solution found.");
            }
            return response.json();
        })
        .then(data => {
            updateGrid(data); // Mettre à jour la grille avec la solution
        })
        .catch(error => {
            alert(error.message);
            console.error("Error:", error);
        });
    });

    resetButton.addEventListener("click", function() {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = grid.rows[i].cells[j].querySelector("input");
                cell.value = ""; // Réinitialise chaque cellule
                cell.style.color = ""; // Réinitialise la couleur
            }
        }
        userInputs.clear(); // Réinitialise les saisies utilisateur
    });

    downloadButton.addEventListener("click", function() {
        window.location.href = "/download";
    });

    function updateGrid(solution) {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = grid.rows[i].cells[j].querySelector("input");
                if (!userInputs.has(cell.id)) {
                    cell.value = solution[i][j]; // Mettre à jour avec la solution
                    cell.style.color = "blue"; // Afficher en bleu les valeurs générées
                }
            }
        }
    }
});