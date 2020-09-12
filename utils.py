import numpy as np

DNAelements = 'ACGT'
RNAelements = 'ACGU'
proteinElements = 'ACDEFGHIKLMNPQRSTVWY'

def sequenceElements(seqType):
    '''
    :param seqType:
    :return:
    '''

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


def processMono(Sequences, d, args):
    '''
    :param Sequences:
    :param d:
    :param args:
    :return:
    '''

    X = []
    for sequence in Sequences:
        x = []
        sequence = sequence[:args.terminusLength]
        for element in sequence:
            x.append(d[element]) # element = {residue, bp}
        # end-for
        v = len(sequence) - args.terminusLength
        if v < 0:
            v = v * (-1)
            for i in range(v):
                x.append(d['p'])
            # end-for
        else:
            x = x[0:args.terminusLength] # it doesn't work as terminus lenght applied above.

        x = np.array(x)
        # x = x.T
        X.append(x)
    #end-for
    X = np.array(X)
    return X
#end-def


def processDi(Sequences, d, args):
    '''
    :param Sequences:
    :param d:
    :param args:
    :return:
    '''

    X = []

    for sequence in Sequences:
        x = []
        sequence = sequence[:args.terminusLength]
        for diElement in kmers(sequence, 2):
            x.append(d[diElement]) # element = {residue, bp}
        # end-for
        v = len(sequence) - args.terminusLength
        if v < 0:
            v = v * (-1)
            for i in range(v):
                x.append(d['p'])
            # end-for
        else:
            x = x[0:args.terminusLength] # it doesn't work as terminus lenght applied above.

        x = np.array(x)
        # x = x.T
        X.append(x)
    #end-for
    X = np.array(X)
    return X
#end-def


def processTri(Sequences, d, args):
    '''
    :param Sequences:
    :param d:
    :param args:
    :return:
    '''

    X = []

    for sequence in Sequences:
        x = []
        sequence = sequence[:args.terminusLength]
        for diElement in kmers(sequence, 3):
            x.append(d[diElement]) # element = {residue, bp}
        # end-for
        v = len(sequence) - args.terminusLength
        if v < 0:
            v = v * (-1)
            for i in range(v):
                x.append(d['p'])
            # end-for
        else:
            x = x[0:args.terminusLength] # it doesn't work as terminus lenght applied above.

        x = np.array(x)
        # x = x.T
        X.append(x)
    #end-for
    X = np.array(X)
    return X
#end-def


def kmers(seq, k):
    '''
    :param seq:
    :param k:
    :return:
    '''

    v = []
    for i in range(len(seq) - k + 1):
        v.append(seq[i:i + k])
    return v
#end-for