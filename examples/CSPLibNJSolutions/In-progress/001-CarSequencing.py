# Car Sequencing

# A number of non-identical cars are to be produced. They are not identical
# as there are production options for each car.

# A production station can only process a set percentage of the production line at
# any one time, so out of every group of N consecutive cars, only L of them can
# require the option that station installs.

# Each car belongs to a class. A class defines which options a car needs. There are
# various different classes, but multiple cars can belong to the same class.

# CSPLib Problem 001 - http://www.csplib.org/Problems/prob001

from Numberjack import *

def get_model(N, O, C, options, classes):
    STAT_CAP = [[0, 0] for i in range(O)] # Represents the station capacity. STAT_CAP[i][0] tells us the max number of cars with option i out of every STAT_CAP[i][1] consecutive cars
    
    temp = 0
    for line in open(options):
        i = 0
        for option in line.split():
            #print ">", option, "<"
            STAT_CAP[i][temp] = int(option)
            i += 1
        temp += 1
    
    CLS = [[0 for i in range(O+1)] for j in range(C)] # Represents the classes. The first element in each row is the number of cars of that class. The next O elements designate whether or not that option is to be installed for cars of that class.

    j = 0
    for line in open(classes):
        i = 0
        for x in line.split()[1:]:
            CLS[j][i] = int(x)
            i += 1
        j += 1    

    order = VarArray(N, 0, C) # The order in which the cars of their respective class number will be made in
    options = Matrix(N, O, 0, 1) # A representation of the order VarArray in terms of which options are to be installed at each step    
    
    cards = {}
    for i in range(C):
        cards[i] = (CLS[i][0], CLS[i][0])
    
    model = Model(
                    # Ensure that the options matrix is a correct representation of the order VarArray
                    
                    ##### ERROR: List indices must be of type int not Variable (?)
                    
                    #[[x == y for x, y in zip(options[i], CLS[order[i]][1:])] for i in range(N)],
                    
                    
                    # Ensure that the number of cars from each class is exactly as specified
                    Gcc(order, cards)
                )    
    
    # Ensure for each option that the corresponding production station can cope according to its capacity
    for i in range(O):
        for j in range(N - STAT_CAP[i][1]):
            model += Sum([options.col[i][j:j+STAT_CAP[i][1]] for j in range(N - STAT_CAP[i][1])]) <= STAT_CAP[i][0]

    return order, model

def solve(param):
    N = param['N']
    O = param['O']
    C = param['C']
    options = param['options']
    classes = param['classes']

    order, model = get_model(N, O, C, options, classes)

    solver = model.load(param['solver'])
    solver.setVerbosity(param['verbose'])
    solver.solve()

    if solver.is_sat():
        print str(order)
    elif solver.is_unsat():
        print "Unsatisfiable"
    else:
        print "Timed out"
        
if __name__ == '__main__':
    default = {'N': 10, 'O': 5, 'C': 6, 'options': 'data/001-CarSequencingOptions.txt', 'classes': 'data/001-CarSequencingClasses.txt', 'solver': 'Mistral', 'verbose': 1}
    param = input(default)
    solve(param)
