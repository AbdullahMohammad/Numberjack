# Crossfigures

# Crossfigures is basically a crosswords puzzle but instead of
# filling in words, we fill in numbers.
# There are clues provided - usually relations between the numbers
# that we need to fill in.

# Here we are solving this instance of a crossfigures puzzle:
# http://thinks.com/crosswords/number/xfig001.htm

# CSPLib Problem 021 - http://www.csplib.org/Problems/prob021/

from Numberjack import *

vars_across = VarArray(30, 0, 9999)
vars_down = VarArray(28, 0, 9999)
grid = Matrix(9, 9, -1, 9)

def variable_to_grid(n, i, j, s, orientation):
    global vars_across
    global vars_down
    global grid
    
    if orientation == "across":
        return [grid[i][j + k] == vars_across[n] / 10**k for k in range(s)]
    elif orientation == "down":
        return [grid[i + k][j] == vars_down[n] / 10**k for k in range(s)]
    else:
        print "Error! Unrecognized orientation \"" + orientation + "\"!"

def get_model():
    global vars_across
    global vars_down
    global grid    
    
    model = Model(  
                    # Across clues
                    vars_across[0] == vars_across[26] * 2,
                    vars_across[3] == vars_down[3] + 71,
                    vars_across[6] == vars_down[17] + 4,
                    vars_across[7] == vars_down[5] / 16,
                    vars_across[8] == vars_down[1] - 18,
                    vars_across[9] == 6 * 144 / 12,
                    vars_across[10] == vars_down[4] - 70,
                    vars_across[12] == vars_down[25] * vars_across[22],
                    vars_across[14] == vars_down[5] - 350,
                    vars_across[16] == vars_across[24] * vars_across[22],
                    vars_across[19] == -1, # Square number?
                    vars_across[22] == -1, # Prime number?
                    vars_across[23] == -1, # Square number?
                    vars_across[24] == vars_across[19] / 17,
                    vars_across[26] == vars_down[5] / 4,
                    vars_across[28] == 6 * 12,
                    vars_across[29] == vars_down[21] + 450,
                    
                    # Down clues
                    vars_down[0] == vars_across[0] + 27,
                    vars_down[1] == 5 * 12,
                    vars_down[2] == vars_across[29] + 888,
                    vars_down[3] == vars_across[16] * 2,
                    vars_down[4] == vars_across[28] / 12,
                    vars_down[5] == vars_across[27] * vars_across[22],
                    vars_down[9] == vars_across[9] + 4,
                    vars_down[11] == vars_across[23] * 3,
                    vars_down[13] == vars_across[12] / 16,
                    vars_down[15] == vars_down[27] * 15,
                    vars_down[16] == vars_across[12] - 399,
                    vars_down[17] == vars_across[28] / 18,
                    vars_down[18] == vars_down[21] - 94,
                    vars_down[19] == vars_across[19] - 9,
                    vars_down[20] == vars_across[24] - 52,
                    vars_down[21] == vars_down[19] * 6,
                    vars_down[25] == vars_across[23] * 5,
                    vars_down[27] == vars_down[20] + 27, 
                    
                    # Inferred across clues
                    [vars_across[i] >= 1000 & vars_across[i] <= 9999 for i in [0, 3, 12, 14, 16, 19, 28, 29]],
                    
                    [vars_across[i] >= 100 & vars_across[i] <= 999 for i in [7]],
                    
                    [vars_across[i] >= 10 & vars_across[i] <= 99 for i in [6, 8, 9, 10, 22, 23, 24, 27]],
                    
                    # Inferred down clues
                    [vars_down[i] >= 1000 & vars_down[i] <= 9999 for i in [0, 2, 3, 5, 16, 18, 19, 21]],
                    
                    [vars_down[i] >= 100 & vars_down[i] <= 999 for i in [13, 15]],
                    
                    [vars_down[i] >= 10 & vars_down[i] <= 99 for i in [1, 4, 9, 11, 17, 20, 25, 27]])
                
    # Positions of across clues in the format [i, j, s] where [i, j] is the cell and s is the size.
    across_pos = [
                    (0, 0, 0, 4), # 1
                    (), # 2
                    (), # 3
                    (3, 0, 5, 4), # 4
                    (), # 5
                    (), # 6
                    (6, 1, 0, 2), # 7
                    (7, 1, 3, 3), # 8
                    (8, 1, 7, 2), # 9
                    (9, 2, 2, 2), # 10
                    (10, 2, 5, 2), # 11
                    (), # 12
                    (12, 3, 0, 4), # 13
                    (), # 14
                    (14, 3, 5, 4), # 15
                    (), # 16
                    (16, 5, 0, 4), # 17
                    (), # 18
                    (), # 19
                    (19, 5, 5, 4), # 20
                    (), # 21 
                    (), # 22
                    (22, 6, 2, 2), # 23
                    (23, 6, 5, 2), # 24
                    (24, 7, 0, 2), # 25
                    (), # 26
                    (26, 7, 2, 3), # 27
                    (27, 7, 7, 2), # 28
                    (28, 8, 0, 4), # 29
                    (29, 8, 5, 4)] # 30
                    
    down_pos = [
                    (0, 0, 0, 4), # 1
                    (1, 0, 1, 2), # 2
                    (2, 0, 3, 4), # 3
                    (3, 0, 5, 4), # 4
                    (4, 0, 7, 2), # 5
                    (5, 0, 8, 4), # 6
                    (), # 7
                    (), # 8
                    (), # 9
                    (9, 2, 2, 2), # 10
                    (10, 2, 5, 2), # 11
                    (11, 2, 6, 2), # 12
                    (), # 13
                    (13, 3, 1, 3), # 14
                    (), # 15
                    (15, 3, 7, 3), # 16
                    (16, 5, 0, 4), # 17
                    (17, 5, 2, 2), # 18
                    (18, 5, 3, 4), # 19
                    (19, 5, 5, 4), # 20
                    (20, 5, 6, 2), # 21 
                    (21, 5, 8, 4), # 22
                    (), # 23
                    (), # 24
                    (), # 25
                    (25, 7, 1, 2), # 26
                    (), # 27
                    (27, 7, 7, 2), # 28
                    (), # 29
                    ()] # 30

    for clue in across_pos:
        if clue != ():
            n, i, j, s = clue
            model += variable_to_grid(n, i, j, s, "across")
        
    for clue in down_pos:
        if clue != ():
            n, i, j, s = clue
            model += variable_to_grid(n, i, j, s, "down")    

    return grid, model

def solve(param):
    grid, model = get_model()

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print "Solution"
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'solver': 'MiniSat', 'verbose': 1}
    param = input(default)
    solve(param)
