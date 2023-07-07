import subprocess
import re

def remove_non_alphanumeric(strings):
    cleaned_strings = []
    pattern = re.compile(r'[^a-zA-Z0-9]')  # Pattern to match non-alphanumeric characters

    for string in strings:
        cleaned_string = pattern.sub('', string)  # Replace non-alphanumeric characters with a space
        cleaned_string = cleaned_string.replace('-', '').replace('_', '')  # Remove hyphen and underscore
        cleaned_strings.append(cleaned_string)

    return cleaned_strings


# Example gene list
# gene_list = ['StoneS', 'bFGF', 'insulin', 'transforming growth factor-', 'Fetal growth restriction§216', 'Procollagen type III amino-terminal propeptide', 'renin angiotensin aldosterone', 'membrane-type matrix metalloproteinases', 'FC>2  P value<0', 'Fu S', 'B-type natriuretic peptide C-reactive', '92-kilodalton', 'ICAM-1', 'basic fibroblast growth factor', 'ST2L', 'Angiotensin receptor .', 'PGC', 'DOI 10 7754 Clin', 'angiotensin I receptors', 'uE3', 'N-terminus-pro- B-type natriuretic peptide', 'TnI 1', 'heart-type fatty acid-binding protein', 'H-FABP heart-type fatty acid-binding protein', 'endothelial growth factor', 'GM  OMalley', 'GR']
# gene_list = ['Stone-S', 'GluCys ligase', 'phospho- lipid', 'p r e s s i o n V E G F', 'Adrenomedullin', 'cTnI])  ', 'SAHH  SAH hydrolase', 'ourresultsdocumentedthatserumlevelsofur ic acid', 'insulin', 'OM  Bas T  ', 'transforming growth factor-', 'NT proBNP', 'Felker G  Januzzi JL  ', 'termneonatesbornbetweenJuly1', 'CHD37 ± 19 40 ±', 'Transforming Growth Factor \x0c', 'alpha fetoprotein  ', 'cTnC  ', 'NT-proBNP Test', 'DOI 10 1046 j', 'KA  ', 'renin angiotensin aldosterone', 'vascular smooth muscle cells  ', 'platelet derived endo thelial growth factor', 'low-density lipoprotein  ', 'NT-proBNP serum concentra', 'platelet-derived endothelial cell growth factor thymidine phosphorylase', 'I-J  ', 'membrane-type matrix metalloproteinases', 'FC>2  P value<0', 'PriceJ', 'DOI 10 1177  ', 'WD  ', 'NT  proBNP', 'Fu S', 'NP', 'cTnI ( 4)', 'VE VCO2)', 'naturetic peptides', 'ICAM-1', 'Abe T  Tsuda E  Miyazaki A  Ishibashi-Ueda H  Yamada O  ', 'basic fibroblast growth factor', 'ST2L', 'PP', 'GluCys', 'c  31759[publishedOnlineFirst:2019 12 14]   3  Mat Bah MN  ', 'car-', 'ARF  ', 'Kader R  Plasma', 'HA  Walker NL  ', 'TGF- \x0c', 'CK-MB of 2 9  ', 'Aldosterone  ', 'Figure 1andTable 1', 'Collins M  Sharpe T  ', 'high-sensitivity troponin T  PediatrCardiol', 'Natriuretic Peptide Structure', 'NTproBNP   ', 'ARF', 'PGC', 'elastin  ', 'angiotensin I receptors', 'Ultrasound Med  ', 'uE3', 'e r v e d  i n  ', 'CoA [', 'DOI 10 1111 j 1651- 2227 2011 02258', 'hs-cTn', 'LL  Yang S  Zhang W  ', 'E  Gitter R  Mair R  ', 'Res AClin Mol Teratol 2005;73:690–2  4  ', 'heart-type fatty acid-binding protein', 'TnI 1', 'insulin like  growth factor 1', 'nitric oxide synthetase', 'angiotensin-converting enzyme', 'sRAGE Soluble receptor', 'meanl e v e l', 'H-FABP heart-type fatty acid-binding protein', 'L14 000 10 00012', 'cardiac troponin I', 'HA  Giannitsis E  ', 'e  ', 'M  Lent RW  ', 'MA  Melnyk S  ', 'troponin-T', 'time-average WSS', 'CNP', 'endothelial growth factor', 'GR', 'DOI 10 15386 cjmed-751   ', 'BuddheS DhuperS KimR', 'sys - 970', 'matrix metallopro- teinase', 'folate levelsin', 'DOI 10 1080 10408363 2019  1678565   95  ', 'Plasma Matrix Metalloproteinase-2', 'genetic factors [', 'Suthahar N  Meijers WC', 'LA Twoof3newbornswithdriedbloodspot(DBS)', 'A-type natriuretic peptide innormal', 'TIMP—tissue inhibitor of metalloproteinase  1 2  ', 'troponin hsTnT', 'troponin  Pediatr Cardiol 2016;37:1469–74', 'NT-proBNP  Growth differentiation', 'Nicotinamide Riboside', 'TnI  ', 'endothelin  ', 'Mytilin B', 'i o nb e t w e e na g ea n d BNP', 'BasedonannualreportsoftheSwedishRegistryofCongenitalHeartDisease nosubstantialnationalchangesinCHDincidenceshavebeenobserved and30-daymortalityafterpediatriccardiacsurgeryJAMA', 'Plasma Transforming Growth Factor- \x0c1', 'amino-terminal procollagen type III peptide', 'SMAD', 'B-type natriuretic  peptide', 'BNP', 'VEGF [19]  ', 'troponin I', 'Brykczy ´ nski  ', 'Paloschi  V  ', 'Komuro I', 'Thymidine  Phosphorylase', 'metalloproteinases-2', 'bFGF', 'e d  ', 'B-type natriuretic peptide', 'CRP', 'Cruz M', 'Pak V  ', 'liver-type fatty acid binding protein', 'glu  M H', 'TIMP-2', 'BD  Ivy DD', 'Vascular endothelial growth factor', 'PS', 'glutathione S-transferase', 'VEGF  ', 'M  Perez-Miguelsanz', 'Galectin-3  ', 'GS  ', 'Yacoub  M H  ', 'ARF patients', 'LeeflangM', 'Hsu D', 'hemoglobin', 'uL-FABP', 'platelet derivedgrowth factors  ', 'creatine kinase MB isoform', 'POX a28', 'Placenta 2015;36:1078-86  ', 'prohormones  i e  ', 'adenosine  ', '≤0 4', 'interleukin 1 receptor-like 1', 'vasopressin growth factors', 'elastolytic metalloproteinase', 'MTHFR  methylenetetrahydrofolate reductase;', 'hypoxia-inducible factor HIF-1', 'AP  Fontoura D  Henriques-Coelho T  Leite-Moreira AF', 'cTnI', 'S-transferase', 'Cancila  V  ', 'AFP', 'NT-', 'hypoxia-inducible factor-1    J Biol Chem', 'DOI 10 1155 2017 9247574', '3-hydroxy-3- methylglutaryl-CoA', 'Nakanishi T  ', 'JM   Rosenthal GL  Jones TK  Grifka RG', 'miRNA-320', 'MAT  ', 'VEGF', 'LK  Sanders', 'tissular MMP-2 [ 98]', 'TGF- b) TGF-', 'p o s u r eo fP', 'Placenta abruptio 28', 'TC  Korgenski K', 'GFAP', 'Troponin T', 'HospitalRyhov', 'VEGF  PD-ECGF TP acti', 'Natriuretic peptides  N  Engl J Med 1998;339:321-328  ', 'b*5-12 5', 'miR-10b', 'M  A', 'TIMP - 3  ', 'G  ', 'life-style factors', 'short-chain fatty acids', 'TroponinT Gen 5', 'BNP  B-type natriuretic peptide', 'K  Nana A', 'Troponin T Gen 5 STATassay1–19', 'SLC2A5', 'von Willebrand factor antigen', 'Page 8', 'vascular endothelial', 'cTnT', 'K  Jnovics A  Paku S', 'C–reactive protein', 'Lei4  Nana Li1 2  Ping Yu1 2', 'Pak', 'cTns  BNP', 'T  Tsuji S  ', 'Reg 1996;61:8781–97', 'M  Kuwata S  Kurishima C  ', 'GS  Davila-Roman  VG  ', 'volume-loaded right ventricle', 'ToF [8 11]  ', 'sys', 'HM', 'OM  ', 'Flt-1', 'G  Bennati E  Marrone C  ', 'K  Manabe H  ', 'Tercile 3', 'PA thrombus46 2 ± 17 1 36', 'E  Zbucka-Kretowska M  Ciborowski M  ', 'tissue angiotensin II  ', 'myoglobin  ', 'MP', 'brainnaturetic peptide', 'Mata-Greenwood E  Meyrick B  ', 'Nitric Oxide Synthase', 'Kailin JA  ', 'M  Koçer D  Aldosterone  ', 'methionine synthase reductase', 'DOI 10 1111 j 1475', 'vascular endothelium   ', 'hs-cTnT', 'veriﬁed 2', 'G  Song X  ', 'NPR-A', 'IL-2', 'Haao-null', 'N-terminal fragment prohormone B-type natriuretic peptide;cTn', 'CW  Bailey AL', 'GSSG  cys-teineylglycine', 'angiotensin II  ', 'DOI 10 1136', 'procollagen type III', 'Natriuretic peptides', 'NYHA', 'N-terminal brain natriuretic peptide plasma', 'BAV—Ikonomidis', 'BHMT', 'cTnT])', 'Neurosci 2003;26:137–46  ', 'high-density lipoprotein cholesterol', 'PA  pul monary', 'V  Th e', 'pro - collagen peptides [3]  ', 'PDGF- BB)  ', 'Sawyer DB  Colucci WS  ', 'NT -proBNP', 'pro-adrenomedullin', 'nitric oxide synthase-3 enzyme', 'proteolytic enzymes', 'Vascular matrix', 'c Ba c', 'glutamyl-cysteine (', 'sug-', 'NAD  ', 'MMP8']
file = open("manual_genes.txt", "r")
gene_list = file.readlines()
gene_list = [gene.rstrip('\n') for gene in gene_list]
# Convert the gene list to a string with comma-separated values



print(len(gene_list))

gene_list = remove_non_alphanumeric(gene_list[:])

print(gene_list)

batch_size = 500
gene_list_str = ','.join(gene_list)

# gene_batches = [gene_list[i:i+batch_size] for i in range(0, len(gene_list), batch_size)]

# Execute the R script with the gene list as a command-line argument
cmd = ['Rscript', 'genes.R', gene_list_str]
subprocess.call(cmd)
# i = 1
# for gene_batch in gene_batches:
#     # Convert the gene batch to a string with comma-separated values
#     gene_batch_str = ','.join(gene_batch)

#     # Execute the R script with the gene batch as a command-line argument
#     cmd = ['Rscript', 'genes.R', gene_batch_str]
#     subprocess.call(cmd)
#     print(i)
#     i +=1 
