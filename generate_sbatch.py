#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:30:38 2017

@author: vassiliadisdane

Generate a Slurm SBATCH script template for use in new projects.
Contains options to customise based on desired software/analysis
"""

usage = """ Generate SBATCH script

USAGE: python generate_sbatch.py [OPTIONS]

General options:
-t type:        Selects type of sbatch file to generate. Options are generic, variant or alignment (default = generic).
-o outdir:      Output directory (default = './')
-u user:        user email for notifications (e.g. firstname.lastname@petermac.org)
-n name:        name (prefix) of output file. .sbatch will be added as a suffix (default = <type>.sbatch). 
-d time:        desired duration of job (DD-HH:MM:SS, e.g. 4 hours = 04:00:00, default = 02:00:00)
-m memory:      desired amount of RAM for job in GB (e.g. 64GB, default = 32GB)
--nodes:        desired number of nodes for job [INTEGER] (default = 1)
--ntasks:       desired number of tasks for nodes [INTEGER] (default = 2)

PeterMac specific options:
-s seqliner:    path to seqliner version to use (defaults to '/config/binaries/seqliner/dev/bin/seqliner')
-r recipes:     seqliner recipes to use. only if -s specified
-p pipeline:    seqliner pipeline to use. only if -s specified
--partition:    desired cluster partition (note at PeterMac this can be prod, prod_short, prod_med, prod_long (default = prod).

"""

import os
from optparse import OptionParser

def main():
    """
    Function to generate sbatch script for running cluster tasks on slurm and optionally using seqliner
    """
    # Define options
    parser = OptionParser()
    parser.add_option('-t', '--type', type = 'string', dest = 'type', default='generic', help='Optional: selects type of sbatch file to generate. Options are generic, minimal, variant or alignment, generic by default')
    parser.add_option('-o','--outdir', type = 'string', dest = 'outdir', help = 'Optional: output base directory use full or relative path. Current working directory used if not specified.')
    parser.add_option('-u','--user',type='string',dest='user',help='Optional: user email for notifications')
    parser.add_option('-n', '--name', type='string', dest='name', help='Optional: name of output file. Default is the selected type.sbatch')
    parser.add_option('-r', '--recipes', type='string', dest='recipes', help='Optional: comma separated list of recipes to include in the sbatch script')
    parser.add_option('-s', '--seqliner', type='string', dest='seqliner', help='Optional: full path to executable of desired seqliner version')
    parser.add_option('-p', '--pipeline', type='string', dest='pipeline', help='Optional: name of the seqliner pipeline to use')
    parser.add_option('-d', '--time', type='string', dest='time', help='Optional: Desired run time of job in format DD-HH:MM:SS. e.g. 2 days 3 hours = 02-03:00:00, default = 00-02:00:00')
    parser.add_option('-m', '--memory', type='string', dest='memory', help='Optional: Desired amount of RAM to use for job in GB. e.g. --memory 64GB, default = 32GB')
    parser.add_option('--partition', type='string', dest='partition', default='prod', help='Desired cluster partition to use. prod, prod_short, prod_med or prod_long.')
    parser.add_option('--nodes', type='string', dest='nodes', help='Optional: Desired number of cluster nodes to request.')
    parser.add_option('--ntasks', type='string', dest='ntasks', help='Optional: Desired number of threads to request.')
    
    
    
    #note -h or --help is added automatically and will report the help messages of other options above.
    (options,args)=parser.parse_args()
    
    # determine type of sbatch to generate
    if options.type is not None:
        filetype = options.type
        try:
            filetype.lower() == "generic" or "variant" or "alignment" or "minimal"
        except:
            print("please set correct sbatch type: generic, minimal, variant, or alignment. Defaulting to generic")
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
        email = options.user
    else:
        email = ""
    
    # get time
    if options.time is not None:
        time = options.time
    else:
        time = "00-02:00:00"
    
    # get memory
    if options.memory is not None:
        memory = options.memory
    else:
        memory = "32GB" 
   
    # get nodes
    if options.nodes is not None:
        nodes = options.nodes
    else:
        nodes = "1" 

    # get ntasks
    if options.ntasks is not None:
        ntasks = options.ntasks
    else:
        ntasks = "4" 

    
    # initialise ouput sbatch file for appending
    if os.path.isfile(outdir+filename):
        print("File exists. Exiting. Retry with different filename or move/delete current file")
        return
    else:
        f = open(outdir+filename, 'a')
        f.write("#!/bin/bash"+"\n")
        f.write("\n")
        
    print("Generating %s sbatch file as %s.sbatch" % (filetype,name))
      
    # generate default SBATCH lines
    f.write('##--------------------------------------------------------------------------------------##')
    f.write('## Setup environment')
    f.write('##--------------------------------------------------------------------------------------##')
    
    f.write("#### SLURM Parameters: ####"+"\n")
    f.write("#SBATCH --nodes=%s\n" % nodes)
    f.write("#SBATCH --ntasks=%s\n" % ntasks)
    f.write("#SBATCH --job-name=%s\n" % name)
    f.write("#SBATCH --time=%s\n" % time)
    f.write("#SBATCH --mem=%s\n" % memory)
    f.write("#SBATCH --mail-user=%s" % email+"\n")
    f.write("#SBATCH --mail-type=ALL"+"\n")
    f.write("#SBATCH --output='%j.out'"+"\n")
    f.write("#SBATCH --error='%j.error'"+"\n")
    f.write("\n")
          
    #generate default module files
    if filetype == "variant":
        variant(f)
    elif filetype == "alignment":
        alignment(f)
    elif filetype == "chip":
        chip(f)
    elif filetype == "minimal":
        minimal(f)
    else:
        generic(f)

    #generate custom running parameters
    f.write("\n")
    f.write("#### RUN Parameters: ####"+"\n")
    
    f.write("\n")
    f.write("INPUT=$1"+"\n")
    f.write("OUTDIR=$2"+"\n")
    f.write("\n")     
            
    # Add seqliner running options if set
    if options.seqliner is not None:
        seqliner = str(options.seqliner)
        #f.write("#### Seqliner run parameters ####"+"\n")
        f.write('seqliner="%s"' % seqliner+"\n")
        f.write("\n")
        
        if options.pipeline is not None:
            pipeline = str(options.pipeline)
            f.write('pipeline="%s"' % pipeline+"\n")
            f.write("\n")
        
        if options.recipes is not None:
            recipes = str(options.recipes)
            f.write('recipes="%s"' % recipes+"\n")
            f.write("\n")
            
        f.write("\n")
        f.write("srun -n 1 ${seqliner} run ${pipeline} -r ${recipes} -o ${OUTDIR} ${INPUT}"+"\n")
    
    #f.write("input=")
    #f.write("output=")
    
    print("Including %s as jobname" % name)   
    print("Including %s as email address" % email)
    print("Including %s as time " % time)
    print("Including %s as memory" % memory)
        
    print("%s.sbatch saved in %s" % (name,outdir))
    
    print("DONE")
        
    f.close()

def minimal(f):
    f.write("#### Load default modules ####"+"\n")
    f.write("module purge"+"\n")
    f.write("module load pmc-utils"+"\n")
    f.write("module load pmc-scripts"+"\n")
    f.write("\n")

def generic(f):
    f.write("#### Load default modules ####"+"\n")
    f.write("module purge"+"\n")
    f.write("module load pmc-utils"+"\n")
    f.write("module load pmc-scripts"+"\n")
    f.write("module load ensembl"+"\n")
    f.write("module load igvtools"+"\n")
    f.write("module load bpipe"+"\n")
    f.write("module load perl-modules"+"\n")
    f.write("module load R"+"\n")
    f.write("module load fastqc"+"\n")
    f.write("module load multiqc"+"\n")
    f.write("module load java"+"\n")
    f.write("module load bedtools"+"\n")
    f.write("module load pipeline"+"\n")
    f.write("module load cutadapt"+"\n")
    f.write("\n")

def variant(f):
    f.write("#### Load variant calling modules ####"+"\n")
    f.write("module load gatk"+"\n")
    f.write("module load picard"+"\n")
    f.write("module load mutect"+"\n")
    f.write("module load vcftools"+"\n")
    f.write("module load tabix"+"\n")
    f.write("module load strelka"+"\n")          
    f.write("\n")
    
def alignment(f):
    f.write("#### Load alignment modules ####"+"\n")
    f.write("module load bwa"+"\n")
    f.write("module load bowtie2"+"\n")
    f.write("module load hisat2"+"\n")
    f.write("module load tophat2"+"\n")
    f.write("\n")

def chip(f):
    f.write("#### Load chip-seq modules ####"+"\n")
    f.write("module load bwa"+"\n")
    f.write("module load bowtie2"+"\n")
    f.write("module load hisat2"+"\n")
    f.write("module load macs"+"\n")
    f.write("module load homer"+"\n")
    f.write("module load deeptools"+"\n")
    f.write("\n")    
    
if __name__ == '__main__':
    main()
    
