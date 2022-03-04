import os
import numpy as np
import pandas as pd


from allensdk.brain_observatory.behavior.behavior_project_cache import VisualBehaviorOphysProjectCache



def average_dataframe_timeseries_values(dataframe, timeseries_column):
    return  dataframe[timeseries_column].values.mean()

def get_stimulus_omission_timestamps(stimulus_presentations_df):
    return  stimulus_presentations_df.loc[stimulus_presentations_df["omitted"] == True]

def get_stimulus_changes_timestamps(stimulus_presentations_df):
    return stimulus_presentations_df.loc[stimulus_presentations_df["is_change"] == True]

def get_stimulus_all_image_presentation_timestamps(stimulus_presentations_df):
    return stimulus_presentations_df.loc[stimulus_presentations_df["omitted"] == False]

def get_stimulus_image_presentation_timestamps(stimulus_presentations_df, image_name):
    return stimulus_presentations_df.loc[stimulus_presentations_df["image_name"] == image_name]


def get_running_speed_timeseries():



def get_first_omission_exposure_experiment_ids(experiments_table):
    data = experiments_table.copy()
    data = data[data.session_type.isin(['OPHYS_1_images_B', 'OPHYS_1_images_A', 'OPHYS_1_images_G'])]
    data = data[data.exposure_number == 0]
    filtered_experiment_ids = data.ophys_experiment_id.unique()
    return filtered_experiment_ids


def get_first_novel_image_exposure_experiment_ids(experiments_table):
    data = experiments_table.copy()
    data = data[data.session_type.isin(['OPHYS_4_images_B', 'OPHYS_4_images_A', 'OPHYS_4_images_H'])]
    data = data[data.exposure_number == 0]
    filtered_experiment_ids = data.ophys_experiment_id.unique()
    return filtered_experiment_ids