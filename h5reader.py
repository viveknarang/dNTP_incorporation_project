import logging
import h5py
from constants import *


def read_flow_order():
    logging.info("read_h5: attempting to read the h5 file...")
    return_map = {}
    data = h5py.File(DATA_DIR + H5_FILE, "r")
    for key in data.keys():
        a_list = []
        for value in data[key]:
            a_list.append(value.decode("utf-8"))
        return_map.update({key: a_list})
    logging.info("read_h5: complete...")
    return return_map
