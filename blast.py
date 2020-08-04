CRED = '\033[91m'
CEND = '\033[0m'

# Reference: https://www.cs.cmu.edu/~02710/Lectures/ScoringMatrices2015.pdf

import utils
import numpy as np

def generate(X, seqType, args):
    '''
    # Reference: It is a very common feature.
    :param X:
    :param seqType:
    :param args:
    :return:
    '''
    if seqType == 'DNA':
        d = {
            'A': [ 5, -4, -4, -4],
            'C': [-4, -4,  5, -4],
            'G': [-4, -4, -4,  5],
            'T': [-4,  5, -4, -4],
            'p': [ 0,  0,  0,  0],  # padding
        }
    else:
        if seqType == 'RNA':
            d = {
                'A': [ 5, -4, -4, -4],
                'C': [-4, -4,  5, -4],
                'G': [-4, -4, -4,  5],
                'U': [-4,  5, -4, -4],
                'p': [ 0,  0,  0,  0],  # padding
            }
        else:
            if seqType == 'PROT': None
            else: None
    #end-if
    # print(X)
    try:
        X = utils.process(X, d, args)

        totalFeature = 0
        if seqType == 'DNA' or seqType == 'RNA':
            totalFeature = 4
        else:
            if seqType == 'PROT':
                None
            else:
                None
        # end-if
        np.save(arr=X, file='blast-{}'.format(totalFeature))
        print('blast-{}.npy generated.'.format(totalFeature))
    except Exception:
        print(CRED+'Error: Please check the sequence type.'+CEND)
    # print(X.shape)
#end-def