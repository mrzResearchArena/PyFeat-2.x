CRED = '\033[91m'
CEND = '\033[0m'
# Thanks to (https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python) for the color blog!

import numpy as np
import sys

def shapeCheck(Ax):
    '''
    :param Ax:
    :return:
    '''

    numberSample = []
    eachSample = []
    for i in range(len(Ax)):
        numberSample.append(Ax[i].shape[0])
        eachSample.append(Ax[i].shape[1])
    #end-for
    return numberSample, eachSample
#end-def

def merge(*args):
    '''
    :param args:
    :return:
    '''

    args = args[0]   ### ignore!
    file = args[1]   ### ignore!
    # print(file)
    args = args[2:]
    # print(args)
    # print(np.load(args[0]).shape)
    # print(np.load(args[1]).shape)

    Ax = [] # Array --> Ax
    for i in args:
        Ax.append(np.load(i))
    #end-for

    numberSample, eachSample = shapeCheck(Ax)
    assert len(set(numberSample)) == 1, CRED+'Shape Mismatch! Please choose the same categories features.'+CEND
    assert len(set(eachSample))   == 1, CRED+'Shape Mismatch! Please choose the same categories features.'+CEND

    T = []
    for i in range(len(Ax[0])):
        t = []
        for i in range(len(Ax)):
            t.append(Ax[i][0])
        #end-for
        t = tuple(t)
        T.append(np.concatenate((t), axis=1))
        # print('----------------------------')
    #end-for
    T = np.array(T)
    # print(T)
    # print(T.shape)
    np.save(file='Extracted-Features/{}'.format(file), arr=T)
    print('\'{}.npy\' generated; and the new shape: {}.'.format(file, T.shape))
#end-def

###################
merge(sys.argv) ###
###################