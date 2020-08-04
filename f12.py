# print('X---XX')

import utils
import itertools
import numpy as np

def generate(X, seqType, args):
    '''
    # Note-1: args.gGap --> 1, 2, 3
    # Note-2: gGap --> ('X', 'X', 'X')
    :param X:
    :param seqType:
    :param args:
    :return:
    '''
    elements = utils.sequenceElements(seqType)
    m3 = list(itertools.product(elements, repeat=3))
    m = m3
    # print(m)

    T = []
    for x in X:
        t = []
        for i in range(1, args.gGap + 1, 1):
            V = utils.kmers(x, i + 2)
            # seqLength = len(x) - (i+2) + 1
            for gGap in m:
                # print(gGap[0], end='')
                # print('-'*i, end='')
                # print(gGap[1])
                # trackingFeatures.append(gGap[0] + '-' * i + gGap[1])
                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[-2] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                # print(C, end=',')
                t.append(C)
            #end-for
        #end-for
        t = np.array(t)
        t = t.reshape(-1, 1)
        T.append(t)
    # end-for
    T = np.array(T)
    # print(T.shape)

    totalFeature = 0
    if seqType == 'DNA' or seqType == 'RNA':
        totalFeature = (4*args.gGap*(4*4))
    else:
        if seqType == 'PROT':
            totalFeature = (20*args.gGap*(20*20))
        else: None
    #end-if
    np.save(arr=T, file='f12-{}'.format(totalFeature))
    print('f12-{}.npy generated.'.format(totalFeature))
#end-def