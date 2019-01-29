#!/bin/bash

# a script to organise high throughput sequencing files from AGRF/PeterMac
# based on sample name
# run from the root directory where sample files are contained
# rearranges files into their own folder named according to the sample name

# this is the output PATH
OUT_PATH="$PWD"

SAMPLE_LIST=`ls ${OUT_PATH}/*fastq.gz` # returns a list of all fastq files
touch sample_names.txt 

# reorganise samples into individual directories
for FILE in $SAMPLE_LIST; do
    SAMPLE=`basename ${FILE}`
    SAMPLE=${SAMPLE%%_CB*} # change the %%_CB parameter as required
    echo ${SAMPLE} >> sample_names.txt
    if [ ! -d "${OUT_PATH}/${SAMPLE}" ]; then
        mkdir ${OUT_PATH}/${SAMPLE}
    fi
    mv ${FILE} ${OUT_PATH}/${SAMPLE}/
done


