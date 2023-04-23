#!/usr/bin/env python3

"""
Project suggestion 4: Output from a given fasta file desired sequences given in command line
    Full description: Write a python program with which you are able to filter sequences from any sequence file based on an input list of sequence IDs.
    Consider that header lines can be complex and long, because they sometimes contain more information than just their sequence IDs.
    Include an option in your program to alphabetically order your Gene IDs. When choosing this project, we can provide you with a database and input list.
Author: Serena Lam
"""

import argparse

parser = argparse.ArgumentParser(
    prog="OutputDesiredSequences",
    description="Returns (output) only the indicated (input) sequences from given fasta file",
    epilog="Incase of error, contact Serena"
)
## Three arguments are required at command line

parser.add_argument('-i', '--inputfile', required=True,
                    help='fastafile with protein/DNA/RNA sequences')
parser.add_argument('-i2', '--inputsequencefile', required=True,
                    help='file with list of desired sequence header-IDs')
parser.add_argument('-o', '--outputfile', required=True,
                    help='name of outputfile')
parser.add_argument('-s', '--sortalphabetically',
                    help='sorts gene IDS from input sequence file alphabetically')
args = parser.parse_args()


# TO READ DATABASE AND CREATE A LIBRARY WITH ONLY THE SEQUENCE ITSELF (removes unwanted data)
fasta_input_file=open(args.inputfile,"r")
gene_count = 0
for line in fasta_input_file:
    if line.startswith(">"):
        gene_count +=1
    else: continue
print(gene_count)
fasta_input_file.close()

fasta_input_file=open(args.inputfile,"r")
dictionary_of_sequences={}
identifier=fasta_input_file.readline()
for x in range(gene_count):
    boolean="TRUE"
    sequence=""
    loc_old=""
    while boolean == "TRUE":
        line=fasta_input_file.readline()
        loc_new=fasta_input_file.tell()
        if line.startswith(">"):
            boolean="FALSE"
        elif loc_new == loc_old:
            boolean="FALSE"
        elif line.endswith('*'):
            sequece=sequence+line
        else:
            boolean="FALSE"
        loc_old=fasta_input_file.tell()
    identifier=identifier.replace("\n", "")
    identifier=identifier.replace(">", "")  # removes  ">"
    dictionary_of_sequences[identifier]=sequence ## stores the id with its sequence in dictionary
    identifier=line

for i in dictionary_of_sequences:
    print(dictionary_of_sequences[i])
    
fasta_input_file.close()


# TO READ INPUT SEQUENCE FILE
fasta_input_seq_file = open(args.inputsequencefile, 'r')  # opens file for option reading 'r'
counter = 0
for v in fasta_input_seq_file:
    if v.endswith("\n"):
        counter +=1
    else: continue
print(counter)
fasta_input_file.close()
fasta_input_seq_file = open(args.inputsequencefile, 'r') 
new ={}
for x in range(counter):
    seq_name = fasta_input_seq_file.readline()
    new[seq_name] = dictionary_of_sequences[seq_name]
fasta_input_seq_file.close()


# WRITE OUTPUT FILE W/ OPTIONAL SORT ALPHABETICALLY
fasta_input_seq_file = open(args.inputsequencefile, 'r') 
file_out = open(args.outputfile, "w") #opens the file to write

if args.sortalphabetically == "yes":
    file_out.writelines('This is sorted alphabetically')
    lines = fasta_input_seq_file.readlines() # reads all lines
    sorted_ids = sorted (lines) # sorts all lines
    for seq_name in sorted_ids:
        file_out.writelines(">" + seq_name + "\n" + new[seq_name] + "\n")

else: # if not sorted alphabetically
    for seq_name in new:
        file_out.writelines(">"+seq_name+"\n"+new[seq_name]+"\n")

file_out.close()
fasta_input_seq_file.close()
