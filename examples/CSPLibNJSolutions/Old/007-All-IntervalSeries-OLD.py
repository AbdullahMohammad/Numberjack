# All-Interval Series

# Arrange the numbers 1 to n in a vector s, such that:
# the interval vector v=(|s2-s1|,|s3-s2|,...,|sn-sn-1|) is a permutation of {1,2,...,n-1}. 

# CSPLib Problem 007 - http://www.csplib.org/Problems/prob007/

from Numberjack import *

def get_model(N):
    series = VarArray(N, 0, N - 1)

    model = Model(
                    AllDiff(series),
                    AllDiff([absVal(series[i], series[i+1]) for i in range(N-1)]))    

    return series, model

def solve(param):
    N = param['N']

    series, model = get_model(N)

    solver = model.load(param['solver'])

    solver.solve()
    out = ""
    if solver.is_sat():
        print str(series)
        
        print "DEBUG: Absolute differences:",
        for i in range(N - 1):
            print absVal(int(str(series[i])), int(str(series[i + 1]))),
    
if __name__ == '__main__':
    default = {'N': 12,'solver': 'Mistral'}
    param = input(default)
    solve(param)
