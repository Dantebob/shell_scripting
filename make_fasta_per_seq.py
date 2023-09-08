#! /bin/python3 

import os

#get then read fasta files
path = 'ExampleAlignments/'
fasta_list = os.listdir(path)

for f in fasta_list:
    fasta_path = path + f
    print(fasta_path)
    fasta = open(fasta_path, "r")
    lines = fasta.readlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith('>'):
            file_name = lines[i].strip()[1:] # remove the > char
            file_name = file_name.replace(" ", "_")
            #using an f-string
            with open(path + file_name + ".txt", 'w') as output_file:
                output_file.write(lines[i])
                i += 1
                if i < len(lines):
                    output_file.write(lines[i])
        i += 1

    fasta.close()
