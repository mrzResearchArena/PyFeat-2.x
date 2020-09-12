CRED = '\033[91m'
CEND = '\033[0m'

import utils
import numpy as np
import save

def generate(X, seqType, args):
    '''
    # Reference: https://doi.org/10.1093/bioinformatics/bty451 (Supp: Table S2)
    :param X:
    :param seqType:
    :param args:
    :return:
    '''

    # Column1  --> Aromatic: {F, Y, W, H}
    # Column2  --> Negative: {D, E}
    # Column3  --> Positive: {K, H, R}
    # Column4  --> Polar: {N, Q, S, D, E, C, T, K, R, H, Y, W}
    # Column5  --> Hydrophobic: {A, G, C, T, I, V, L, K, H, F, Y, W, M}
    # Column6  --> Aliphatic: {I, V, L}
    # Column7  --> Tiny: {A, S, G, C}
    # Column8  --> Charged: {K, H, R, D, E}
    # Column9  --> Small: {P, N, D, T, C, A, G, S, V}
    # Column10 --> Proline: {P}

    if seqType == 'PROT':
        d = {
            'A': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            'R': [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            'N': [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            'D': [0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
            'C': [0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
            'Q': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            'E': [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
            'G': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            'H': [1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
            'I': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            'L': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            'K': [0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
            'M': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            'F': [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            'P': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            'S': [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            'T': [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
            'W': [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            'Y': [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            'V': [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
            'p': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        }

    else:
        if seqType == 'DNA' or seqType == 'RNA':
            print(CRED+'Error: The \'Physicochemical Properties-P1\' feature is NOT applicable for DNA/RNA.'+CEND)
            return None
        else:
            return None
    #end-if
    X = utils.processMono(X, d, args)

    totalFeature = 0
    if seqType == 'DNA' or seqType == 'RNA': None
    else:
        if seqType == 'PROT':
            totalFeature = 10
        else:
            None
    # end-if

    save.datasetSave(X, totalFeature, 'pcpP1')
#end-def
