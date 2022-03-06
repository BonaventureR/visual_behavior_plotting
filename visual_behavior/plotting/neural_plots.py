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
