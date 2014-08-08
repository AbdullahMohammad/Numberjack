# Magic Squares and Sequences - hettero squares variant
#
# An order n hetero square is a n by n matrix containing the
# numbers 1 to n^2, with each row, column and main diagonal
# summing to a different value.
#
# CSPlib Problem 019 - http://www.csplib.org/Problems/prob019/

from Numberjack import *


def get_model(N, data):
    square = Matrix(N, N, 1, N**2)

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
            Sum([square[i][N-i-1] for i in range(N)])]),

        # Values must match those in the data file.
        [(x == int(v)) for x, v in
            zip(square.flat, "".join(open(data)).split()) if v != '*'])

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
    default = {'N': 3, 'solver': 'Mistral', 'verbose': 1,
               'data': 'data/019-MagicSquaresAndSequences-HeteroSquares.txt'}
    param = input(default)
    solve(param)

