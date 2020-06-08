"""
From a multi fasta file and a file containing id names one per line. 
Extracts fasta records in wanted list and those not in wanted list to separate files.

usage:

python extract_fasta_records.py example.fasta wanted-list.txt

"""

from Bio import SeqIO
import sys

wanted = [line.strip() for line in open(sys.argv[2])]
seqiter = SeqIO.parse(open(sys.argv[1]), 'fasta')

# write records in wanted list 
SeqIO.write((seq for seq in seqiter if seq.id in wanted), 'wanted.fa', 'fasta')
# write records not in wanted list
SeqIO.write((seq for seq in seqiter if seq.id not in wanted), 'not-wanted.fa', 'fasta')
