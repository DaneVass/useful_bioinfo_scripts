#!/bin/bash


# set to location of aspera ascp binary
ASPERA="/Users/vassiliadisdane/Applications/Aspera\ CLI/bin/ascp"
# set to location of aspera ssh key
SSH_KEY="/Users/vassiliadisdane/Applications/Aspera\ CLI/etc/asperaweb_id_dsa.openssh"

URL=$1

OUTPUT=$2
NAME=`basename $1`
NAME=${NAME%%.*}

OUTDIR=${OUTPUT}/${NAME}

cmd="$ASPERA -i $SSH_KEY -k1 -Tr -l100m ${URL} ${OUTDIR}"

# –T to disable encryption
# –k 1 enables resume of partial transfers
# –r recursive copy
# –l (maximum bandwidth of request, try 100M and go up from there)

echo ${cmd}
${cmd}
