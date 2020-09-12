CRED = '\033[91m'
CEND = '\033[0m'

import utils
import numpy as np
import save

def generate(X, seqType, args):
    '''
    # Reference: https://doi.org/10.1093/bioinformatics/bty451 (Supp: Table S3)
    :param X:
    :param seqType:
    :param args:
    :return:
    '''

    ### Group-1:
    # Column1   --> Hydrophobicity: {A, C, F, G, H, I, L, M, N, P, Q, S, T, V, W, Y}
    # Column2   --> Normalized Van der Waals volume: {C, F, I, L, M, V, W}
    # Column3   --> Polarity: {A, C, D, G, P, S, T}
    # Column4   --> Polarizibility: {C, F, I, L, M, V, W, Y}
    # Column5   --> Charge: {A, D, G, S, T}
    # Column6   --> Secondary structures: {D, G, N, P, S}
    # Column7   --> Solvent accessibility: {A, C, F, G, I, L, V, W}

    ### Group-2:
    # Column8   --> Hydrophobicity: {D, E}
    # Column9   --> Normalized Van der Waals volume: {A, G, H, P, S, T, Y}
    # Column10  --> Polarity: {E, I, L, N, Q, V}
    # Column11  --> Polarizibility: {A, G, P, S, T}
    # Column12  --> Charge: {C, E, I, L, N, P, Q, V}
    # Column13  --> Secondary structures: {A, E, H, K, L, M, Q, R}
    # Column14  --> Solvent accessibility: {H, M, P, S, T, Y}

    ### Group-3:
    # Column15  --> Hydrophobicity: {K, R}
    # Column16  --> Normalized Van der Waals volume: {D, E, K, N, Q, R}
    # Column17  --> Polarity: {F, H, K, M, R, W, Y}
    # Column18  --> Polarizibility: {D, E, H, K, N, Q, R}
    # Column19  --> Charge: {F, H, K, M, R, W, Y}
    # Column20  --> Secondary structures: {C, F, I, T, V, W, Y}
    # Column21  --> Solvent accessibility: {D, E, K, N, R, Q}

    if seqType == 'PROT':
        d = {
            'A': [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            'R': [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            'N': [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            'D': [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
            'C': [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
            'Q': [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            'E': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            'G': [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            'H': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            'I': [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
            'L': [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
            'K': [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            'M': [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            'F': [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            'P': [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            'S': [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            'T': [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
            'W': [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            'Y': [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            'V': [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
            'p': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        }

    else:
        if seqType == 'DNA' or seqType == 'RNA':
            print(CRED+'Error: The \'Physicochemical Properties-P2\' feature is NOT applicable for DNA/RNA.'+CEND)
            return None
        else:
            return None
    #end-if
    X = utils.processMono(X, d, args)

    totalFeature = 0
    if seqType == 'DNA' or seqType == 'RNA': None
    else:
        if seqType == 'PROT':
            totalFeature = 21
        else:
            None
    # end-if

    save.datasetSave(X, totalFeature, 'pcpP2')
#end-def
