import numpy as np
import itertools
import utils

def generate(X, seqType, args):
    if seqType == 'DNA' or seqType == 'RNA':
        p = [0]*(4*4*4) # As we are working for g12
    else:
        if seqType == 'PROT':
            p = [0] * (20*20*20) # As we are working for g12
        else: None

    # Trail: Merged
    elements = utils.sequenceElements(seqType)
    m = list(itertools.product(elements, repeat=3))

    T = []
    for x in X:
        merged = []
        x = x[:args.terminusLength]
        for i in range(1, args.gGap + 1):
            kmers = utils.kmers(x, 3 + i)  # g12 --> 3, gGap (g11+gGap)
            t = []
            require = (args.terminusLength - (3 + 1) + 1) - (len(x) - (3 + i) + 1)
            for kmer in kmers:
                d = {''.join(_): 0 for _ in m}
                segment = kmer[0] + kmer[-2] + kmer[-1]
                d[segment] = 1
                t.append(list(d.values()))
                # break
            # break
            # print(v)
            if require > 0:
                for i in range(require):
                    t.append(p)
                # end-for
            else:
                None
            t = np.array(t)
            # print(t)
            merged.append(t)
            # print('------------------')
        # end-for
        T.append(np.concatenate((merged), axis=1))
    # end-for
    T = np.array(T)
    print(T.shape)

    totalFeature = 0
    if seqType == 'DNA' or seqType == 'RNA':
        totalFeature = (4 * args.gGap * 4 * 4 )
    else:
        if seqType == 'PROT':
            totalFeature = (20 * args.gGap * 20 * 20)
        else:
            None
    # end-if
    np.save(arr=T, file='g12-{}'.format(totalFeature))
    print('g12-{}.npy generated.'.format(totalFeature))
#end-for