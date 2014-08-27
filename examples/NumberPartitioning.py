# Number Partitioning
#
# In this problem, the numbers 1 to N must be arranged in two
# different groups A and B in such a way that:
# 1. A and B have the same cardinality.
# 2. The sum of numbers in A equals the sum of numbers in B.
# 3. The sum of the squares of numbers in A equals the sum of
# the squares of numbers in B.
#
# CSPLib Problem 049 - http://www.csplib.org/Problems/prob049/
#
# Note: There is no solution for N < 8! Also, there is no solution
# if N is not a multiple of 4! (Source: CSPLib - see above link.)

from Numberjack import *


def get_model(N):
    # By definition a and b will have the same cardinality:
    a = VarArray(N / 2, 1, N)
    b = VarArray(N / 2, 1, N)

    model = Model(
        # Each of the numbers 1 to N must be present exactly once.
        AllDiff([x for x in a+b]),

        # The sum of numbers in A equals the sum of numbers in B.
        Sum(a) == Sum(b),

        # The sum of the squares of numbers in A equals the sum of
        # the squares of numbers in B.
        Sum([x*x for x in a]) == Sum([y*y for y in b]))

    return a, b, model


def solve(param):
    N = param['N']

    a, b, model = get_model(N)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print "A: " + str(a) + "\n" + "B: " + str(b)
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"


if __name__ == '__main__':
    default = {'N': 8, 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)

