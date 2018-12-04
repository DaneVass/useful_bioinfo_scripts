#!/bin/bash

# Dane Vassiliadis
# 2-8-17

#### RUN DOWNLOADS FROM INTERNET IN BACKGROUND ON CLUSTER ####

# see SRA guide https://www.ncbi.nlm.nih.gov/books/NBK242621/

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=1G
#SBATCH --time=5-00:00:00
#SBATCH --output="logs/sra-dl-%j.out"
#SBATCH --error="logs/sra-dl-%j.err"
#SBATCH --mail-user=dane.vassiliadis@petermac.org
#SBATCH --mail-type=ALL
#SBATCH --job-name="sra_dl"
#SBATCH --partition=prod

accession=$1
outdir=$PWD/$accession

#echo "downloading $accession from SRA to $outdir"

module load sratoolkit

# commands
#prefetch --list $accession
#prefetch --max-size 100G $accession

echo "dumping $accession fastqs to $outdir"
fastq-dump --split-files -O $outdir --gzip -v $accession

#echo "dumping $accession SAMs to $outdir"
#sam-dump "$outdir/$accession.sra" -O $outdir -v
