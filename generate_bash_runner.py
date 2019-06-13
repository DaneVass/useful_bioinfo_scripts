#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:30:38 2017

@author: vassiliadisdane
"""

usage = """ Generate bash script for launching cluster jobs

USAGE: python generate_bash_launcher.py -t <type> -o <outdir> -u <user> -n <name>

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
    parser.add_option('-t', '--type', type = 'string', dest = 'type', default='generic', help='Optional: selects type of bash launcher script to generate. Options are generic or snakemake, Generic by default')
    parser.add_option('-o','--outdir', type = 'string', dest = 'outdir', help = 'Optional: output base directory use full or relative path. Current working directory used if not specified.')
    parser.add_option('-u','--user',type='string',dest='user',help='Optional: user email for notifications')
    parser.add_option('-n', '--name', type='string', dest='name', help='Optional: name of output file. Default is the selected type.sbatch')
    parser.add_option('-m','--modules', type='string', dest='modules', help='Optional: collection of modules to be loaded using "module load X". Options are Generic, RNA-seq, CHIP-seq, variant-calling. Generic by default' )
    (options,args)=parser.parse_args()
    
    # determine type of script to generate
    if options.type is not None:
        filetype = options.type
        try:
            filetype == "generic" or "snakemake"
        except:
            print("No valid launcher script type given: Options are 'generic' or 'snakemake'. Defaulting to generic")
            filetype = "generic"
    else:
        filetype = "generic"
        
    # determine name of output file
    if options.name is not None:
        name=options.name
    else:
        name=options.type
    filename = name + '.sh'
    
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
        sys.exit("File exists. Exiting. Retry with different filename or move/delete current file")
    else:
        f = open(outdir+filename, 'a')
        f.write("#!/bin/bash"+"\n")
        f.write("\n")
        
      
    # generate default bash lines
    f.write("#!/bin/bash"+"\n")
    f.write("\n")
          
    if options.modules is not None:
        modules = options.modules
        try:
            modules == "none" or "rna-seq" or "chip-seq" or "variant-calling"
        except:
            print("No valid module set type given: Options are 'none', 'rna-seq', 'chip-seq' or 'variant-calling'. Defaulting to none")
            modules = "none"
    else:
        modules = "none"
    
    if modules != "none": 
        # always load default module set 
        f.write("#### Load default modules ####"+"\n")
        f.write("module purge"+"\n")
        f.write("module load pmc-utils/2.6"+"\n")
        f.write("module load pmc-scripts/2.9"+"\n")
        f.write("module load ensembl/92"+"\n")
        f.write("module load igvtools"+"\n")
        f.write("module load perl-modules/1.4"+"\n")
        f.write("module load java"+"\n")
        f.write("module load R"+"\n")
        f.write("module load samtools"+"\n")
        f.write("module load bedtools"+"\n")
        f.write("module load pipeline"+"\n")
        f.write("module load bwa"+"\n")
        f.write("module load hisat2"+"\n")
        f.write("module load bowtie2"+"\n")
        f.write("module load bowtie2"+"\n")
        f.write("module load cutadapt"+"\n")
        f.write("module load trim_galore"+"\n")
        f.write("module load deeptools/3.0.0"+"\n")
        f.write("module load fastqc"+"\n")
        f.write("module load multiqc"+"\n")

        if modules == "variant-calling":
            f.write("#### Load variant-calling modules ####"+"\n")
            f.write("module load vcftools"+"\n")
            f.write("module load bcftools"+"\n")
            f.write("module load gatk/4.0.10.0"+"\n")
            f.write("module load "+"\n")
        elif modules == "rna-seq":
            f.write("#### Load RNA-seq modules ####"+"\n")
            f.write("module load"+"\n")
            f.write("module load"+"\n")
            f.write("module load"+"\n")
        elif modules == "chip-seq":
            f.write("#### Load ChIP-seq modules ####"+"\n")
            f.write("module load macs"+"\n")
            f.write("module load "+"\n")
   
    
        f.write("\n")
        f.write("#### Run parameters ####"+"\n")
        f.write("INPUT=")
        f.write("OUTPUT=")
            
    else:
        f.write()
    print("Generating %s sbatch file as %s" % (filetype,name))
    print("%s saved in %s" % (name,outdir))
    print("Including %s as email address" % email)
    print("DONE")
        
    f.close()
    
    
if __name__ == '__main__':
    main()
    
