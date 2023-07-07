library(biomaRt)
# library(vroom)

options(timeout = 30000)

# Read the gene list from command-line arguments
args <- commandArgs(trailingOnly = TRUE)
gene_list <- unlist(strsplit(args[1], ","))

# Function to check if a gene set is valid and retrieve valid genes
get_valid_genes <- function(gene_set) {
  mart <- useMart(biomart = "ensembl", dataset = "hsapiens_gene_ensembl")
  
  # Retrieve gene IDs for the given gene symbols
  genes <- getBM(attributes = c("ensembl_gene_id", "external_gene_name"),
                 filters = "external_gene_name", values = gene_set,
                 mart = mart)
  
  # Get the valid gene symbols
  valid_genes <- unique(genes$external_gene_name)
  
  return(valid_genes)
}

valid_genes <- get_valid_genes(gene_list)

if (length(valid_genes) > 0) {
  cat("Valid gene set:\n")
  cat(paste(valid_genes, collapse = "\n"))
  cat("\n")
} else {
  cat("No valid genes found.\n")
}
