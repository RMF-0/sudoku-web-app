def validate_grid(grid):
    """Validates the Sudoku grid to ensure it follows the rules."""
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            # Validate rows
            if grid[i][j] != 0:
                if grid[i][j] in row:
                    return False
                row.add(grid[i][j])
            
            # Validate columns
            if grid[j][i] != 0:
                if grid[j][i] in col:
                    return False
                col.add(grid[j][i])
            
            # Validate 3x3 boxes
            box_row = 3 * (i // 3)
            box_col = 3 * (i % 3)
            if grid[box_row + j // 3][box_col + j % 3] != 0:
                if grid[box_row + j // 3][box_col + j % 3] in box:
                    return False
                box.add(grid[box_row + j // 3][box_col + j % 3])
    
    return True


def format_output(solution):
    """Formats the output of the solution into a 2D list."""
    grid = [[0] * 9 for _ in range(9)]
    for val in solution:
        if val > 0:
            k = (val - 1) % 9 + 1
            j = ((val - 1) // 9) % 9 + 1
            i = (val - 1) // 81 + 1
            grid[i - 1][j - 1] = k
    return grid