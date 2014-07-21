# Steiner Triple Systems

# Find a set of n(n-1)/6 triples of distinct integer elements in {1,...,n} such that any two triples have at most one common element.

# CSPLib Problem 044 - http://www.csplib.org/Problems/prob044/

from Numberjack import *

def get_model(N):
    N_ROWS = N * (N - 1) / 6
    
    sol = Matrix(N_ROWS, N, 0, 1)

    model = Model([Sum(row) == 3 for row in sol.row])
        
    for i in range(N_ROWS):
        for j in range(i, N_ROWS):
                model += Sum([sol[i][k] == 1 and sol[j][k] == 1 for k in range(N)]) <= 1
    
    return sol, model

def solve(param):
    N = param['N']

    sol, model = get_model(N)

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
