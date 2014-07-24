# Magic Squares and Sequences

# CSPlib Problem 019 - http://www.csplib.org/Problems/prob019/

from Numberjack import *

def get_model(N, clues, cages):
    grid = Matrix(N*N, N*N, 1, N*N)

    sudoku = Model(
                    )
    
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
