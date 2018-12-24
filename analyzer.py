import logging

__author__ = "Vivek Narang"
__status__ = "Development"


# procedure to get the number of incorporation for the flow order
def analyze(flow_order, sequence):
    logging.info("analyze: commencing analysis...")
    # initializing
    number_of_incorporation = [0] * len(flow_order)
    # estimating the size of flow order and sequence
    flow_length = len(flow_order)
    sequence_length = len(sequence)
    # initializing the pointers
    flow_pointer = 0
    sequence_pointer = 0
    # while the flow pointer is within the limits
    while flow_pointer < flow_length:
        # initialize/reset count
        count = 0
        # while the sequence pointer is within the limits
        while sequence_pointer < sequence_length and sequence[sequence_pointer] == flow_order[flow_pointer]:
            # increment counters
            count += 1
            sequence_pointer += 1
        # setting the count value to the index
        number_of_incorporation[flow_pointer] = count
        # increment flow pointer
        flow_pointer += 1

    logging.info("analyze: complete...")
    # returning incorporation value
    return number_of_incorporation
