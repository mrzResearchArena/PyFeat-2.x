import utils
import itertools
import numpy as np
import save

def generate(X, seqType, args):
    '''
    # Reference-1: (http://rosalind.info/glossary/k-mer-composition/) # It is also called "k-mer composition".
    # Reference-2: iRecSpot-EF: https://www.sciencedirect.com/science/article/abs/pii/S0010482518302981
    :param X:
    :param seqType:
    :param args:
    :return:
    '''

    elements = utils.sequenceElements(seqType)
    # print(elements)
    # print(args.gGap)
    # print(args.kTuple)

    T = []
    for x in X:
        x = x[:args.terminusLength]
        t = []
        for i in range(1, args.kTuple + 1, 1):
            v = list(itertools.product(elements, repeat=i))
            # seqLength = len(x) - i + 1
            for i in v:
                # print(x.count(''.join(i)), end=',')
                t.append(x.count(''.join(i)))
        ### --- ###
        t = np.array(t)
        # t = t.reshape(-1, 1)
        # print(t.shape)
        T.append(t)
    #end-for

    T = np.array(T)
    # print(T.shape)

    totalFeature = 0
    if seqType == 'DNA' or seqType == 'RNA':
        totalFeature = np.sum([4**(i) for i in range(1, args.kTuple+1)])
    else:
        if seqType == 'PROT':
            totalFeature = np.sum([20**(i) for i in range(1, args.kTuple+1)])
        else: None
    #end-if

    save.datasetSave(T, totalFeature, 'fkmer')
#end-def
