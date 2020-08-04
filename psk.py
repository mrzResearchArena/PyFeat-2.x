import numpy as np
import itertools
import utils


def generate(X, seqType, args):
    if seqType == 'DNA' or seqType == 'RNA':
        p = [0]*(4**args.kTuple)
    else:
        if seqType == 'PROT':
            p = [0] * (20 ** args.kTuple)
        else: None
    # print(p)
    # print(len(p))

    elements = utils.sequenceElements(seqType)
    m = list(itertools.product(elements, repeat=args.kTuple))

    terminusLength = args.terminusLength
    # print(terminusLength)

    T = []
    for x in X:
        # print(len(x))
        x = x[:terminusLength]
        # print(len(x))
        # print('-----------------')
        require = (terminusLength - args.kTuple + 1) - (len(x) - args.kTuple + 1)
        # print(require)
        t = []
        kmers = utils.kmers(x, args.kTuple)
        for kmer in kmers:
            d = {''.join(i): 0 for i in m}
            d[kmer] = 1
            t.append(list(d.values()))
        #end-for
        if require > 0:
            for i in range(require):
                t.append(p)
            #end-for
        else: None
        t = np.array(t)
        # print(t.shape)
        T.append(t)
        # print(t.shape)
    #end-for
    T = np.array(T)
    # print(T.shape)

    totalFeature = 0
    if seqType == 'DNA' or seqType == 'RNA':
        totalFeature = (4**args.kTuple)
    else:
        if seqType == 'PROT':
            totalFeature = (20**args.kTuple)
        else:
            None
    # end-if
    np.save(arr=T, file='psk-{}'.format(totalFeature))
    print('psk-{}.npy generated.'.format(totalFeature))
#end-def