
import os
import numpy as np
import pandas as pd


def average_dataframe_timeseries_values(dataframe, values_column):
    values_array =  np.vstack(dataframe[values_column].values)
    mean_trace = np.mean(values_array, axis = 0)
    return  mean_trace

def verify_dataset_type(dataset_obj, expected_obj_type, expected_obj_name):
    assert type(dataset_obj) == expected_obj_type, "Error: expected type {}, but\
        recieved {} type insteead.".format(expected_obj_name, type(dataset_obj))

def validate_value_in_dict_keys(input_value, dictionary, dict_name):
    assert input_value in dictionary, "Error: input value is not in {} keys.".format(dict_name)
