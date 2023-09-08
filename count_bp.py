#! /bin/python3 

import os

def count_bp(path):
    #get then read fasta files
    dirs = os.listdir(path)
    fasta_list = []
    for d in dirs:
        if ".fasta" in d:
            fasta_list.append(d)
    
    count = 0
    #read sequence in each fasta
    for f in fasta_list:
        fasta_path = path + f
        with open(fasta_path, "r") as fasta:
            lines = fasta.readlines()
            # lines[0] is sample lines[1] is the sequence
            if len(lines) > 1:
                count += len(lines[1])
    return count


path = 'individual_fastas/'
print(count_bp(path))
