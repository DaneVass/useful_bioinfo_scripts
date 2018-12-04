#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:30:38 2017

@author: vassiliadisdane
"""

usage = """ Generate SBATCH scriptp

USAGE: python generate_sbatch.py -t <type> -o <outdir> -u <user> -n <name>

Arguments:
-t type: Selects type of sbatch file to generate. Options are generic, variant or alignment, generic by default.
-o outdir:  Output directory
-u user: user email for notifications
-n name: name of output file. Default is the selected <type>.sbatch

"""

import os, sys
from optparse import OptionParser

def main():
    """
    Function to generate sbatch script for running cluster tasks using seqliner
    """
    # Define options
    parser = OptionParser()
    parser.add_option('-t', '--type', type = 'string', dest = 'type', default='generic', help='Optional: selects type of sbatch file to generate. Options are generic, variant or alignment, Generic by default')
    parser.add_option('-o','--outdir', type = 'string', dest = 'outdir', help = 'Optional: output base directory use full or relative path. Current working directory used if not specified.')
    parser.add_option('-u','--user',type='string',dest='user',help='Optional: user email for notifications')
    parser.add_option('-n', '--name', type='string', dest='name', help='Optional: name of output file. Default is the selected type.sbatch')
    #parser.add_option('--help', action='store_true', dest='usage', help='Print usage information and exit.')
    
    (options,args)=parser.parse_args()
    
    #if options.usage:
    #    print(usage)
    #    return
    
    # determine type of sbatch to generate
    if options.type is not None:
        filetype = options.type
        try:
            filetype == "generic" or "variant" or "alignment"
        except:
            print("please set type of sbatch desired: generic, variant or alignment. Defaulting to generic")
            filetype = "generic"
    else:
        filetype = "generic"
        
    # determine name of output file
    if options.name is not None:
        name=options.name
    else:
        name=options.type
    filename = name + '.sbatch'
    
    # determine output folder
    if options.outdir is not None:
        outdir=options.outdir
    else:
        outdir='./'
        
        
    # get user email
    if options.user is not None:
        email="--mail-user=" + options.user
    else:
        email = ""
    
    # initialise ouput sbatch file for appending
    if os.path.isfile(outdir+filename):
        print("File exists. Exiting. Retry with different filename or move/delete current file")
        return
    else:
        f = open(outdir+filename, 'a')
        f.write("#!/bin/bash"+"\n")
        f.write("\n")
        
    
    
    # generate default SBATCH lines
    f.write("#### SLURM Parameters: ####"+"\n")
    
    f.write("#SBATCH --nodes=1"+"\n")
    f.write("#SBATCH --ntasks=1"+"\n")
    f.write("#SBATCH --jobname="""+"\n")
    f.write("#SBATCH --time=2-00:00:00"+"\n")
    f.write("#SBATCH --mem=64GB"+"\n")
    f.write("#SBATCH --mail-type=ALL"+"\n")
    f.write("#SBATCH --mail-user=%s" % email+"\n")
    f.write("#SBATCH --mail-type=ALL"+"\n")
    f.write("\n")
          
    #generate default module files
    f.write("#### Load modules ####"+"\n")
    f.write("module purge"+"\n")
    f.write("module load pmc-utils"+"\n")
    f.write("module load pmc-scripts"+"\n")
    f.write("module load ensembl/78"+"\n")
    f.write("module load igvtools"+"\n")
    f.write("module load bpipe/0.9.8.6_rc2"+"\n")
    f.write("module load perl-modules"+"\n")
    f.write("module load R"+"\n")
    f.write("module load vcftools"+"\n")
    f.write("module load samtools"+"\n")
    f.write("module load java"+"\n")
    f.write("module load bedtools"+"\n")
    f.write("module load pipeline"+"\n")
    f.write("module load"+"\n")
    f.write("module load"+"\n")
    f.write("module load"+"\n")

    if filetype == "variant":
        f.write("module load"+"\n")
        f.write("module load"+"\n")
        f.write("module load"+"\n")
    elif filetype == "alignment":
        f.write("module load"+"\n")
        f.write("module load"+"\n")
        f.write("module load"+"\n")

    
    f.write("#### Seqliner run parameters ####"+"\n")
        
    f.write("seqliner= ")
    f.write("pipeline= ")
    f.write("input=")
    f.write("output=")
            
    
    print("Generating %s sbatch file as %s" % (filetype,name))
    print("%s saved in %s" % (name,outdir))
    print("Including %s as email address" % email)
    print("DONE")
        
    f.close()
    
    
if __name__ == '__main__':
    main()
    
