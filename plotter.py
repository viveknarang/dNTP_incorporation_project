import logging
import numpy as np
import matplotlib.pyplot as plt
from constants import *


def plot(flow_order, no_of_incorporation, flow_order_key):
    logging.info("plot: commencing the plotting ...")
    plt.rcdefaults()
    y_pos = np.arange(len(flow_order))
    plt.bar(y_pos, no_of_incorporation, align='center', alpha=0.5)
    plt.xticks(y_pos, flow_order)
    plt.title(PLOTTER_TITLE + flow_order_key)
    plt.xlabel(PLOTTER_X_LABEL)
    plt.ylabel(PLOTTER_Y_LABEL)
    plt.show()
    logging.info("plot: complete ...")
