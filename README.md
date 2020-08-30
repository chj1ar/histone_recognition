# Histone recognition

This repo mainly contains the data and code to obtain the reader-histone interaction matrix and sequence and structural similarity matrices, and update the similarity matrices, saving them to a data directory as input of PyDTI. It also includes statistics for multivalent interactions of histone marks and reader proteins.

A brief introduction to the files is as follows.

code to obtain the matrices: `reader-histone interaction matrix and sequence and structural similarity.ipynb`

code to update the similarity matrices and save for PyDTI: `update_reader_sequence_similarity_matrix.py`, `update_histone_mark_structural_similarity_matrix.py`

original histone recognition pairs: `regulator-histone relations_add Flanking Sequences and SMILES.csv`

reader-histone interaction matrix: `mat_reader_histone.csv`

histone mark sequence similarity matrix: `Similarity_histone_mark_sequence.csv`

histone mark structural similarity matrix: `Similarity_histone_mark_structure.csv`

reader domain sequence similarity matrix: Absent so far

histone mark indices: `uniquified_histone_marks.csv`

reader indices: `uniquified_readers.csv`

statistics -- distribution of # of histone marks recognized per reader: `statistics_histone_marks_per_reader.csv`

statistics -- distribution of # of readers recognizing per histone mark: `statistics_readers_per_histone_mark`

### ./similarity docs

[Requirements](similarity/README.md)
