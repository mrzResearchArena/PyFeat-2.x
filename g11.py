import numpy as np
import itertools
import utils

def generate(X, seqType, args):
    if seqType == 'DNA' or seqType == 'RNA':
        p = [0]*(4*4) # As we are working for g11
    else:
        if seqType == 'PROT':
            p = [0] * (20*20) # As we are working for g11
        else: None

    # Trail: Merged
    elements = utils.sequenceElements(seqType)
    m = list(itertools.product(elements, repeat=2))

    T = []
    for x in X:
        merged = []
        x = x[:args.terminusLength]
        for i in range(1, args.gGap + 1):
            kmers = utils.kmers(x, 2 + i)  # g11 --> 2, gGap (g11+gGap)
            t = []
            require = (args.terminusLength - (2 + 1) + 1) - (len(x) - (2 + i) + 1)
            for kmer in kmers:
                d = {''.join(_): 0 for _ in m}
                segment = kmer[0] + kmer[-1]
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
        totalFeature = (4 * args.gGap * 4 )
    else:
        if seqType == 'PROT':
            totalFeature = (20 * args.gGap * 20)
        else:
            None
    # end-if
    np.save(arr=T, file='g11-{}'.format(totalFeature))
    print('g11-{}.npy generated.'.format(totalFeature))
#end-for