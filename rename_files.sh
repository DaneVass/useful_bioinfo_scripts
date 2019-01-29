#!/bin/bash

# this is the output PATH
OUT_PATH="$PWD"

touch samples_renamed.txt
files=`find . -name 'ECD*.fastq.gz' -type 'f'` # change to select desired samples

# gets the base dir path, old name and generates a new name for each file based
# on criteria set out in the cut command. change cut fields to return values
# required be sure to generate file that lists the oldname and newname for
# record purposes. 

for FILE in $files
do
    #echo `basename $FILE`
    BASE=`dirname ${FILE}`
    OLD=`basename ${FILE}`
    NEW=`basename ${FILE} | cut -d_ -f 1,2,5,6`
    #echo $FILE  $BASE/$NEW >> samples_renamed.txt
    echo mv $FILE $BASE/$NEW
    #mv $FILE $BASE/$NEW
done


# to rename directories
for file in `find . -mindepth 1 -name '*' -type d`
do
    echo ${file}
    echo ./${file//_/-}
    echo mv ${file} ${file//_/-}
    #mv ${file} ${file//_/-}
done

# to rename files using find and sed
for file in `find . -mindepth 1 -name 'MBCS*.fastq.gz' -type f`
do
    #echo ${file}
    BASE=`dirname ${file}`
    #echo `basename ${file} | sed 's/_/-/1' | sed 's/_/-/1'`
    NEW=`basename ${file} | sed 's/_/-/1' | sed 's/_/-/1'`
    echo mv ${file} $BASE/$NEW
    #echo ${file} $BASE/$NEW >> samples_renamed.txt
    #mv ${file} $BASE/$NEW
done





