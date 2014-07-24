# Langford's number problem

# Given k sets of numbers 1 to n, arrange them all in
# such a way that each number m, appears m positions from the
# next number m.

# CSPLib Problem 024 - http://www.csplib.org/Problems/prob024/

from Numberjack import *

def get_model(K, N):
    seq = Matrix(N, K, 1, N - 1) # Each row m contains the positions of the number m in the sequence
    
    model = Model(
                    # All numbers have to be at a different position.
                    AllDiff(seq.flat),
    
                    # Each number m has to be m positions from its next occurence
                    [[Abs(seq[m][i] - seq[m][i]) == m+1 for i in range(K)] for m in range(N)])
    
    return seq, model

def solve(param):
    seq, model = get_model(param['K'], param['N'])

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print str(seq)
    elif solver.is_unsat():
        print "Unsatisfiable"   
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'K': 2, 'N': 4, 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
