#! /bin/bash

cd=~/shell_scripting/

# python script puts sequences in individual fasta files named after sample and puts them in individual_fastas
python3 make_fasta_per_seq.py
#python3 count_bp.py
num_fasta_files=$( ls ${cd}/ExampleAlignments/ | grep -c "\.fasta" )
num_sequences=$( ls ${cd}/individual_fastas/ | grep -c "\.fasta" )
num_bp=$( cat ${cd}/individual_fastas/Sample* | grep -v "^>" | wc -c )

#clear log then append to it
echo "" > log.txt
echo $num_fasta_files >> log.txt
echo $num_sequences >> log.txt
echo $num_bp >> log.txt
echo "$num_fasta_files"
echo "$num_sequences"
echo "BP $num_bp"

