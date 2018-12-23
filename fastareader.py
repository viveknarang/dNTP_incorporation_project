import logging
from Bio import SeqIO
from constants import *


def read_sequence():
    logging.info("read_fasta: attempting to read the sequence...")

    record_dict = SeqIO.to_dict(SeqIO.parse(DATA_DIR + FASTA_FILE, "fasta"))
    logging.info("read_fasta: complete...")

    return record_dict[FASTA_SEQUENCE_KEY].seq
