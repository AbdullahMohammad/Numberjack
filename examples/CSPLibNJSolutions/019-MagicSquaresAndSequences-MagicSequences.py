# Magic Squares and Sequences - magic sequences variant

# A magic sequence of length n is a sequence of integers x[0]..x[n-1] between 0 and n-1,
# such that for all i in 0 to n-1, the number i occurs exactly x[i] times in the sequence. 

# For instance, 6,2,1,0,0,0,1,0,0,0 is a magic sequence since 0 occurs 6 times in it, 1 occurs twice, ...

# CSPlib Problem 019 - http://www.csplib.org/Problems/prob019/

from Numberjack import *

def get_model(N):
    seq = VarArray(N, 0, N-1)

    # A boolean matrix to represent which positions each number appears at in the sequence. 
    # (Rows = numbers in sequence. Columns = positions in sequence).
    count = Matrix(N, N, 0, 1)

    model = Model(
                    # Each position in the sequence can have only one value at it.
                    [Sum(col) == 1 for col in count.col],
                    
                    # Each number must appear at the position the matrix specifies.
                    [count[seq[i]][i] == 1 for i in range(N)],
                    
                    # Each number i must appear as many times in the sequence as the number at position i.
                    [seq[i] == Sum(count[i]) for i in range(N)])
    
    return seq, model

def solve(param):
    N = param['N']

    seq, model = get_model(N)

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
    default = {'N': 10, 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
