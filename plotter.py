import logging
import numpy as np
import matplotlib.pyplot as plt
import math
import constants

__author__ = "Vivek Narang"
__status__ = "Development"


def plot(flow_order, no_of_incorporation, flow_order_key):
    logging.info("plot: commencing the plotting ...")
    plt.rcdefaults()
    y_pos = np.arange(len(flow_order))
    plt.bar(y_pos, no_of_incorporation, align='center', alpha=0.9)
    plt.xticks(y_pos, flow_order)
    plt.xticks(y_pos[::math.ceil(len(flow_order) / constants.PLOTTER_X_LABEL_SPACING_FACTOR)])
    plt.title(constants.PLOTTER_TITLE + flow_order_key)
    plt.xlabel(constants.PLOTTER_X_LABEL)
    plt.ylabel(constants.PLOTTER_Y_LABEL)
    plt.show()
    logging.info("plot: complete ...")
