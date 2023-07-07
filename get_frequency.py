import re
import matplotlib.pyplot as plt

def dashed(string):
    pattern = re.compile(r'([A-Za-z]+)(\d+)')  # Pattern to match alphabetic and numeric portions
    converted_string = pattern.sub(r'\1-\2', string)
    return converted_string

def contains_alphabets_and_numbers(string):
    has_alphabets = bool(re.search('[a-zA-Z]', string))
    has_numbers = bool(re.search('[0-9]', string))
    return has_alphabets and has_numbers



pdf_file = open("all_pdfs.txt", "r")
body = pdf_file.read()
pdf_file.close()
frequencies = dict()

gene_file = open("gene_list.txt", "r")
gene_list = gene_file.readlines()
gene_list = [gene.rstrip('\n') for gene in gene_list]
gene_file.close()
# print(gene_list)

for gene in gene_list:
    if contains_alphabets_and_numbers(gene):
        frequencies[gene] = body.upper().count(gene) + body.upper().count(dashed(gene))
    else:
        frequencies[gene] = body.count(gene) + body.count(dashed(gene))

gene_file = open("gene_list.txt", "w")
gene_file.writelines([gene+"\n" for gene in gene_list if frequencies[gene] > 0])
gene_file.close()


sorted_data = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
genes, frequency = zip(*sorted_data)

# Create a bar plot
plt.bar(genes, frequency)

# Customize the plot
plt.xlabel('Gene')
plt.ylabel('Frequency')
plt.title('Gene Frequency Histogram')
plt.xticks(rotation=90)  # Rotate the x-axis labels for better visibility

# Display the plot
plt.show()



print(frequencies)