import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from plot_utils import *



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


def plot_dff(ophys_data_obj, ax=None, cell_specimen_ids=None):
    """_summary_:
        plot each cell's dff response for a given trial
    Parameters
    ----------
    dataObject : (BehaviorSesson, BehaviorOphysExperiment) 
        Objects provided via allensdk.brain_observatory module
    ax : (matplotlib.axes), optional
        Figure axes, by default None
    cell_specimen_id : List, optional
        Specific cell specimen id, by default None
    """
    if ax is None:
      fig, ax = plt.subplots()
    
    if cell_specimen_id:
        for cell_specimen_id in cell_specimen_ids:
            ax.plot(
                ophys_data_obj.tidy_dff_traces.query('cell_specimen_id == @cell_specimen_id')['timestamps'],
                ophys_data_obj.tidy_dff_traces.query('cell_specimen_id == @cell_specimen_id')['dff']
                )
        return

    for cell_specimen_id in ophys_data_obj.tidy_dff_traces['cell_specimen_id'].unique():
      ax.plot(
          ophys_data_obj.tidy_dff_traces.query('cell_specimen_id == @cell_specimen_id')['timestamps'],
          ophys_data_obj.tidy_dff_traces.query('cell_specimen_id == @cell_specimen_id')['dff']
          )
        
    ax.set_title('deltaF/F responses')
    ax.set_ylabel('dF/F')

def plot_dff_heatmap(ophys_data_obj, ax = None):
    dff_traces_array = np.vstack(ophys_data_obj.get_dff_traces["dff"].values)

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