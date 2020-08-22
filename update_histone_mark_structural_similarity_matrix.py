#! /Users/cjr/miniconda3/bin/python

'''
This script aims to update the histone mark structural similarity matrix given a new histone mark. There are 7 arguments for the user to provide. Please find their roles in the 'global parameters' section.

### Minimal working example

./update_histone_mark_structural_similarity_matrix.py Similarity_histone_mark_structure.csv updated_Similarity_histone_mark_structure.csv uniquified_histone_marks.csv uniquified_histone_marks_add_serotonylation.csv mat_reader_histone.csv updated_mat_reader_histone.csv H3Q5ser 'C1=CC2=C(C=C1O)C(=CN2)CCN[C@@H](CCC(=O)N)C(=O)O'
'''

import sys
import numpy as np
import pandas as pd
import csv

#global parameters
histone_mark_structural_similarity_matrix_file = sys.argv[1]
updated_histone_mark_structural_similarity_matrix_file = sys.argv[2]
uniquified_histone_mark_file = sys.argv[3]
updated_uniquified_histone_mark_file = sys.argv[4]
interaction_matrix_file = sys.argv[5]
updated_interaction_matrix_file = sys.argv[6]
new_histone_mark = sys.argv[7]
new_mark_SMILES = sys.argv[8]

histone_mark_structural_similarity_matrix = np.loadtxt(histone_mark_structural_similarity_matrix_file)
interaction_matrix = np.loadtxt(interaction_matrix_file)

##########
## Update the indices of histone marks
##########

# retrieve the indices of histone marks (i.e., uniquified histone marks)
with open(uniquified_histone_mark_file) as f:
    reader = csv.reader(f)
    retrieved_uniquified_histone_marks = dict(reader)

# add the new histone mark
retrieved_uniquified_histone_marks[new_histone_mark] = str(len(retrieved_uniquified_histone_marks))
with open(updated_uniquified_histone_mark_file,'w') as f:
    w = csv.writer(f)
    w.writerows(retrieved_uniquified_histone_marks.items())

##########
## Update the interaction matrix
##########

# add a column for the new histone mark
zeros = np.zeros((interaction_matrix.shape[0], interaction_matrix.shape[1] + 1))
zeros[:, :-1] = interaction_matrix
updated_interaction_matrix = zeros

# save
np.savetxt(updated_interaction_matrix_file, updated_interaction_matrix)

##########
## Update the histone mark structural similarity matrix
##########

# map a histone mark to its SMILES
def mark2SMILES(histone_mark):
    regulator_histone = pd.read_table('../data/regulator-histone relations_add Flanking Sequences and SMILES.csv', sep='\t', index_col=0)
    for i in range(len(regulator_histone)):
        if histone_mark == regulator_histone['Substrate'][i]:
            return regulator_histone['SMILES'][i]

# retrieve the indices of histone marks (i.e., uniquified histone marks)
import csv
with open(uniquified_histone_mark_file) as f:
    reader = csv.reader(f)
    retrieved_uniquified_histone_marks = dict(reader)

# add a row and a column of zeros to the similarity matrix
zeros = np.zeros((histone_mark_structural_similarity_matrix.shape[0] + 1, histone_mark_structural_similarity_matrix.shape[1] + 1))
zeros[:-1, :-1] = histone_mark_structural_similarity_matrix
updated_histone_mark_structural_similarity_matrix = zeros

# compute the structural similarity between 2 molecules
def struct_score(SMILES1, SMILES2):
    from rdkit import Chem,DataStructs
    mol1 = Chem.MolFromSmiles(SMILES1)
    mol2 = Chem.MolFromSmiles(SMILES2)
    fp1 = Chem.RDKFingerprint(mol1)
    fp2 = Chem.RDKFingerprint(mol2)
    return DataStructs.TanimotoSimilarity(fp1,fp2)

# compute the similarity between the new histone mark and each existing histone mark, and update the similarity matrix
from tqdm import tqdm
for histone_mark, index in tqdm(retrieved_uniquified_histone_marks.items()):
    updated_histone_mark_structural_similarity_matrix[-1][int(index)] = struct_score(new_mark_SMILES, mark2SMILES(histone_mark))
    updated_histone_mark_structural_similarity_matrix[int(index)][-1] = struct_score(new_mark_SMILES, mark2SMILES(histone_mark))
updated_histone_mark_structural_similarity_matrix[-1][-1] = 1

# save
np.savetxt(updated_histone_mark_structural_similarity_matrix_file, updated_histone_mark_structural_similarity_matrix)

