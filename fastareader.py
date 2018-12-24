import logging
import constants
from Bio import SeqIO

__author__ = "Vivek Narang"
__status__ = "Development"


# procedure to read the sequence from the fasta file
def read_sequence():
    logging.info("read_fasta: attempting to read the sequence...")
    # parsing the fasta file and loading the record in a dictionary
    record_dict = SeqIO.to_dict(SeqIO.parse(constants.DATA_DIR + constants.FASTA_FILE, "fasta"))
    logging.info("read_fasta: complete...")
    # returning the sequence using the FASTA_SEQUENCE_KEY value
    return record_dict[constants.FASTA_SEQUENCE_KEY].seq
