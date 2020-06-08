#!/bin/bash

# Dane Vassiliadis
# 20 Jun 2017

# Call pmc-utils/filterTSV.py to filter based on required fields
# Make a file containing paths to filenames first with `find`

module purge
module load pmc-utils/2.3

while read line; do
    # get basename of file
    file=`basename ${line}`
    path=`dirname $line`
    #echo $path
    #echo $file
    out="$path/${file%.*}_filtered.tsv"
    echo ${out}
    #echo filterTSV.py -s $line -o $out -c "Filter_for_unique_deleterious_consequence" -p "==" -v "Y"
    filterTSV.py -s $line -o $out -c "Filter_for_unique_deleterious_consequence" -p "==" -v "Y"
        
done < files.txt


