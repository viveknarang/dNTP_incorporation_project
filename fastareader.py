import logging
import constants
from Bio import SeqIO

__author__ = "Vivek Narang"
__status__ = "Development"


def read_sequence():
    logging.info("read_fasta: attempting to read the sequence...")

    record_dict = SeqIO.to_dict(SeqIO.parse(constants.DATA_DIR + constants.FASTA_FILE, "fasta"))
    logging.info("read_fasta: complete...")

    return record_dict[constants.FASTA_SEQUENCE_KEY].seq
