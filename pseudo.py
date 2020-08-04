import utils
import itertools
import numpy as np

def generate(X, seqType, args):
    elements = utils.sequenceElements(seqType)
    # print(elements)
    # print(args.gGap)
    # print(args.kTuple)

    T = []
    for x in X:
        t = []
        for i in range(1, args.kTuple + 1, 1):
            v = list(itertools.product(elements, repeat=i))
            # seqLength = len(x) - i + 1
            for i in v:
                # print(x.count(''.join(i)), end=',')
                t.append(x.count(''.join(i)))
        ### --- ###
        t = np.array(t).reshape(-1, 1)
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
    np.save(arr=T, file='pseudo-{}'.format(totalFeature))
    print('pseudo-{}.npy generated.'.format(totalFeature))
#end-def