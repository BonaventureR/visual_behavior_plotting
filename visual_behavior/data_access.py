import os
import numpy as np
import pandas as pd
import visual_behavior.util as util

def get_stimulus_name(dataset_obj):
    """gets the stimulus name for a dataset object
    Parameters
    ----------
    dataset_object : object
        options: 
        behavior session
        ophys experiment object

    Returns
    -------
    string
        the stimulus name for a given session or experiment
    """
    stimulus_name = dataset_obj.metadata['session_type']
    return stimulus_name

def get_lick_timestamps(dataset_obj):
    """_summary_

    Parameters
    ----------
    dataset_object : _type_
        _description_

    Returns
    -------
    array
        _description_
    """
    lick_timestamps = dataset_obj.licks["timestamps"].values
    return lick_timestamps

def get_reward_timestamps(dataset_obj, reward_type):
    """_summary_

    Parameters
    ----------
    dataset_object : visual behavior dataset object from the allen SDK
        options
    reward_type : string
        options: 
            "all": all rewards (auto and earned)
            "auto": only free or unearned rewards 
            "earned": only earned (hit on a go trial) rewards

    Returns
    -------
    array
        arry of timestamps for rewards
    """

    rewards_df = dataset_obj.rewards
    if reward_type == "all":
        reward_timestamps = rewards_df['timestamps'].values
    elif reward_type == "auto":
        reward_timestamps = rewards_df.loc[rewards_df["autorewarded"] == True]["timestamps"].values
    elif reward_type == "earned":
        reward_timestamps = rewards_df.loc[rewards_df["autorewarded"] == False]["timestamps"].values
    return reward_timestamps

def get_running_speed(dataset_obj):
    """_summary_

    Parameters
    ----------
    dataset_object : _type_
        _description_

    Returns
    -------
    tuple: timestamps, running_speed
        _description_
    """
    running_speed = dataset_obj.running_speed["speed"].values
    timestamps = dataset_obj.running_speed["timestamps"].values
    return running_speed, timestamps

def get_pupil_area(ophys_experiment_dataset_obj):
    pupil_area = ophys_experiment_dataset_obj.eye_tracking["pupil_area"].values
    timestamps = ophys_experiment_dataset_obj.eye_tracking["timestamps"].values
    return pupil_area, timestamps

def get_dff_trace(ophys_experiment_dataset_obj, cell_specimen_id = None):
    """_summary_

    Parameters
    ----------
    ophys_experiment_dataset_obj : _type_
        _description_
    cell_specimen_id : int, optional
        unified id of segmented cell across experiments (assigned
        after cell matching), by default None

    Returns
    -------
    _type_
        _description_
    """
    dff_df =ophys_experiment_dataset_obj.dff_traces.reset_index()
    if cell_specimen_id == None:
        dff = util.average_dataframe_timeseries_values(dff_df, 'dff')
    else:
        dff = dff_df.loc[dff_df["cell_specimen_id"] == cell_specimen_id, "dff"].values
    timestamps = ophys_experiment_dataset_obj.ophys_timestamps
    return dff, timestamps

def get_stimulus_omission(stimulus_presentations_df):
    return  stimulus_presentations_df.loc[stimulus_presentations_df["omitted"] == True]

def get_stimulus_changes(stimulus_presentations_df):
    return stimulus_presentations_df.loc[stimulus_presentations_df["is_change"] == True]

def get_stimulus_all_image_presentation(stimulus_presentations_df):
    return stimulus_presentations_df.loc[stimulus_presentations_df["omitted"] == False]

def get_stimulus_image_presentation(stimulus_presentations_df, image_name):
    return stimulus_presentations_df.loc[stimulus_presentations_df["image_name"] == image_name]
    
def get_trial_type(trials_df, trial_type, include_aborted_trials = False):
    filtered_trials = trials_df.loc[trials_df[trial_type] == True]
    if include_aborted_trials == False:
        filtered_trials = filtered_trials.loc[filtered_trials["aborted"] == False]
    return filtered_trials 

def get_hit_trials(trials_df):
    return get_trial_type(trials_df, "hit")

def get_miss_trials(trials_df):
    return get_trial_type(trials_df, "miss")

def get_correct_reject_trials(trials_df):
    return get_trial_type(trials_df, "correct_reject")

def get_correct_reject_trials(trials_df):
    return get_trial_type(trials_df, "false_alarm")

def get_aborted_trials(trials_df):
    return get_trial_type(trials_df, "aborted", include_aborted_trials = True)

def get_go_trials(trials_df, include_aborted_trials = False):
    return get_trial_type(trials_df, "go", include_aborted_trials)

def get_catch_trials(trials_df, include_aborted_trials = False):
    return get_trial_type(trials_df, "catch", include_aborted_trials)
