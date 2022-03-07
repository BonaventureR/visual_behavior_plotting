
import os
import numpy as np
import pandas as pd


def average_dataframe_timeseries_values(dataframe, timeseries_column):
    return  dataframe[timeseries_column].values.mean()