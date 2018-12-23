import logging


def analyze(flow_order, sequence):
    logging.info("analyze: commencing analysis...")

    number_of_incorporation = [0] * len(flow_order)

    flow_length = len(flow_order)
    flow_pointer = 0
    sequence_pointer = 0

    while flow_pointer < flow_length:
        count = 0
        while sequence[sequence_pointer] == flow_order[flow_pointer]:
            count += 1
            sequence_pointer += 1
        number_of_incorporation[flow_pointer] = count
        flow_pointer += 1

    logging.info("analyze: complete...")
    return number_of_incorporation
