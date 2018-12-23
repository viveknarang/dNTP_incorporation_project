import logging

from fastareader import read_fasta
from h5reader import read_h5
from analyzer import analyze
from plotter import plot

logging.getLogger().setLevel(logging.INFO)


def main():
    logging.info("main: begin ...")
    sequence = read_fasta()
    flow_order_map = read_h5()
    for flow_order in flow_order_map:
        logging.info("For flow order: " + flow_order)
        flow = flow_order_map.get(flow_order)
        number_of_incorporation = analyze(flow, sequence)
        plot(flow, number_of_incorporation, flow_order)
    logging.info("main: complete ...")

    # main()


flow = ['T', 'A', 'T', 'G', 'T', 'C', 'B', 'A', 'G', 'T', 'G', 'C', 'A', 'T', 'G', 'T', 'C', 'A', 'T', 'G', 'T', 'C',
        'A']
sequence = ['T', 'C', 'A', 'G', 'G', 'G', 'C', 'A', 'G', 'C', 'G', 'C', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'A', 'A',
            'G', 'A', 'T', 'A']
number_of_incorporation = analyze(flow, sequence)
plot(flow, number_of_incorporation, "Test")
