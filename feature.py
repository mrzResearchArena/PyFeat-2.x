import bpf
import blosum62
import pam250
import bits

import pseudo
import f11
import f12
import f21

import blast
import tv
import psk

import g11
import g12
import g21

def generateFeature(X, seqType, args):
    if args.binaryProfileFeature == 1:
        bpf.generate(X, seqType, args)
    #end-if

    if args.BLOSUM62 == 1:
        blosum62.generate(X, seqType, args)
    #end-if

    if args.PAM250 == 1:
        pam250.generate(X, seqType, args)
    #end-if

    if args.bits == 1:
        bits.generate(X, seqType, args)
    #end-if

    if args.pseudoComposition == 1:
        pseudo.generate(X, seqType, args)
    # end-if

    if args.monoMono == 1:
        f11.generate(X, seqType, args)
    #end-if

    if args.monoDi == 1:
        f12.generate(X, seqType, args)
    #end-if

    if args.diMono == 1:
        f21.generate(X, seqType, args)
    #end-if

    if args.diMono == 1:
        f21.generate(X, seqType, args)
    # end-if

    if args.BLAST == 1:
        blast.generate(X, seqType, args)
    # end-if

    if args.transversion == 1:
        tv.generate(X, seqType, args)
    # end-if

    if args.PSkMers == 1:
        psk.generate(X, seqType, args)
    # end-if

    if args.PSgGaps11 == 1:
        g11.generate(X, seqType, args)
    # end-if

    if args.PSgGaps12 == 1:
        g12.generate(X, seqType, args)
    # end-if

    if args.PSgGaps21 == 1:
        g21.generate(X, seqType, args)
    # end-if
#end-def