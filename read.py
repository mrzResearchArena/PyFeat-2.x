CRED = '\033[91m'
CEND = '\033[0m'

def readMultipleFASTA(fileName):
    '''
    :param fileName: anyName.txt or, anyName.fa or, anyName.fasta
    :return: DNA/RNA/Protein/Peptide sequences
    '''

    with open(fileName, 'r') as file:
        v = []
        genome = ''
        for line in file:
            if line[0] != '>':
                genome += line.strip()
            else:
                v.append(genome.upper())
                genome = ''
        #end-for
        v.append(genome.upper())
        del v[0]
        return v
    #end-with
#end-def

def check(x, elements):
    '''
    :param x: a single sequence
    :param elements: charater of DNA/RNA/PROT as a set elements
    :return: ensure whether "elements" is superset or not
    '''

    x  = set(x)
    if elements >= x:
        return True
    else:
        return False
    #end-if
#end-def

def standardElements(seqType):
    '''
    :param seqType: DNA/RNA/PROT
    :return: elements of a set
    '''

    if seqType == 'DNA':
        elements = set('ACGT')
    else:
        if seqType == 'RNA':
            elements = set('ACGU')
        else:
            if seqType == 'PROT':
                elements = set('ACDEFGHIKLMNPQRSTVWY') # Except: BOJUXZ
            else:
                elements = None
            #end-if
        #end-if
    #end-if
    return elements
#end-def

def ensureBadElements(X, seqType):
    '''
    :param X:
    :param seqType:
    :return:
    '''

    elements = standardElements(seqType)
    for x in X:
        if check(x, elements) == False:
            return False
        #end-if
    #end-for
    return True
#end-def


def fetchX(fileName, seqType):
    '''
    :param fileName: anyName.txt or, anyName.fa or, anyName.fasta
    :param seqType: DNA, RNA, PROT
    :return: (Without bad elements) DNA/RNA/Protein/Peptide sequences
    '''

    X = readMultipleFASTA(fileName)

    # Check the bad/evil elements ...
    if ensureBadElements(X, seqType) == False:
        raise Exception(CRED+'Please remove the bad elements from the given \'{}\' sequences. We only accept {} as characters.'.format(seqType, sorted(standardElements(seqType)))+CEND)
    #end-if

    return X
#end-def
