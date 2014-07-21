# Balanced Incomplete Block Designs

# Fill in a binary matrix of size v * b in such a way that:
# - Every row sums to r.
# - Every column sums to k.
# - Scalar product equals p for any pair of rows.

# CSPLib Problem 028 - http://www.csplib.org/Problems/prob028/

from Numberjack import *

def get_model(V, B, R, K, P):
    # By definition a and b will have the same cardinality:
    matrix = Matrix(V, B, 0, 1)

    model = Model(
                    # Each row must contain R ones.
                    Sum([row for row in matrix.row]) == R,
                    
                    # Each column must contain K ones.
                    Sum([col for col in matrix.col]) == K)    

    # Every pair of row must have a scalar product of P.
    for i in range(V):
        for j in range(i, V):
            model += Sum([matrix[i][k] == 1 and matrix[j][k] == 1 for k in range(B)]) == P

            return matrix, model

def solve(param):
    V = param['V']
    B = param['B']
    R = param['R']
    K = param['K']
    P = param['P']

    matrix, model = get_model(V, B, R, K, P)

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
    default = {'V': 7, 'B': 7, 'R': 3, 'K': 3, 'P': 1, 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
