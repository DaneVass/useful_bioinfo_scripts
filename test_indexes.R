

idx <- read.table("test_indexes.txt", , head=F, as.is=T)
for(i in 1:(nrow(idx)-1)) {for(j in (i+1):nrow(idx)) {mlen <- min(nchar(idx[i,1]), nchar(idx[j,1])) 
                  if(sum(!strsplit(idx[i,1], "")[[1]][1:mlen] == strsplit(idx[j,1], "")[[1]][1:mlen]) < 3) {cat(i, j, idx[i,1], idx[j,1], sum(!strsplit(idx[i,1], "")[[1]][1:mlen] == strsplit(idx[j,1], "")[[1]][1:mlen]), "\n")}}}





