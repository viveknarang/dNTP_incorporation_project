import logging
import h5py
import constants

__author__ = "Vivek Narang"
__status__ = "Development"


# function to read the flow order from the h5 file
def read_flow_order():
    logging.info("read_h5: attempting to read the h5 file...")
    return_map = {}
    # opening the h5 file in read mode
    data = h5py.File(constants.DATA_DIR + constants.H5_FILE, "r")
    # iterating over the keys
    for key in data.keys():
        a_list = []
        # preparing the list of flow order
        for value in data[key]:
            a_list.append(value.decode("utf-8"))
        # saving it in a form of key-value pare in a dictionary
        return_map.update({key: a_list})
    logging.info("read_h5: complete...")
    # returning the dictionary
    return return_map
