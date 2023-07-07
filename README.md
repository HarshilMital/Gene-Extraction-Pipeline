# Gene_Extraction_Pipeline

This pipeline was used to extract the gene references (of the Human Genome) present in selected research papers on Congenital Heart Disease (CHD). It was part of the course project for BIO221 - Practical Bioinformatics.
It uses the pre-trained SciSpacy model "en_ner_bionlp13cg_md" to perform Named Entity Recognition (NER) on the text present in the selected PDFs to find entities of the type "GENE_OR_GENE_PRODUCT". Then the R library BiomaRt is used to extract genes present in the Human Genome.
