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
            'A': [0, 5, 5, 1],
            'C': [5, 1, 0, 5],
            'G': [1, 5, 5, 0],
            'T': [5, 0, 1, 5],
            'p': [0, 0, 0, 0],  # padding
        }
    else:
        if seqType == 'RNA':
            d = {
                'A': [0, 5, 5, 1],
                'C': [5, 1, 0, 5],
                'G': [1, 5, 5, 0],
                'U': [5, 0, 1, 5],
                'p': [0, 0, 0, 0],  # padding
            }
        else:
            if seqType == 'PROT': None
            else: None
    #end-if
    # print(X)

    try:
        X = utils.process(X, d, args)
        # print(X.shape)

        totalFeature = 0
        if seqType == 'DNA' or seqType == 'RNA':
            totalFeature = 4
        else:
            if seqType == 'PROT': None
            else:
                None
        # end-if
        np.save(arr=X, file='tt-{}'.format(totalFeature))
        print('tt-{}.npy generated.'.format(totalFeature))
    except Exception:
        print(CRED + 'Error: Please check the sequence type.' + CEND)
#end-def