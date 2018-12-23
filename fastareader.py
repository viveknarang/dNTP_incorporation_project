import logging
from Bio import SeqIO
from constants import *


def read_fasta():
    logging.info("read_fasta: attempting to read the sequence...")
    with open(DATA_DIR + FASTA_FILE, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            logging.info("read_fasta: complete...")
            return record.seq