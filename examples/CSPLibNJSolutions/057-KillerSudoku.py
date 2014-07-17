# Killer Sudoku

# Killer Sudoku is a Sudoku puzzle with a twist.

# The standard Sudoku puzzle is a 9x9 matrix to be filled out in such a way that
# each row, column and each of the 3x3 sub-matrices would contain the numbers 1 to 9.

# In Killer Sudoku, there is one extra constraint. There are so-called "cages" which
# are much like the 3x3 sub-matrices. They may contain at most one of each number (1 to 9)
# and the numbers' sum must be equal to the cage's number (see CSPLib link).

# CSPlib Problem 057 - http://www.csplib.org/Problems/prob057/

from Numberjack import *

def get_model(N, clues, cages):
    grid = Matrix(N*N, N*N, 1, N*N)

    sudoku = Model(
                    [AllDiff(row) for row in grid.row],
                    [AllDiff(col) for col in grid.col],
                    
                    # Contents of sub-matrices must be distinct.
                    [AllDiff(grid[x:x + N, y:y + N]) for x in range(0, N*N, N) for y in range(0, N * N, N)],
                    
                    # Given solved cells. (Is this present in current problem?)
                    #[(x == int(v)) for x, v in zip(grid.flat, "".join(open(clues)).split()) if v != '*'],
                    
                    # Contents of cages must be distinct. [1:] to ignore the sum value.
                    [AllDiff([grid.flat[int(cell)] for cell in cage.split()[1:]]) for cage in open(cages)],
                    #[AllDiff(cells) for cage in open(cages) for cells in grid.flat if cells.position in cage.split()[1:]],
                    
                    # Contents of cages must add up to the cage's number.
                    [Sum([grid.flat[int(cell)] for cell in cage.split()[1:]]) == int(cage.split()[0]) for cage in open(cages)])
    
    return grid, sudoku

def solve(param):
    N = param['N']
    clues = param['hints']
    cages = param['cages']

    grid, sudoku = get_model(N, clues, cages)

    solver = sudoku.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print str(grid)
    elif solver.is_unsat():
        print "Unsatisfiable" 
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'N': 3, 'solver': 'Mistral', 'hints': 'data/057-KillerSudokuHints.txt', 'cages': 'data/057-KillerSudokuCages.txt', 'verbose': 1}
    param = input(default)
    solve(param)
