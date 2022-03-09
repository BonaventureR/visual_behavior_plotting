import os
import numpy as np
import pandas as pd
import util

def get_data_object_type(dataset_obj):
    return type(dataset_obj)
    
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
        reward_timestamps = rewards_df.loc[rewards_df["autorewarded"] 
            == True]["timestamps"].values
    elif reward_type == "earned":
        reward_timestamps = rewards_df.loc[rewards_df["autorewarded"] 
            == False]["timestamps"].values
    return reward_timestamps

def get_running_speed(dataset_obj):
    """_summary_

    Parameters
    ----------
    dataset_object : _type_
        _description_

    Returns
    -------
    tuple: 
        running_speed (cm/sec), timestamps (sec)
    """
    running_speed = dataset_obj.running_speed["speed"].values
    timestamps = dataset_obj.running_speed["timestamps"].values
    return running_speed, timestamps

def get_pupil_area(ophys_data_obj):
    pupil_area = ophys_data_obj.eye_tracking["pupil_area"].values
    timestamps = ophys_data_obj.eye_tracking["timestamps"].values
    return pupil_area, timestamps

def get_dff_trace(ophys_data_obj, dff_trace_type = "mean"):
    """_summary_

    Parameters
    ----------
    ophys_data_obj : _type_
        _description_
    dff_trace_type : str, optional
            "mean": will return a single mean dff timeseries
                of all the cells
            "all": will return an array with the dff timeseries
                for all cells
            cell_specimen_id (int): unified id of segmented cell
                across experiments (assigned after cell matching).
                Will return dff trace for this single
                cell_specimen_id.

        _description_, by default "mean"

    Returns
    -------
    tuple
        dff_trace, timestamps (sec)
    """
    dff_traces_df = ophys_data_obj.dff_traces.reset_index()
    
    if dff_trace_type == "mean":
        dff = get_all_cells_mean_dff(dff_traces_df)
    elif dff_trace_type == "all":
        dff =  np.vstack(dff_df['dff'].values)
    else:
        dff = get_cell_dff(dff_traces_df, dff_trace_type)
    
    timestamps = ophys_data_obj.ophys_timestamps
    return dff, timestamps

def get_all_cells_dff(dff_traces_df):
    dff_trace_array =  np.vstack(dff_traces_df['dff'].values)
    return dff_trace_array

def get_cell_dff(dff_traces_df, cell_specimen_id):
    # put a precondition check here to make sure its a csid for this experiment
    cell_dff = dff_traces_df.loc[dff_traces_df["cell_specimen_id"] 
        == cell_specimen_id, "dff"].values[0]
    return cell_dff

def get_all_cells_mean_dff(dff_traces_df):
    ave_dff = util.average_dataframe_timeseries_values(dff_traces_df, 'dff')
    return ave_dff


