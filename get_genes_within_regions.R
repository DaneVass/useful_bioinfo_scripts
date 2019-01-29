rm(list=ls())
library("biomaRt")
#ensembl54=useMart("ENSEMBL_MART_ENSEMBL", host="may2009.archive.ensembl.org/biomart/martservice/", dataset="hsapiens_gene_ensembl")
martENSEMBL=useMart(host='grch37.ensembl.org', biomart='ENSEMBL_MART_ENSEMBL',
                    dataset='hsapiens_gene_ensembl')
chr.region = c("9:1:2200000","9:2200000:4600000","9:4600000:9000000","9:9000000:14200000","9:14200000:16600000",
               "9:16600000:18500000","9:18500000:19900000","9:19900000:25600000","9:25600000:28000000","9:28000000:33200000", "9:33200000:33474857")

entrez.ids=vector() 
entrez.count=vector()
all.results=data.frame() 

for (i in 1:length(chr.region)){
  filterlist=list(chr.region[i],"protein_coding")
  
  
  results=getBM(attributes = c("hgnc_symbol","entrezgene", "chromosome_name", "start_position", "end_position"), 
                filters = c("chromosomal_region","biotype"), 
                values = filterlist, 
                mart = martENSEMBL)
  
  results$region = chr.region[i]
  all.results=rbind(all.results,results)
  
  ids=unique(results$entrezgene) 
  ids <- ids[!is.na(ids)] 
  
  entrez.ids[i]=paste(ids, sep=",", collapse=",") 
  entrez.count[i]=unique(length(ids)) 
}

write.csv(all.results, file="all_results.csv",row.names=F)
