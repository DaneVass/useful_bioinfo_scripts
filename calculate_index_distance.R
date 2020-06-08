# check hamming distance of all pairwise comparisons
#

library(stringdist)
library(pheatmap)
library(ggplot2)

# list indexes
indexes <- c("TTGTTTCC",
"GGAGGAGG",
"CCTAACAA",
"AACCCGTT",
"ATTACTCG",
"TCCGGAGA",
"CGCTCATT",
"GAGATTCC",
"ATTCAGAA",
"GAATTCGT",
"CTGAAGCT",
"TAATGCGC",
"CGGCTATG",
"TCCGCGAA",
"TCTCGCGC",
"AGCGATAG",
"CGAGTAAT")

# setup matrix of indexes
indexes2 <- as.matrix(indexes)
mat <- stringdistmatrix(a = indexes2, method = "hamming")
mat <- as.matrix(mat)
mat <- as.data.frame(mat)
colnames(mat) <- indexes
rownames(mat) <- indexes

# plot hamming distance matrix
pheatmap(mat, cluster_rows = F, cluster_cols = F, display_numbers = T, fontsize = 12, main = "Hamming distances between selected indexes", show_colnames = T, show_rownames = T)
