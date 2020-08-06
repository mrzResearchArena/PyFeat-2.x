CRED = '\033[91m'
CEND = '\033[0m'
# Thanks to (https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python) for the color blog!

import read
import feature

import argparse

def main(args):
    seqType = args.seqType.upper()[:4] # Sequence Type Upper
    assert args.kTuple > 0, CRED+'The \'kTuple (-k)\' value must be greater than 0.'+CEND
    assert args.gGap > 0, CRED+'The \'gGap (-g)\' value must be greater than 0.'+CEND
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

    X = read.fetchX(args.fasta, seqType)
    feature.generateFeature(X, seqType, args)
    # print(X)
#end-def

if __name__ == '__main__':
    ######################
    # Adding Arguments
    #####################
    p = argparse.ArgumentParser(description='Features Geneation Tool from DNA, RNA, and Protein/Peptide Sequences')

    p.add_argument('-seq', '--seqType', type=str, help='DNA/RNA/PROTEIN/PROT', default='PROT')
    p.add_argument('-fa', '--fasta', type=str, help='~/FASTA.txt')

    p.add_argument('-bpf', '--binaryProfileFeature', type=int, help='One Hot Encoding', default=0, choices=[0, 1]) #It is also called "identity matrix".
    p.add_argument('-blosum62', '--BLOSUM62', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pam250', '--PAM250', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-pcp', '--physicochemicalProperties', type=int, help='~', default=0, choices=[0, 1])

    p.add_argument('-blastn', '--BLASTn', type=int, help='~', default=0, choices=[0, 1])
    p.add_argument('-tt', '--transitionTransversion', type=int, help='~', default=0, choices=[0, 1])

    p.add_argument('-t', '--terminusLength', type=int, help='~', default=50)
    p.add_argument('-g', '--gGap', type=int, help='(l,k,p)-mers', default=5)
    p.add_argument('-k', '--kTuple', type=int, help='k=1 then (X), k=2 then (XX), k=3 then (XXX),', default=3)

    p.add_argument('-pseudo', '--pseudoComposition', type=int, help='Generate feature: X, XX, XXX', default=0, choices=[0, 1]) # It is also called "k-mer composition" (http://rosalind.info/glossary/k-mer-composition/).

    #(l,k,p)-mers:
    p.add_argument('-f11', '--monoMono', type=int, help='Generate feature: X_X', default=0, choices=[0, 1])
    p.add_argument('-f12', '--monoDi', type=int, help='Generate feature: X_XX', default=0, choices=[0, 1])
    p.add_argument('-f21', '--diMono', type=int, help='Generate feature: XX_X', default=0, choices=[0, 1])

    #Position Specific: kMers
    p.add_argument('-psk', '--PSkMers', type=int, help='Generate feature: position-wised k-Mers', default=0, choices=[0, 1])

    # Position Specific: gGaps
    p.add_argument('-g11', '--PSgGaps11', type=int, help='Generate feature: position-wised g-Gaps for monoMono Style', default=0, choices=[0, 1])
    p.add_argument('-g12', '--PSgGaps12', type=int, help='Generate feature: position-wised g-Gaps for monoDi Style', default=0, choices=[0, 1])
    p.add_argument('-g21', '--PSgGaps21', type=int, help='Generate feature: position-wised g-Gaps for diMono Style', default=0, choices=[0, 1])

    args = p.parse_args()

    main(args)
#end-if

