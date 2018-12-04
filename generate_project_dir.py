#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:30:38 2017

@author: vassiliadisdane
"""

usage = """ Generate new project directory structure

USAGE: python generate_project_dir.py -t <type> -o/--rootdir <rootdir>

Arguments:
-o --rootdir:  Output/root directory for project file structure. This directory will become the project root

Project file structure:

./rootdir
  | project-notes.Rmd
  | data/
      | raw/
      | processed/
  | scripts/
  | docs/
  | plots/
  
"""

import os, sys
from optparse import OptionParser

def main():
    """
    Function to generate folder structure for new projects
    """
    # Define options
    parser = OptionParser()
    parser.add_option('-o','--outdir', type = 'string', dest = 'outdir', help = 'Optional: Output/root directory for project file structure. Use full or relative path. Current working directory used if not specified.')
    
    (options,args)=parser.parse_args()
    
    # determine output folder
    if options.outdir is not None:
        outdir=options.outdir
    else:
        outdir='./'
    
    # initialise ouput sbatch file for appending
    if os.path.isfile(outdir + "project-notes.Rmd"):
        print("File exists. Exiting. Retry with different filename or move/delete current file")
        return
    else:
        f = open(outdir + "project-notes.Rmd", 'a')
        f.write('---' + "\n")
        f.write('title: "Project Title"' + "\n")
        f.write("output: html_notebook" + "\n")
        f.write("---" + "\n")
        f.write("\n")
        f.write("\n")
        f.close()
        
    # Generate directory structure
    if not os.path.exists(outdir + "data/"):
        os.makedirs(outdir + "data/")
    
    if not os.path.exists(outdir + "data/raw/"):
        os.makedirs(outdir + "data/raw/")
    
    if not os.path.exists(outdir + "data/processed/"):
        os.makedirs(outdir + "data/processed/")
    
    if not os.path.exists(outdir + "plots/"):
        os.makedirs(outdir + "plots/")
    
    if not os.path.exists(outdir + "scripts/"):
        os.makedirs(outdir + "scripts/")
    
    if not os.path.exists(outdir + "docs/"):
        os.makedirs(outdir + "docs/")
    
    # print parameters to terminal 
    print("Generating project directory in %s" % (outdir))
    print("DONE")
        
if __name__ == '__main__':
    main()
    
