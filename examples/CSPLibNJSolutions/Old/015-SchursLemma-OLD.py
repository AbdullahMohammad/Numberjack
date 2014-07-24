# 015: Schur's Lemma

# Given n balls, labelled 1 to n, put them into 3 boxes such that:
# For any triple of balls (x,y,z) with x+y=z, not all are in the same box.

# CSPLib Problem 015 - http://www.csplib.org/Problems/prob015/

from Numberjack import *

def get_model(N):
    balls = VarArray(N, 1, 3)

    model = Model(
                    [[[balls[i] != balls[j] | balls[i] != balls[k] | balls[j] != balls[k] \
                     for i in range(N) if i + j == k & i != j & j != k] \
                     for j in range(N)] \
                     for k in range(N)]
                )    

    return balls, model

def solve(param):
    N = param['N']

    balls, model = get_model(N)

    solver = model.load(param['solver'])

    solver.solve()
    out = ""
    if solver.is_sat():
        print str(balls)
    
if __name__ == '__main__':
    default = {'N': 13,'solver': 'Mistral'}
    param = input(default)
    solve(param)
