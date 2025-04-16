document.addEventListener("DOMContentLoaded", function () {
    const solveButton = document.getElementById("solve-button");
    const resetButton = document.getElementById("reset-button");
    const downloadButton = document.getElementById("download-button");
    const generateButton = document.getElementById("generate-button");
    const fillPercentage = document.getElementById("fill-percentage");
    const grid = document.getElementById("sudoku-grid");

    // Mémoriser les cases où l'utilisateur a saisi une valeur
    const userInputs = new Set();

    // Mémoriser les cases générées aléatoirement
    const generatedCells = new Set();

    grid.addEventListener("input", function (event) {
        const cell = event.target;
        if (cell.tagName === "INPUT") {
            if (cell.value) {
                userInputs.add(cell.id);
                cell.classList.add("user-input");
            } else {
                userInputs.delete(cell.id);
                cell.classList.remove("user-input");
            }
        }
    });

    solveButton.addEventListener("click", function () {
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
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ grid: values }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("No solution found.");
                }
                return response.json();
            })
            .then((data) => {
                updateGrid(data);
            })
            .catch((error) => {
                alert(error.message);
                console.error("Error:", error);
            });
    });

    resetButton.addEventListener("click", function () {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = grid.rows[i].cells[j].querySelector("input");
                cell.value = "";
                cell.classList.remove("user-input", "generated", "solution");
            }
        }
        userInputs.clear();
        generatedCells.clear();
    });

    downloadButton.addEventListener("click", function () {
        window.location.href = "/download";
    });

    generateButton.addEventListener("click", function () {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = grid.rows[i].cells[j].querySelector("input");
                cell.value = "";
                cell.classList.remove("user-input", "generated", "solution");
            }
        }
        userInputs.clear();
        generatedCells.clear();

        const percentage = parseInt(fillPercentage.value);
        const initialGrid = generateInitialGrid();
        fetch("/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ grid: initialGrid }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Erreur lors de la génération de la grille.");
                }
                return response.json();
            })
            .then((data) => {
                displayPartialGrid(data, percentage);
            })
            .catch((error) => {
                alert(error.message);
                console.error("Error:", error);
            });
    });

    function updateGrid(solution) {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = grid.rows[i].cells[j].querySelector("input");
                const cellId = `cell-${i}-${j}`;
                if (generatedCells.has(cellId)) {
                    cell.classList.add("generated");
                } else if (!userInputs.has(cellId)) {
                    cell.value = solution[i][j];
                    cell.classList.add("solution");
                }
            }
        }
    }

    function generateInitialGrid() {
        const grid = Array.from({ length: 9 }, () => Array(9).fill(0));
        const numbers = Array.from({ length: 9 }, (_, i) => i + 1).sort(() => Math.random() - 0.5);

        for (let region = 0; region < 9; region++) {
            const startRow = Math.floor(region / 3) * 3;
            const startCol = (region % 3) * 3;
            const num = numbers[region];

            let placed = false;
            while (!placed) {
                const row = startRow + Math.floor(Math.random() * 3);
                const col = startCol + Math.floor(Math.random() * 3);
                if (grid[row][col] === 0) {
                    grid[row][col] = num;
                    placed = true;
                }
            }
        }

        return grid;
    }

    function displayPartialGrid(solution, percentage) {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = grid.rows[i].cells[j].querySelector("input");
                cell.value = "";
                cell.classList.remove("user-input", "generated", "solution");
            }
        }

        const totalCells = Math.floor((81 * percentage) / 100);
        const filledPositions = new Set();

        while (filledPositions.size < totalCells) {
            const i = Math.floor(Math.random() * 9);
            const j = Math.floor(Math.random() * 9);
            const position = `${i}-${j}`;
            const cellId = `cell-${i}-${j}`;

            if (!filledPositions.has(position)) {
                filledPositions.add(position);
                generatedCells.add(cellId);
                const cell = grid.rows[i].cells[j].querySelector("input");
                cell.value = solution[i][j];
                cell.classList.add("generated");
            }
        }
    }
});