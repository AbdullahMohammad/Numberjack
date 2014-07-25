# Stuck: Probably needs http://sofdem.github.io/gccat/aux/pdf/alldifferent_consecutive_values.pdf

# Magic Squares and Sequences - anti-magic squares variant

# An order n magic square is a n by n matrix containing the numbers 1 to n^2, with each row, column and main diagonal equal the same sum.

# CSPlib Problem 019 - http://www.csplib.org/Problems/prob019/

from Numberjack import *

def get_model(N, data):
    square = Matrix(N, N, 1, N**2)
    
    # The minimum sum of a row is the sum of the first N smallest numbers in the domain of 1 to N^2.
    # That is equivalent to the sum of the numbers 1 to N.
    minimum = N * (N+1) / 2
    
    # The maximum sum of a row is the sum of the last N biggest numbers in the domain of 1 to N^2.
    # That is equivalent to the difference between the sum of the numbers 1 to N^2 and the sum of the numbers 1 to (N^2 - N) 
    maximum = (N**2 * (N**2 + 1) / 2) - ((N**2 - N) * (N**2 - N + 1) / 2) 
    
    # There are 2*N + 2 sums: N rows, N columns and 2 diagonals.
    sums_list = VarArray(2 * N + 2, minimum, maximum)

    model = Model(
                    # Square must contain all numbers from 1 to N^2.
                    AllDiff(square.flat),
                    
                    # All sums must be different.
                    AllDiff([
                    
                        # Rows
                        [Sum(row) for row in square.row], 
                        
                        # Columns
                        [Sum(col) for col in square.col], 
                        
                        # Top-left to bottom-right diagonal
                        Sum([square[i][i] for i in range(N)]),
                        
                        # Top-right to bottom-left diagonal
                        Sum([square[i][N-i-1] for i in range(N)])
                    ]),
    
                    # Need to use this: http://sofdem.github.io/gccat/aux/pdf/alldifferent_consecutive_values.pdf ???
    
                    # Values must match those in the data file.
                    [(x == int(v)) for x, v in zip(square.flat, "".join(open(data)).split()) if v != '*'])
    
    return square, model

def solve(param):
    N = param['N']
    data = param['data']

    square, model = get_model(N, data)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print str(square)
    elif solver.is_unsat():
        print "Unsatisfiable" 
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'N': 3, 'data': 'data/019-MagicSquaresAndSequences-AntiMagicSquares.txt', 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
