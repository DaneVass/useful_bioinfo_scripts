# -*- coding: utf-8 -*-

# cat_fastq_index.py <file.fastq> <sample index>
""" 

From multiple fastq inputs, each with a separate index within the fastq header.
Return a fastq of trimmed reads with header appended to read

"""

import sys
from Bio import SeqIO

file = sys.argv[1]
index = sys.argv[2]
mir30loop = 'TAGTGAAGCCACAGATGTA'

def parse_fastq(file, index):
    fastq_file = open(file,'r')
    print(str(fastq_file))
    
    index=str(index)
    print("index is: %s") %index
    
       
    # generator function
    fastq_parser = SeqIO.parse(file, "fastq")
    
    
    SeqIO.write(my_filter(fastq_parser), output_file, "fastq")
    
    
# get only proper reads by filtering the mir30 Loop region
def filter_reads(records):
    for rec in records:
        if mir30loop in rec:
            yield rec
