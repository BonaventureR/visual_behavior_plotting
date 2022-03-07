import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def plot_max_intensity_projection(ophys_experiment_obj, ax = None):
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(ophys_experiment_obj.max_projection, cmap='gray')
    return ax


def plot_segmentation_masks(ophys_experiment_obj, ax = None):
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(ophys_experiment_obj.segmentation_mask_image)
    return ax


def plot_segmentation_mask_overlay(ophys_experiment_obj):
    if ax is None:
        fig, ax = plt.subplots()
    ax = plot_max_intensity_projection(ophys_experiment_obj)
    segmentation_mask = ophys_experiment_obj.segmentation_mask_image
    mask = np.zeros(segmentation_mask[0].shape)
    mask[:] = np.nan
    mask[segmentation_mask[0] == 1] = 1
    ax.imshow(mask, cmap='hsv', vmax=1, alpha=0.5)
    ax.axis('off')
    return ax

def plot_dff(dataObject, ax=None, cell_specimen_ids=None):
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
                dataObject.tidy_dff_traces.query('cell_specimen_id == @cell_specimen_id')['timestamps'],
                dataObject.tidy_dff_traces.query('cell_specimen_id == @cell_specimen_id')['dff']
                )
        return

    for cell_specimen_id in dataObject.tidy_dff_traces['cell_specimen_id'].unique():
      ax.plot(
          dataObject.tidy_dff_traces.query('cell_specimen_id == @cell_specimen_id')['timestamps'],
          dataObject.tidy_dff_traces.query('cell_specimen_id == @cell_specimen_id')['dff']
          )
        
    ax.set_title('deltaF/F responses')
    ax.set_ylabel('dF/F')