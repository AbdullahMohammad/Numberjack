# Unsatisfiable for some reason.

# Steiner Triple Systems

# Find a set of n(n-1)/6 triples of distinct integer elements in {1,...,n} such that any two triples have at most one common element.

# CSPLib Problem 044 - http://www.csplib.org/Problems/prob044/

from Numberjack import *

def get_model(N):
    N_ROWS = N * (N - 1) / 6
    
    triples = Matrix(N_ROWS, N, 0, 1)

    model = Model([Sum(row) == 3 for row in triples.row])
        
    for i in range(N_ROWS):
        for j in range(i + 1, N_ROWS):
                model += Sum([triples[i][k] == triples[j][k] for k in range(N) if triples[i][k] == 1]) <= 1
    
    return triples, model

def solve(param):
    N = param['N']

    triples, model = get_model(N)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        for triple in triples:
            for i in range(N):
                if triple[i] == 1:
                    print (i + 1),
        print
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'N': 7, 'solver': 'MiniSat', 'verbose': 1}
    param = input(default)
    solve(param)
