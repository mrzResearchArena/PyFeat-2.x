CRED = '\033[91m'
CEND = '\033[0m'

import utils
import numpy as np
import save

def generate(X, seqType, args):
    '''
    # Reference: https://www.biorxiv.org/content/10.1101/332171v2.full.pdf (Supp: Table-5)
    :param X:
    :param seqType:
    :param args:
    :return:
    '''

    # Column1 --> Acidic              : D, E
    # Column2 --> Basic               : R, H, K
    # Column3 --> Aromatic side chain : Y, F, W
    # Column4 --> Aliphatic side chain: I, L, V, A, G
    # Column5 --> Cyclic              : P
    # Column6 --> Sulfur containing   : M, C
    # Column7 --> Hydroxyl containing : S, T
    # Column8 --> Acidic amide        : Q, N

    # [1, 0, 0, 0, 0, 0, 0, 0], #Acidic
    # [0, 1, 0, 0, 0, 0, 0, 0], #Basic
    # [0, 0, 1, 0, 0, 0, 0, 0], #Aromatic side chain
    # [0, 0, 0, 1, 0, 0, 0, 0], #Aliphatic side chain
    # [0, 0, 0, 0, 1, 0, 0, 0], #Cyclic
    # [0, 0, 0, 0, 0, 1, 0, 0], #Sulfur containing
    # [0, 0, 0, 0, 0, 0, 1, 0], #Hydroxyl containing
    # [0, 0, 0, 0, 0, 0, 0, 1], #Acidic amide
    # [0, 0, 0, 0, 0, 0, 0, 0], #padding

    if seqType == 'PROT':
        d = {
            'A':[0, 0, 0, 1, 0, 0, 0, 0], #Aliphatic side chain
            'C':[0, 0, 0, 0, 0, 1, 0, 0], #Sulfur containing
            'D':[1, 0, 0, 0, 0, 0, 0, 0], #Acidic
            'E':[1, 0, 0, 0, 0, 0, 0, 0], #Acidic
            'F':[0, 0, 1, 0, 0, 0, 0, 0], #Aromatic side chain
            'G':[0, 0, 0, 1, 0, 0, 0, 0], #Aliphatic side chain
            'H':[0, 1, 0, 0, 0, 0, 0, 0], #Basic
            'I':[0, 0, 0, 1, 0, 0, 0, 0], #Aliphatic side chain
            'K':[0, 1, 0, 0, 0, 0, 0, 0], #Basic
            'L':[0, 0, 0, 1, 0, 0, 0, 0], #Aliphatic side chain
            'M':[0, 0, 0, 0, 0, 1, 0, 0], #Sulfur containing
            'N':[0, 0, 0, 0, 0, 0, 0, 1], #Acidic amide
            'P':[0, 0, 0, 0, 1, 0, 0, 0], #Cyclic
            'Q':[0, 0, 0, 0, 0, 0, 0, 1], #Acidic amide
            'R':[0, 1, 0, 0, 0, 0, 0, 0], #Basic
            'S':[0, 0, 0, 0, 0, 0, 1, 0], #Hydroxyl containing
            'T':[0, 0, 0, 0, 0, 0, 1, 0], #Hydroxyl containing
            'V':[0, 0, 0, 1, 0, 0, 0, 0], #Aliphatic side chain
            'W':[0, 0, 1, 0, 0, 0, 0, 0], #Aromatic side chain
            'Y':[0, 0, 1, 0, 0, 0, 0, 0], #Aromatic side chain
            'p':[0, 0, 0, 0, 0, 0, 0, 0], #padding
        }
    else:
        if seqType == 'DNA' or seqType == 'RNA':
            print(CRED+'Error: The \'Physicochemical Properties-P3\' feature is NOT applicable for DNA/RNA.'+CEND)
            return None
        else:
            return None
    #end-if
    X = utils.processMono(X, d, args)

    totalFeature = 0
    if seqType == 'DNA' or seqType == 'RNA': None
    else:
        if seqType == 'PROT':
            totalFeature = 8
        else:
            None
    # end-if

    save.datasetSave(X, totalFeature, 'pcpP3')
#end-def
