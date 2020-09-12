CRED = '\033[91m'
CEND = '\033[0m'

import utils
import numpy as np
import save

def generate(X, seqType, args):
    '''
    # Reference: https://www.cs.cmu.edu/~02710/Lectures/ScoringMatrices2015.pdf
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
            if seqType == 'PROT':
                print(CRED + 'Error: The \'BLASTn\' feature is NOT applicable for PROT.' + CEND)
                return None
            else:
                return None
    #end-if
    # print(X)
    X = utils.processMono(X, d, args)

    totalFeature = 0
    if seqType == 'DNA' or seqType == 'RNA':
        totalFeature = 4
    else:
        if seqType == 'PROT':
            None
        else:
            None
    # end-if

    save.datasetSave(X, totalFeature, 'blastn')
#end-def