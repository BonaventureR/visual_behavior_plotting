import os
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from .plot_utils import *

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import data_access as data



def plot_max_intensity_projection(ophys_data_obj, ax = None):
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(ophys_data_obj.max_projection, cmap='gray')
    return ax


def plot_segmentation_masks(ophys_data_obj, ax = None):
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(ophys_data_obj.segmentation_mask_image)
    return ax


def plot_segmentation_mask_overlay(ophys_data_obj, ax = None):
    if ax is None:
        fig, ax = plt.subplots()
    ax = plot_max_intensity_projection(ophys_data_obj)
    segmentation_mask = ophys_data_obj.segmentation_mask_image
    mask = np.zeros(segmentation_mask[0].shape)
    mask[:] = np.nan
    mask[segmentation_mask[0] == 1] = 1
    ax.imshow(mask, cmap='hsv', vmax=1, alpha=0.5)
    ax.axis('off')
    return ax


def plot_dff(ophys_data_obj, cell_specimen_id = None, ax = None):
    """_summary_

    Parameters
    ----------
    ophys_data_obj : _type_
        _description_
    cell_specimen_id : str, optional
        by default "mean", options include:
            "mean": 
            cell_specimen_id (int):
    ax : _type_, optional
        _description_, by default None

    Returns
    -------
    _type_
        _description_
    """

    if ax == None:
        fig, ax = plt.subplots()
    
    dff_trace, timestamps = data.get_dff_trace_timeseries(ophys_data_obj, 
                                                          cell_specimen_id)
    ax.plot(timestamps, dff_trace, color = DATASTREAM_STYLE_DICT['dff']['color'])
    ax.set_title("Fluorescence trace")
    ax.set_xlabel("time (sec)")
    ax.set_ylabel("df/f")
    return ax


def plot_dff_heatmap(ophys_data_obj, ax = None):
    dff_traces_array = data.get_dff_trace(ophys_data_obj,
                            dff_trace_type = "all")

    if ax is None:
      fig, ax = plt.subplots()

    fig, ax = plt.subplots(figsize = (20,5))
    color_ax = ax.pcolormesh(dff_traces_array,
                    vmin = 0, vmax = np.percentile(dff_traces_array, 99),
                    cmap = 'magma')
    # label axes 
    ax.set_ylabel('cells')
    ax.set_xlabel('time (sec)')
    
    # x ticks
    ax.set_yticks(np.arange(0, len(dff_traces_array), 10));
    ax.set_xticklabels(np.arange(0, ophys_data_obj.ophys_timestamps[-1], 300));
    
    # creating a color bar
    cb = plt.colorbar(color_ax, pad=0.015, label='dF/F')