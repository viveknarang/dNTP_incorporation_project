import logging
import fastareader
import h5reader
import analyzer
import plotter


__author__ = "Vivek Narang"
__status__ = "Development"


def main():
    logging.info("main: begin ...")
    sequence = fastareader.read_sequence()
    flow_order_map = h5reader.read_flow_order()
    for flow_order in flow_order_map:
        logging.info("For flow order: " + flow_order)
        flow = flow_order_map.get(flow_order)
        number_of_incorporation = analyzer.analyze(flow, sequence)
        plotter.plot(flow, number_of_incorporation, flow_order)
    logging.info("main: complete ...")


logging.getLogger().setLevel(logging.INFO)
main()

# flow = ['T', 'A', 'T', 'G', 'T', 'C', 'B', 'A', 'G', 'T', 'G', 'C', 'A', 'T', 'G', 'T', 'C', 'A', 'T', 'G', 'T', 'C',
#        'A']
# sequence = ['T', 'C', 'A', 'G', 'G', 'G', 'C', 'A', 'G', 'C', 'G', 'C', 'A', 'A', 'A', 'A', 'G', 'G', 'G', 'A', 'A',
#            'G', 'A', 'T', 'A']
# number_of_incorporation = analyze(flow, sequence)
# plot(flow, number_of_incorporation, "Test")
