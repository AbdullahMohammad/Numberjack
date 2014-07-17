# Magic Hexagon

# Arrange the numbers 1 to 19 in the following pattern:
#   A,B,C
#  D,E,F,G
# H,I,J,K,L
#  M,N,O,P
#   Q,R,S

# All diagonals (horizontal, and two diagonal directions) must sub to 38.

# CSPLib Problem 023 - http://www.csplib.org/Problems/prob023/

from Numberjack import *

def get_model():
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s = VarArray(19, 1, 19)

    model = Model(
                    AllDiff([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]),
    
                    a + b + c == 38,
                    d + e + f + g == 38,
                    h + i + j + k + l == 38,
                    m + n + o + p == 38,
                    q + r + s == 38,
                    
                    a + d + h == 38,
                    b + e + i + m == 38,
                    c + f + j + n + q == 38,
                    g + k + o + r == 38,
                    l + p + s == 38,
                    
                    c + g + l == 38,
                    b + f + k + p == 38,
                    a + e + j + o + s == 38,
                    d + i + n + r == 38,
                    h + m + q == 38)    

    return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, model

def solve(param):
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, model = get_model()

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print "  ", str(a).zfill(2), str(b).zfill(2), str(c).zfill(2)
        print " ", str(d).zfill(2), str(e).zfill(2), str(f).zfill(2), str(g).zfill(2)
        print str(h).zfill(2), str(i).zfill(2), str(j).zfill(2), str(k).zfill(2), str(l).zfill(2)
        print " ", str(m).zfill(2), str(n).zfill(2), str(o).zfill(2), str(p).zfill(2)
        print "  ", str(q).zfill(2), str(r).zfill(2), str(s).zfill(2)
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
