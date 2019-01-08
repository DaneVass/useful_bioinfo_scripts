#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:41:32 2019

@author: vassiliadisdane
"""

usage = """ Download files from online repos using aspera client

USAGE: python generate_project_dir.py -t <type> -o/--rootdir <rootdir>

Arguments:
-o --rootdir:  Output/root directory for project file structure. This directory will become the project root

"""

#  

import sys, os, subprocess
from optparse import OptionParser

def main():
    try:
        subprocess.check_output(['ascp', '-v'])
    except:
        sys.exit("ascp binary not found, is Aspera client installed and in path?")
        
    # Define options
    parser = OptionParser()
    parser.add_option('-i','--infile', type = 'string', dest = 'infile', help = 'URL to input file')
    parser.add_option('-o','--outdir', type = 'string', dest = 'outdir', help = 'path to output directory. Use full or relative path. Current working directory used if not specified.')
    parser.add_option('-n','--filename', type = 'string', dest = 'filename', help = 'desired prefix of output file(s)')
    
    (options,args)=parser.parse_args()
    
    # determine output folder
    if options.outdir is not None:
        outdir=options.outdir
    else:
        outdir='.'
    
    # set to location of aspera ascp binary
    ASPERA="/Users/vassiliadisdane/Applications/Aspera\ CLI/bin/ascp"
    # set to location of aspera ssh key
    SSH_KEY="/Users/vassiliadisdane/Applications/Aspera\ CLI/etc/asperaweb_id_dsa.openssh"

    # determine input
    if options.infile is not None:
        infile=options.infile
    else:
        sys.exit("ERROR: no input file given")
    
    # determine filename
    if options.filename is not None:
        filename=options.filename
    else:
        filename = os.path.splitext("path_to_file")[0]

    outfile = outdir + '/' + filename
    
    cmd="%s -i %s -k1 -Tr -l100m %s %s" % (ASPERA, SSH_KEY, infile, outfile)
    print(cmd)
    subprocess.run(cmd)

    # ascp options
    # –T to disable encryption
    # –k 1 enables resume of partial transfers
    # –r recursive copy
    # –l (maximum bandwidth of request, try 100M and go up from there)

if __name__ == '__main__':
    main()