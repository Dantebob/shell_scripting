#! /bin/python3

f = open("ExampleAlignments/ExampleAlignment1.fasta", 'r') 
lines = f.readlines()

file_name = lines[0]
print(file_name)
file_name = file_name.strip()
print(file_name)
new_file = open(file_name,'w')
new_file.close()

