# Synchronous Optical Networking (SONET) Problem
# Unlimited Traffic Capacity version
#
# We are given a set of nodes and rings. Each pair of nodes has
# a demand between them, which, in the unlimited version, is
# whether the two nodes need to be connected or not. Nodes can
# be connected if they are on the same ring. Rings have a limit
# on the number of nodes they can have on them.
#
# CSPLib Problem 056 - http://www.csplib.org/Problems/prob056/

from Numberjack import *


def get_model(N, R, pairs_data, rings_data):
    rings = Matrix(R, N, 0, 1)

    pairs = []
    with open(pairs_data) as p:
        for pair in p:
            pairs.append([int(pair.split()[0]), int(pair.split()[1])])

    model = Model(
        # Ensure that nodes that need to be connected are on the same ring.
        [Disjunction([rings[i][pair[0]] + rings[i][pair[1]] == 2
         for i in range(R)]) for pair in pairs],

        # Ensure that none of the rings exceed their limit.
        [Sum(ring) <= int(lim) for ring, lim in zip(rings.row,
         "".join(open(rings_data)).split())],

        # Try to minimise the number of times a node is placed on a ring.
        Minimise(Sum(rings.flat)))

    return rings, model


def solve(param):
    N = param['N']
    R = param['R']
    pairs_data = param['pairs_data']
    rings_data = param['rings_data']

    rings, model = get_model(N, R, pairs_data, rings_data)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        for ring in rings:
            print ring
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"


if __name__ == '__main__':
    default = {
        'N': 5, 'R': 4, 'solver': 'MiniSat', 'verbose': 1,
        'pairs_data': 'data/056-SONETProblemPairs.txt',
        'rings_data': 'data/056-SONETProblemRings.txt'}
    param = input(default)
    solve(param)

