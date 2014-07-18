# Nonogram

# Nonograms are a popular puzzle where one has to shade in squares in a grid so that
# blocks of consecutive shaded squares satisfy constraints given for each row and column. 

# Constraints typically indicate the sequence of shaded blocks (e.g. 3,1,2 means that
# there is a block of 3, then a gap of unspecified size, a block of length 1, another
# gap, and then a block of length 2).

# CSPLib Problem 012 - http://www.csplib.org/Problems/prob012/

from Numberjack import *

def get_model(data):


    with open(data) as f:
        lines = f.read().split('\n')

        N_ROWS = int(lines[0])
        N_COLS = int(lines[1])
        row_const = [[int(y) for y in x.split()] for x in lines[2:N_ROWS + 2]]
        col_const = [[int(y) for y in x.split()] for x in lines[N_ROWS + 2:N_ROWS + N_COLS + 2]]

    grid = Matrix(N_ROWS, N_COLS, 0, 1)

    model = Model()
    
    # Constraints on rows
    count = 0
    for row in row_const:
        shades = 0
        gaps = -1
        cards = {}
        
        for const in row:
            shades += const
            gaps += 1
        
            cards[0] = (gaps, N_COLS)
            cards[1] = (shades, N_COLS)
                    
        model += Gcc(grid.row[count], cards)
        count += 1            
        
    # Constraints on columns
    count = 0
    for col in col_const:
        shades = 0
        gaps = -1
        cards = {}
        
        for const in col:
            shades += const
            gaps += 1
        
            cards[0] = (gaps, N_ROWS)
            cards[1] = (shades, N_ROWS)
                    
        model += Gcc(grid.col[count], cards)
        count += 1            
        
    return grid, model

def solve(param):
    data = param['data']

    grid, model = get_model(data)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print grid
        
        print
        print "Visual:"
        for line in grid:
            out = ""
            for val in line:
                val = val.get_value()
                
                if val == 1:
                    out += '#'
                elif val == 0:
                    out += ' '
                else:
                    print "Unknown value:", str(val)
            print out
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"

if __name__ == '__main__':
    default = {'data': 'data/012-Nonogram.txt', 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)

