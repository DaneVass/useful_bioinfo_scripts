#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:41:32 2019

@author: vassiliadisdane
"""

usage = """ Download files from online repos SRA/GEO using aspera client. 

USAGE: aspera_dl.py -i/--infile <infile> -o/--outdir <outdir> -n/--filename <filename>

"""

# Import libs  
import sys, os, subprocess
from optparse import OptionParser
from contextlib import contextmanager

def main():
    try:
        subprocess.check_output(['ascp', '--version'])
    except:
        sys.exit("ascp binary not found, is Aspera client installed and in your path?")
    
    try:
        subprocess.check_output(['prefetch', '--version'])
    except:
        sys.exit("SRA toolkit: prefetch not found, is it installed and in your path?")

    # Define options
    parser = OptionParser()
    parser.add_option('-i','--infile', type = 'string', dest = 'infile', help = 'SRA/GEO file to download')
    parser.add_option('-o','--outdir', type = 'string', dest = 'outdir', help = 'path to output directory. Use full or relative path. Current working directory used if not specified.')
    #parser.add_option('-n','--filename', type = 'string', dest = 'filename', help = 'desired prefix of output file(s)')
    parser.add_option('--useprefetch', action = "store_true", help = 'Use SRA toolkit prefetch without aspera. Runs prefetch <SRA ID> in local folder.')
    parser.add_option("--ascp_opts", type = 'string', dest = 'ascp_opts', help = 'Additional options to pass to ascp. Defaults to -k 1 -T -r -l 300m -v.') 
    (options,args) = parser.parse_args()
   
    # handle using prefetch first
    if options.useprefetch:
        cmd="prefetch -v -X 30G %s" % (infile)
        sys.exit("SRA download using prefetch complete!")
    
    #----------------------------

    # determine output folder
    if options.outdir is not None:
        outdir=options.outdir
    else:
        outdir=os.getcwd()

    # get location of aspera ascp binary
    ASPERA = subprocess.check_output(['which', 'ascp'])
    
    # get location of aspera ssh key
    path1 = os.path.dirname(ASPERA)
    SSH_KEY = os.path.dirname(path1) + '/etc/asperaweb_id_dsa.openssh'
    
    print("Aspera ascp location is: %s" % (ASPERA.rstrip())) 
    print("Aspera ssh key location is: %s" % (SSH_KEY.rstrip())) 
    print("------------------------")
    print("\n")
    
    # determine input
    if options.infile is not None:
        infile=options.infile
        #print(infile[0:3]) 
        if not any(p in str(infile) for p in ("SRR", "ERR", "DRR")):
            sys.exit("ERROR: no valid input SRA run id given, must start with SRR|ERR|DRR")
        
        # [TO-DO] set this up to point to GEO submissions
        #elif infile[0:2] is not ""

        else:    
            # construct file path arg for SRA run
            print("downloading %s from SRA" % (infile))
            aspera_ftp_prefix="anonftp@ftp.ncbi.nlm.nih.gov:/sra/sra-instant/reads/ByRun/sra"
            prefix=infile[0:3]
            prefix2=infile[0:6]
            filepath = aspera_ftp_prefix+'/'+prefix+'/'+prefix2+'/'+infile+'/'+infile+'.sra'
            #print(filepath)
    else:
        sys.exit("No input file given. Exiting")


    # determine filename
    #if options.filename is not None:
    #    filename=options.filename
    #else:
    #    filename = os.path.splitext("path_to_file")[0]

    #outfile = outdir + '/' + filename

    
    # get ascp options
    if options.ascp_opts is not None:
        ascp_options = options.ascp_opts
    else:
        ascp_options = "-k 1 -T -r -l 300m -v"
        # ascp options:
        # –T to disable encryption
        # –k 1 enables resume of partial transfers
        # –r recursive copy
        # –l (maximum bandwidth of request, try 100M and go up from there)


    # setup shell commands to run
    """[path_to_ascp_binary]/ascp -i [path_to_Aspera_key]/asperaweb_id_dsa.openssh -k 1 –T -l200m anonftp@ftp.ncbi.nlm.nih.gov:/sra/sra-instant/reads/ByRun/sra/SRR/SRR304/SRR304976/SRR304976.sra [local_target_directory]"""
    
    cmd='%s -i %s %s %s %s' % (ASPERA.rstrip(), SSH_KEY.rstrip(), ascp_options.rstrip(), filepath.rstrip(), outdir)
    print(cmd)
    subprocess.call(cmd, shell=True)
    print("%s download from SRA using ascp into %s is complete!" % (infile, outdir))
    
    # run fastq-dump
    #cmd2='fastq-dump '

if __name__ == '__main__':
    main()
