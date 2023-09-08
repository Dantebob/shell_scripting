#! /bin/bash

cd=~/shell_scripting/

# python script puts sequences in individual fasta files named after sample and puts them in individual_fastas
python3 make_fasta_per_seq.py
bp_num=$(python3 count_bp.py 2> /dev/null)
#python3 count_bp.py
num_fasta_files=$( ls ${cd}/ExampleAlignments/ | grep -c "\.fasta" )
num_sequences=$( ls ${cd}/individual_fastas/ | grep -c "\.fasta" )
#num_bp=$( cat ${cd}/individual_fastas/Sample* | grep -v "^>" | wc -c )

#clear log then append to it
echo "" > log.txt
echo $num_fasta_files >> log.txt
echo $num_sequences >> log.txt
echo $bp_num >> log.txt

echo "Number of fasta files: $num_fasta_files"
echo "Number of sequences: $num_sequences"
echo "Number of base pairs: $bp_num"

