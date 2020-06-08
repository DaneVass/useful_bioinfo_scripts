#!/bin/bash

# Simple script to merge bam file paths by comma
# samples must be sorted correctly

## Dane Vassiliadis
## 5-6-17

dir=/bioinf_core/Proj/Validation/Downsampling/Sim-CCPv2-N/

touch temp_bams1.txt

for file in `find ${dir} -name "*merged.bam" | sort`
do
    echo ${file}
    echo ${file} >> temp_bams1.txt
done

dir2=/bioinf_core/Proj/Validation/Downsampling/Sim-CCPv2-T_fixed/

touch temp_bams2.txt

for file in `find ${dir2} -name "*merged.bam" | sort`
do
    echo ${file}
    echo ${file} >> temp_bams2.txt
done

paste -d ',' temp_bams2.txt temp_bams1.txt > matched_bams.txt

rm temp_bams*

