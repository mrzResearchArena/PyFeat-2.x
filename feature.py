import bpf
import blosum62
import pam250

import pcpP1
import pcpP2
import pcpP3
import pcpP4
import pcpP5

import pcpR1
import pcpD1
import pcpD2

import fkmer
import fg11
import fg12
import fg21

import blastn
import tt
import pkmer

import pg11
import pg12
import pg21

def generateFeature(X, seqType, args):
    '''
    :param X:
    :param seqType:
    :param args:
    :return:
    '''
    ### Binary Profile Feature Encoding for the both DNA/RNA/Protein:
    if args.binaryProfileFeature == 1:
        bpf.generate(X, seqType, args)
    # end-if

    ### Evolutionary Information based Features for protein/peptide:
    if args.BLOSUM62 == 1:
        blosum62.generate(X, seqType, args)
    # end-if

    if args.PAM250 == 1:
        pam250.generate(X, seqType, args)
    # end-if

    ### Physicochemical Properties bases Encoding for protein/peptide:
    if args.physicochemicalPropertiesP1 == 1:
        pcpP1.generate(X, seqType, args)
    #end-if

    if args.physicochemicalPropertiesP2 == 1:
        pcpP2.generate(X, seqType, args)
    #end-if

    if args.physicochemicalPropertiesP3 == 1:
        pcpP3.generate(X, seqType, args)
    #end-if

    if args.physicochemicalPropertiesP4 == 1:
        pcpP4.generate(X, seqType, args)
    #end-if

    if args.physicochemicalPropertiesP5 == 1:
        pcpP5.generate(X, seqType, args)
    #end-if

    if args.physicochemicalPropertiesR1 == 1:
        pcpR1.generate(X, seqType, args)
    #end-if

    if args.physicochemicalPropertiesD1 == 1:
        pcpD1.generate(X, seqType, args)
    #end-if

    if args.physicochemicalPropertiesD2 == 1:
        pcpD2.generate(X, seqType, args)
    #end-if

    ### Frequency-based gapped composition:
    if args.FgGaps11 == 1:
        fg11.generate(X, seqType, args)
    #end-if

    if args.FgGaps12 == 1:
        fg12.generate(X, seqType, args)
    #end-if

    if args.FgGaps21 == 1:
        fg21.generate(X, seqType, args)
    #end-if

    ### Position-based gapped composition:
    if args.PgGaps11 == 1:
        pg11.generate(X, seqType, args)
    #end-if

    if args.PgGaps12 == 1:
        pg12.generate(X, seqType, args)
    #end-if

    if args.PgGaps21 == 1:
        pg21.generate(X, seqType, args)
    #end-if


    if args.PkMers == 1:
        pkmer.generate(X, seqType, args)
    #end-if

    if args.FkMers == 1:
        fkmer.generate(X, seqType, args)
    # end-if


    ### Feature for only DNA/RNA:
    if args.BLASTn == 1:
        blastn.generate(X, seqType, args)
    # end-if

    if args.transitionTransversion == 1:
        tt.generate(X, seqType, args)
    # end-if


#end-def