# Crossfigures


# CSPLib Problem 021 - http://www.csplib.org/Problems/prob021/

from Numberjack import *

def get_model(data):
    
	
	grid = Matrix()
	
    model = Model(
				)

    return grid, model

def solve(param):
    data = param['data']
	
	grid, model = get_model(data)

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
    default = {'data': 'data/021-Crossfigures.txt', 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)