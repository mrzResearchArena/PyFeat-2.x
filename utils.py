import numpy as np

# def save(X, fileName):
#     np.save(file='{}'.format(fileName), arr=X)
#     print('\'{}.ny\' file saved.'.format(fileName))
# #end-def

DNAelements = 'ACGT'
RNAelements = 'ACGU'
proteinElements = 'ACDEFGHIKLMNPQRSTVWY'

def sequenceElements(seqType):
    if seqType == 'DNA':
        elements = DNAelements
    else:
        if seqType == 'RNA':
            elements = RNAelements
        else:
            if seqType == 'PROT':
                elements = proteinElements
            else:
                elements = None
    #end-if
    return elements
#end-def


def process(Sequences, d, args):
    terminusLength = args.terminusLength

    X = []
    for sequence in Sequences:
        x = []
        for element in sequence:
            x.append(d[element]) # element = {residue, bp}
        # end-for
        v = len(sequence) - terminusLength
        if v < 0:
            v = v * (-1)
            for i in range(v):
                x.append(d['p'])
            # end-for
        else:
            x = x[0:terminusLength]

        x = np.array(x)
        # x = x.T
        X.append(x)
    #end-for
    X = np.array(X)
    return X
#end-def

def kmers(seq, k):
    v = []
    for i in range(len(seq) - k + 1):
        v.append(seq[i:i + k])
    return v
#end-for
