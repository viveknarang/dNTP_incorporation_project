import h5py
from constants import *


def read_h5():
    return_map = {}
    data = h5py.File(DATA_DIR + H5_FILE, "r")
    for key in data.keys():
        a_list = []
        for value in data[key]:
            a_list.append(value.decode("utf-8"))
        return_map.update({key: a_list})
    return return_map
