# Equidistant Frequency Permutation Arrays
#
# Find a set E of v sequences such that:
# - Each sequence contains each of the symbols (1 to q) n times.
# - The Hamming distance between any pair of sequences is exactly d.
#
# CSPLib Problem 055 - http://www.csplib.org/Problems/prob055/

from Numberjack import *


def get_model(V, Q, N, D):
    # By definition a and b will have the same cardinality:
    matrix = Matrix(V, Q*N, 0, Q-1)

    # Setting up the cardinality limits for the first constraint.
    cards = {}
    for i in range(0, Q):
        cards[i] = (N, N)

    model = Model(
        # Each sequence must contain each symbol n times.
        [Gcc(matrix.row[i], cards) for i in range(V)])

    for i in range(V):
        for j in range(i + 1, V):
            model += Sum([matrix[i][k] != matrix[j][k]
                         for k in range(Q*N)]) == D

    return matrix, model


def solve(param):
    V = param['V']
    Q = param['Q']
    N = param['N']
    D = param['D']

    matrix, model = get_model(V, Q, N, D)

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
    default = {'V': 5, 'Q': 3, 'N': 2, 'D': 4, 'solver': 'Mistral',
               'verbose': 1}
    param = input(default)
    solve(param)

