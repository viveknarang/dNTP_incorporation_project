from Bio import SeqIO
from constants import *


def read_fasta():
    with open(DATA_DIR + FASTA_FILE, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            return record.seq
