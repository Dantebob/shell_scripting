#! /bin/python3 

import os

#get then read fasta files
path = 'ExampleAlignments/'
fasta_list = os.listdir(path)
destination_path = 'individual_fastas/'
if not os.path.exists(destination_path):
    os.mkdir(destination_path)

samples = []
for f in fasta_list:
    fasta_path = path + f
    print(fasta_path)
    fasta = open(fasta_path, "r")
    lines = fasta.readlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith('>'):
            for s in samples:
                if lines[i] != s:
                    file_name = lines[i].strip()[1:] # remove the > char
                    file_name = file_name.replace(" ", "_")
                    with open(destination_path + file_name + ".fasta", 'w') as output_file:
                        output_file.write(lines[i])
                        i += 1
                        if i < len(lines):
                            output_file.write(lines[i])
        i += 1

    fasta.close()
