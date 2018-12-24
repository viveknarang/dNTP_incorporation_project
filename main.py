import logging
import fastareader
import h5reader
import analyzer
import plotter

__author__ = "Vivek Narang"
__status__ = "Development"


# main method that contains the high-level steps
def main():
    logging.info("main: begin ...")
    # reading the sequence from the fasta file
    sequence = fastareader.read_sequence()
    # reading the flow order
    flow_order_map = h5reader.read_flow_order()
    # for each flow order do the following
    for flow_order in flow_order_map:
        logging.info("For flow order: " + flow_order)
        # getting the list against the key
        flow = flow_order_map.get(flow_order)
        # passing in the flow and the sequence to get the number on incorporation for the current flow order
        number_of_incorporation = analyzer.analyze(flow, sequence)
        # plot the output with the current flow order
        plotter.plot(flow, number_of_incorporation, flow_order)
    logging.info("main: complete ...")


# TEST CASE - AS GIVEN IN THE ASSIGNMENT DESCRIPTION #
def test():
    logging.info("test: begin ...")

    # test flow order
    flow = ['T', 'A', 'T', 'G', 'T', 'C', 'B', 'A', 'G', 'T', 'G', 'C', 'A', 'T', 'G', 'T', 'C', 'A', 'T', 'G', 'T',
            'C',
            'A']
    # test sequence
    sequence = ['T', 'C', 'A', 'G', 'G', 'G', 'C', 'A', 'G', 'C', 'G', 'C', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'A', 'A',
                'G', 'A', 'T', 'A', 'C', 'C', 'A', 'A', 'G', 'G', 'A', 'G', 'G', 'C', 'A', 'T', 'G', 'G', 'C', 'C', 'T',
                'T', 'T', 'G', 'T', 'C', 'A', 'A', 'G', 'G', 'G', 'C', 'C', 'C', 'C', 'C', 'C', 'T', 'C', 'T', 'C', 'T',
                'G', 'A', 'G', 'C', 'T', 'C', 'T', 'C', 'A', 'T', 'C', 'A', 'C', 'T', 'T', 'T', 'C', 'C', 'T', 'C', 'C',
                'C', 'C', 'C']
    # test analysis
    number_of_incorporation = analyzer.analyze(flow, sequence)
    # test incorporation output
    logging.info(number_of_incorporation)
    # test output plotting
    plotter.plot(flow, number_of_incorporation, "Test")
    logging.info("test: complete ...")


# setting log level
logging.getLogger().setLevel(logging.INFO)

# Assumptions:
# [1] non empty inputs
# [2] first value in the incorporation array is not required to be non zero
# [3] each flow is a separate data set in the h5 file with a unique key example: flow_order, flow_order1 etc ...


# calling main (optionally test) function
main()
# test()
