# 015: Schur's Lemma

# Given n balls, labelled 1 to n, put them into 3 boxes such that:
# For any triple of balls (x,y,z) with x+y=z, not all are in the same box.

# CSPLib Problem 015 - http://www.csplib.org/Problems/prob015/

from Numberjack import *


def get_model(N):

    balls = VarArray(N, 3)

    model = Model()

    for i in range(1, N + 1):
        for j in range(1, N - i + 1):
                # model += Sum([balls[i - 1] == balls[j - 1],
                #               balls[i - 1] == balls[i + j - 1],
                #               balls[j - 1] == balls[i + j - 1]]) < 3

                model += Disjunction([
                    balls[i - 1] != balls[j - 1],
                    balls[i - 1] != balls[i + j - 1],
                    balls[j - 1] != balls[i + j - 1]])

    return balls, model

def solve(param):
    N = param['N']

    balls, model = get_model(N)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print str(balls)
    elif solver.is_unsat():
        print "Unsatisifiable"
    else:
        print "Timed out"

if __name__ == '__main__':
    default = {'N': 12, 'solver': 'MiniSat', 'verbose': 1}
    param = input(default)
    solve(param)

