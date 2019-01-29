#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from optparse import OptionParser

def main():
    """
    Generate sgRNA sequence for ordering IVT method
    """
    # define options
    parser = OptionParser()
    parser.add_option('-t', '--type', type = 'string', dest = 'type', default = 'normal', help = 'Type of sgRNA scaffold to generate: normal or improved')
    parser.add_option('-i', '--input', type = 'string', dest = 'sgrna', help = "sequence 5' -> 3' of the sgRNA.")
    
    # determine type of sbatch to generate
    if options.type is not None:
        type = options.type
        try:
            type == "normal" or "improved"
        except:
            print("please select correct sgRNA type: normal or improved. Defaulting to normal")
            type = "normal"
    else:
        type = "normal"

    # get input sgRNA
    if options.sgrna is not None:
        sgrna = options.sgrna
    else:
        print("please enter an sgRNA sequence")
        break

    T7 = "TAATACGACTCACTATAGG"
    normal_scaffold = "GTTTTAGAGCTAGAAATAGC"
    improved_scaffold = "gtttaagagctatgctggaaacagc"
    
    

    T7 = T7.lower()
    normal_scaffold = normal_scaffold.lower()

    print("sgRNA sequence is:")
    print(cat(T7, sgrna, normal_scaffold)


if __name__ == "__main__":
    main()
