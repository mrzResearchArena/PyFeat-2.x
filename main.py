CRED = '\033[91m'
CEND = '\033[0m'
# Thanks to (https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python) for the color blog!

import read
import feature

import argparse

def main(args):
    '''
    :param args:
    :return:
    '''

    seqType = args.sequenceType.upper()[:4] # Sequence Type Upper
    assert args.kTuple > 0, CRED+'The \'--kTuple (-k)\' value must be greater than 0.'+CEND
    assert args.gGap > 0, CRED+'The \'--gGap (-g)\' value must be greater than 0.'+CEND
    assert args.terminusLength > 1, CRED+'The \'terminusLength (-t)\' value must be greater than 1.'+CEND
    assert args.terminusLength > args.gGap, CRED + 'The \'terminusLength (-t)\' value must be greater than \'gGap (-g)\'.' + CEND
    # assert args.fasta == None, CRED + 'Please insert a valid FASTA file.' + CEND

    # print(args.fasta)
    # print(type(args.fasta))

    # print(seqType)
    # try:
    #     X = read.fetchX(args.fasta, seqType)
    #     feature.generateFeature(X, seqType, args)
    # except Exception:
    #     print(CRED + 'Error: Please insert the value carefully.' + CEND)

    X = read.fetchX(args.FASTA, seqType)
    feature.generateFeature(X, seqType, args)
    # print(X)
#end-def

if __name__ == '__main__':
    ###################
    # Adding Arguments
    ###################
    p = argparse.ArgumentParser(description='Features Geneation Tool from DNA, RNA, and Protein/Peptide Sequences')
    # Hyperparameters:
    p.add_argument('-seq', '--sequenceType', type=str, help='DNA/RNA/PROTEIN/PROT', default='PROT', choices=['DNA', 'dna', 'RNA', 'rna', 'PROT', 'prot'])
    p.add_argument('-fa', '--FASTA', type=str, default='samplePROT.fasta', help='~/FASTA.txt')

    p.add_argument('-t', '--terminusLength', type=int, help='~', default=50)
    p.add_argument('-g', '--gGap', type=int, help='(l,k,p)-mers', default=5)
    p.add_argument('-k', '--kTuple', type=int, help='k=1 then (X), k=2 then (XX), k=3 then (XXX),', default=3)

    # Features:
    p.add_argument('-bpf', '--binaryProfileFeature', type=int, help='One Hot Encoding', default=0, choices=[0, 1])
    p.add_argument('-blosum62', '--BLOSUM62', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pam250', '--PAM250', type=int, help='~', default=0, choices=[0, 1])

    p.add_argument('-pcpP1', '--physicochemicalPropertiesP1', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pcpP2', '--physicochemicalPropertiesP2', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pcpP3', '--physicochemicalPropertiesP3', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pcpP4', '--physicochemicalPropertiesP4', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pcpP5', '--physicochemicalPropertiesP5', type=int, help='~', default=0, choices=[0, 1])

    p.add_argument('-pcpR1', '--physicochemicalPropertiesR1', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pcpD1', '--physicochemicalPropertiesD1', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pcpD2', '--physicochemicalPropertiesD2', type=int, help='~', default=0, choices=[0, 1])

    p.add_argument('-blastn', '--BLASTn', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-tt', '--transitionTransversion', type=int, help='~', default=0, choices=[0, 1])

    # Frequency-based: kMers
    p.add_argument('-fkmer', '--FkMers', type=int, help='Generate feature: X, XX, XXX', default=0, choices=[0, 1])

    # (l,k,p)-mers:
    p.add_argument('-fg11', '--FgGaps11', type=int, help='Generate feature: X*X', default=0, choices=[0, 1])
    p.add_argument('-fg12', '--FgGaps12', type=int, help='Generate feature: X*XX', default=0, choices=[0, 1])
    p.add_argument('-fg21', '--FgGaps21', type=int, help='Generate feature: XX*X', default=0, choices=[0, 1])

    # Position Specific: kMers
    p.add_argument('-pkmer', '--PkMers', type=int, help='Generate feature: position-wised k-Mers', default=0, choices=[0, 1])

    # Position Specific: gGaps
    p.add_argument('-pg11', '--PgGaps11', type=int, help='Generate feature: position-wised g-Gaps for monoMono Style', default=0, choices=[0, 1])
    p.add_argument('-pg12', '--PgGaps12', type=int, help='Generate feature: position-wised g-Gaps for monoDi Style', default=0, choices=[0, 1])
    p.add_argument('-pg21', '--PgGaps21', type=int, help='Generate feature: position-wised g-Gaps for diMono Style', default=0, choices=[0, 1])

    # SET arguments:
    args = p.parse_args()

    # Calling the "main( )":
    main(args)
#end-if