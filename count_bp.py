#! /bin/python3 

import os

def count_bp(path):
    #get then read fasta files
    dirs = os.listdir(path)
    print(len(dirs))
    fasta_list = []
    for d in dirs:
        if ".fasta" in d:
            fasta_list.append(d)
    
    print(len(fasta_list))
    count = 0
    #read sequence in each fasta
    for f in fasta_list:
        fasta_path = path + f
        print(f)
        with open(fasta_path, "r") as fasta:
            lines = fasta.readlines()
            # lines[0] is sample lines[1] is the sequence
            if lines[1]:
                count += len(lines[1])
    return count


path = 'individual_fastas/'
print(count_bp(path))
