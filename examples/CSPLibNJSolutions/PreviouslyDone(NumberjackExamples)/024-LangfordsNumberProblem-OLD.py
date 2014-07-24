# Langford's number problem

# Given k sets of numbers 1 to n, arrange them all in
# such a way that each number m, appears m positions from the
# next number m.

# CSPLib Problem 024 - http://www.csplib.org/Problems/prob024/

from Numberjack import *

def abs_val(a, b):
	res = a - b
	if res < 0:
		res *= -1
	return res

curr_pos = -1
next_pos = -1

def current_position(seq, m):
    global curr_pos
    
    if curr_pos == -1:
        return next_position(seq, m)
    else:
        return curr_pos
    
def next_position(seq, m):
    global curr_pos
    global next_pos
        
    curr_pos = next_pos
    next_pos += 1
    while seq[next_pos].get_value() != m:
        next_pos += 1
        
    return next_pos
    
# test_positions was finding all positions of number m in seq, and checking that they are all m distance apart. Returned True if so and False otherwise.
    
        
def get_model(K, N):
    seq = VarArray(N * K, 1, N)
    
    cards = {}
    for i in range(1, N + 1):
        cards[i] = (K, K)
    
    pos = [1, 2, 3, 4]
    
    model = Model(
                    # Each number 1 to n has to occur exactly k times.
                    Gcc(seq, cards),
 
                    # Each number m has to be m positions from its next occurence
#                    [[abs_val(pos[i], pos[i + 1]) == m for i in range(K-1) with pos = [j for j, val in enumerate(seq) if val.get_value() == m]] for m in range(N)])
#                    [abs_val(current_position(seq, m), next_position(seq, m)) == m + 1 for m in range(N)])                   
#                    [test_positions(seq, m, K) == True for m in range(N)])
    
    return seq, model

def solve(param):
    K = param['K']
    N = param['N']

    seq, model = get_model(K, N)

    solver = model.load(param['solver'])

    solver.solve()

    if solver.is_sat():
        print str(seq)
    
if __name__ == '__main__':
    default = {'K': 2, 'N': 4, 'solver': 'Mistral'}
    param = input(default)
    print solve(param)
