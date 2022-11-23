# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:22:19 2022

@author: Stefan
"""
# What is important in algorithm design?
# correct > efficient > easy to implement

# Review basic data types
# strings, ints, float, list, dic, bool
# mathematical operators, bool operators
# loops

# Set CWD to current project ---------------------------------------------------
import os
os.chdir("C:/Users/Stefan/Desktop/TIG Python")


# Generate DNA with the following tool: http://www.faculty.ucr.edu/~mmaduro/random.htm
# Save it to a file called dna_example.txt
with open('dna_example.txt') as f:
    dna = f.read().replace('\n', '')
    

# DNA to RNA
# show them how to google this question
rna = dna.replace("T", "U")


# Start and Stop Codons
start = ["AUG"]
stop = ["UAG", "UAA", "UGA"]


# Find coding regions by iterating through the rna ---------------------------------------------------
# Show a basic loop example
coding_strands = []
for nucleotide_index in range(0, len(rna)-1):
    
    # Checks to see the current nucleotide is alanine, if not it will move on to the next one
    nucleotide = rna[nucleotide_index]
    if not nucleotide == "A":
        continue
    
    # Checks to see if the current codon is a start codon, if not it moves on
    codon = rna[nucleotide_index:nucleotide_index+3]
    if not codon in start:
        continue
    
    # Begins recording the coding region, only exiting if the current codon is a stop codon
    coding_strand = []
    while codon not in stop:
        start_ind = nucleotide_index
        stop_ind = nucleotide_index+3
        
        # Manually breaks the while loop if we reach the end of our code
        if stop_ind >= len(rna):
            break
        
        codon = rna[start_ind:stop_ind]
        
        coding_strand.append(codon)
        
        nucleotide_index += 3        
    coding_strands.append(coding_strand)
        

# Create a function for translating sequences ---------------------------------------------------
# Explain that functions allow for code reuse
def rna_translator(coding_strand):
    
    translation_table = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
                        "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T", 
                        "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S", 
                        "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I", 
            
                        "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H", 
                        "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P", 
                        "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R", 
                        "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", 
            
                        "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D", 
                        "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A", 
                        "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G", 
                        "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V", 
            
                        "UAA":"\n", "UAC":"Y", "UAG":"\n", "UAU":"T", 
                        "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
                        "UGA":"\n", "UGC":"C", "UGG":"W", "UGU":"C", 
                        "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}
    
    protein = []
    for codon in coding_strand:
        protein.append(translation_table[codon])
        
    protein = "".join(protein)
        
    return protein


proteins = []
for coding_strand in coding_strands:
    protein = rna_translator(coding_strand)
    proteins.append(protein)
    

with open(r'./proteins.txt', 'w') as protein_file:
    protein_file.writelines(proteins)





