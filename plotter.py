import logging
import numpy as np
import matplotlib.pyplot as plt
import math
import constants

__author__ = "Vivek Narang"
__status__ = "Development"


# procedure to plot the program output
def plot(flow_order, no_of_incorporation, flow_order_key):
    logging.info("plot: commencing the plotting ...")
    # Restore the rc params from Matplotlib's internal default style.
    plt.rcdefaults()
    # preparing
    y_pos = np.arange(len(flow_order))
    # creating bars for the chart
    plt.bar(y_pos, no_of_incorporation, align='center', alpha=0.9)
    # setting xticks
    plt.xticks(y_pos, flow_order)
    # handling xticks to avoid text overlap
    plt.xticks(y_pos[::math.ceil(len(flow_order) / constants.PLOTTER_X_LABEL_SPACING_FACTOR)])
    # setting the title
    plt.title(constants.PLOTTER_TITLE + flow_order_key)
    # setting xlabel
    plt.xlabel(constants.PLOTTER_X_LABEL)
    # setting the ylabel
    plt.ylabel(constants.PLOTTER_Y_LABEL)
    # preparing and showing up the plot
    plt.show()
    logging.info("plot: complete ...")
