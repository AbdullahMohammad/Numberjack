# Not sure why it's saying unsatisfiable.

# Perfect Square Placement

# Given N squares of varying sizes, and a master square of size S, place the N squares in a such a
# way that none of the squares overlap. The sum of the surface areas of the smaller squares should
# be equal to the surface area of the master square.

# CSPLib Problem 009 - http://www.csplib.org/Problems/prob009/

from Numberjack import *

def get_model(N, S, data):
    # X coordinates are in the 0th position in each row of the matrix
    X = 0
    # Y coordinates are in the 1st position in each row of the matrix
    Y = 1

    # Each row in the matrix represents the bottom-left corner co-ordinates of a square, 
    # relative to the master square, where (0,0) is the bottom-left corner of the master square.
    sq_pos = Matrix(N, 2, 0, S)

    # The sizes of the squares
    sq_size = VarArray(N, 1, S)

    model = Model(
                    # Sizes should be as specified in the data file.
                    [(sq_size[i] == int(size)) for i, size in zip(range(N), "".join(open(data)).split())])
                    
    for i in range(N):
        # Square should fit in master square
        model += sq_pos[i][X] + sq_size[i] <= S
        model += sq_pos[i][Y] + sq_size[i] <= S
        
        # No squares should overlap.
        for j in range(i + 1, N):
            model += sq_pos[i][X] != sq_pos[j][X]
            model += sq_pos[i][Y] != sq_pos[j][Y]
            
            model += ((sq_pos[i][X] + sq_size[i] <= sq_pos[j][X]) | (sq_pos[j][X] + sq_size[j] <= sq_pos[i][X]))
            
            model += ((sq_pos[i][Y] + sq_size[i] <= sq_pos[j][Y]) | (sq_pos[j][Y] + sq_size[j] <= sq_pos[i][Y]))
            
    return sq_pos, sq_size, model

def solve(param):
    N = param['N']
    S = param['S']
    data = param['data']

    sq_pos, sq_size, model = get_model(N, S, data)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        for i in range(N):
            print str(sq_size[i]), str(sq_pos[i])
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'N': 21, 'S': 121,'data': 'data/009-PerfectSquarePlacement.txt', 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
