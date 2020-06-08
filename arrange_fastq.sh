# give script path to folder containing fastqs

indir=$1
echo $indir

cd $indir

for file in `ls *fastq.gz`; do
	samp=`basename $file`; 
	samp=${samp%%_*}; # get basename of sample and use that as folder name 
	folder=$PWD/${samp} 

	if [[ ! -d ${folder} ]]; then
		echo "mkdir ${folder}"
		mkdir ${folder} # make sample dir
	fi 

	#echo "mv ${file} ${folder}/"
	mv ${file} ${folder}/ # move file into sample folder.
	# should work for R1 and R2 files. Check basenames are the same beforehand.
done
