# Lam's Problem

# Consider a 111 by 111 binary matrix. 
# The goal is to put 11 zeros in each row in such a way that each column has 11 zeros,
# and each pair of rows must have exactly one zero in the same column.

# CSPLib Problem 025 - http://www.csplib.org/Problems/prob025/

from Numberjack import *

def get_model(N):
    # By definition a and b will have the same cardinality:
    matrix = Matrix(N, N, 0, 1)

    model = Model(
                    # Each row must contain 11 zeroes (rest of the 100 are 1s).
                    [Sum(row) == 100 for row in matrix.row],
                    
                    # Each column must contain 11 zeroes (rest of the 100 are 1s).
                    [Sum(col) == 100 for col in matrix.col],
                    
                    # Each pair of rows must have exactly one zero in the same column.
                    [[[Sum([matrix[row1][col], matrix[row2][col]]) == 1 for col in range(N)] for row2 in range(row1 + 1, N)] for row1 in range(N)])    

    return matrix, model

def solve(param):
    N = param['N']

    matrix, model = get_model(N)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()
    
    if solver.is_sat():
        print str(matrix)
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'N': 111, 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
