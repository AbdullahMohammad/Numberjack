# Steiner Triple Systems

# Find a set of n(n−1)/6 triples of distinct integer elements in {1,...,n} such that any two triples have at most one common element.

# CSPLib Problem 023 - http://www.csplib.org/Problems/prob044/

from Numberjack import *

def get_model(N):
    N_ROWS = N * (N - 1) / 6
    
    sol = Matrix[N_ROWS, 3, 1, N]
    
    cards = {}

    for i in range(1, N + 1):
        cards[i] = 2

    model = Model()

    # This model will not work for the problem.
            
    for i in range(N_ROWS):
        for j in range(i + 1, N_ROWS): 
            model += Gcc(sol.row[i] + sol.row[j], cards)

    return sol, model

def solve(param):
    N = param['N']

    sol, model = get_model()

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print str(sol)
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'N': 7, 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
