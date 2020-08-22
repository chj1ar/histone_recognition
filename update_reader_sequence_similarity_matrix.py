#! /Users/cjr/miniconda3/bin/python

'''
This script aims to update the reader sequence similarity matrix after deleting a domain of a reader. Obviously, the interaction matrix also needs updating. There are 4 arguments for the user to provide.

### Minimal working example

./update_reader_sequence_similarity_matrix.py O43918 15 35 ../data/reader_sequences/ mat_reader_histone.csv updated_mat_reader_histone.csv temp_Similarity_reader_protein_sequence.csv updated_temp_Similarity_reader_protein_sequence.csv uniquified_readers.csv
'''

import numpy as np
import csv
import os
import skbio
from skbio.alignment import local_pairwise_align_protein
import sys

# global parameters
reader_to_delete = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

reader_sequence_folder = sys.argv[4]

interaction_matrix_file = sys.argv[5]
updated_interaction_matrix_file = sys.argv[6]

reader_sequence_similarity_matrix_file = sys.argv[7]
updated_reader_sequence_similarity_matrix_file = sys.argv[8]

uniquified_reader_file = sys.argv[9]



interaction_matrix = np.loadtxt(interaction_matrix_file)
reader_sequence_similarity_matrix = np.loadtxt(reader_sequence_similarity_matrix_file)
with open(uniquified_reader_file) as f:
    reader = csv.reader(f)
    retrieved_uniquified_readers = dict(reader)


###########
# Get the truncated sequence
###########

# read the fasta file to get the sequence
def get_sequence_from_fasta(reader):
    with open(os.path.join(reader_sequence_folder, reader + '.fasta')) as reader_file:
        reader_sequence = reader_file.read()
        reader_sequence = ''.join(reader_sequence.split('\n')[1:])
    return reader_sequence

reader_sequence_to_delete = get_sequence_from_fasta(reader_to_delete)


# truncate the sequence
reader_sequence_truncated = reader_sequence_to_delete[:start] + reader_sequence_to_delete[end:]


##########
# Compute the similarities and update the similarity matrix
##########

# Define the function to compute similarities
def seq_score(s1, s2):
    alignment,score,start_end_positions = local_pairwise_align_protein(s1,s2,gap_open_penalty=11,gap_extend_penalty=1)
    return score

# Compute and update
updated_reader_sequence_similarity_matrix = reader_sequence_similarity_matrix
index_to_delete = int(retrieved_uniquified_readers[reader_to_delete])
from tqdm import tqdm
for reader, index in tqdm(retrieved_uniquified_readers.items()):
    reader_sequence = get_sequence_from_fasta(reader)
    # Compute the row and column
    updated_reader_sequence_similarity_matrix[int(index_to_delete)][int(index)] = seq_score(skbio.sequence.Protein(reader_sequence_truncated), skbio.sequence.Protein(reader_sequence))
    updated_reader_sequence_similarity_matrix[int(index)][int(index_to_delete)] = seq_score(skbio.sequence.Protein(reader_sequence_truncated), skbio.sequence.Protein(reader_sequence))
updated_reader_sequence_similarity_matrix[int(index_to_delete)][int(index_to_delete)] = 1

# Save
np.savetxt(updated_reader_sequence_similarity_matrix_file, updated_reader_sequence_similarity_matrix)



##########
# Update the interaction matrix
##########

# Replace with zeros the row of the reader
updated_interaction_matrix = interaction_matrix
index_to_delete = int(retrieved_uniquified_readers[reader_to_delete])
updated_interaction_matrix[index_to_delete] = 0

# Save
np.savetxt(updated_interaction_matrix_file, updated_interaction_matrix)

