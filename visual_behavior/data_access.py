
import numpy as np
import util


def get_stimulus_name(dataObject):
    """gets the stimulus name for a dataset object
    Parameters
    ----------
    dataObject : (BehaviorSesson, BehaviorOphysExperiment)
        Objects provided via allensdk.brain_observatory module

    Returns
    -------
    string
        the stimulus name for a given session or experiment
    """
    stimulus_name = dataObject.metadata['session_type']
    return stimulus_name


def get_lick_timestamps(dataObject):
    """gets the timestamps of licks

    Parameters
    ----------
    dataObject : (BehaviorSesson, BehaviorOphysExperiment)
        Objects provided via allensdk.brain_observatory module
    Returns
    -------
    array
        array of lick timestamps
    """
    lick_timestamps = dataObject.licks["timestamps"].values
    return lick_timestamps


def get_reward_timestamps(dataObject, reward_type="all"):
    """gets the timestamps of water rewards
    Parameters
    ----------
    dataObject : (BehaviorSesson, BehaviorOphysExperiment)
        Objects provided via allensdk.brain_observatory module
    reward_type : string
        by default "all", options:
            "all": all rewards (auto and earned)
            "auto": only free or unearned rewards
            "earned": only earned (hit on a go trial) rewards

    Returns
    -------
    array
        arry of reward timestamps
    """

    rewards_df = dataObject.rewards
    if reward_type == "all":
        reward_timestamps = rewards_df['timestamps'].values
    elif reward_type == "auto":
        reward_timestamps = rewards_df.loc[rewards_df["autorewarded"] == True]["timestamps"].values  # noqa: E501
    elif reward_type == "earned":
        reward_timestamps = rewards_df.loc[rewards_df["autorewarded"] == False]["timestamps"].values  # noqa: E501
    return reward_timestamps


def get_running_speed_timeseries(dataObject):
    """gets the mouse running speed timeseries

    Parameters
    ----------
    ophysObject : (BehaviorSesson, BehaviorOphysExperiment)
        Objects provided via allensdk.brain_observatory module

    Returns
    -------
    tuple:
        running_speed (cm/sec), timestamps (sec)
    """
    running_speed = dataObject.running_speed["speed"].values
    timestamps = dataObject.running_speed["timestamps"].values
    return running_speed, timestamps


def get_pupil_area_timeseries(ophysObject):
    """gets mouse's pupil area timeseries

    Parameters
    ----------
    ophysObject : (BehaviorOphysExperiment)
        Object provided via allensdk.brain_observatory
        module

    Returns
    -------
   tuple
        pupil area (pixels ^2), timestamps
    """
    pupil_area = ophysObject.eye_tracking["pupil_area"].values
    timestamps = ophysObject.eye_tracking["timestamps"].values
    return pupil_area, timestamps


def get_dff_trace_timeseries(ophysObject, cell_specimen_id=None):
    """ By default will return the average dff trace (mean
        of all cell dff traces) for an ophys experiment. If
        cell_specimen_id is specified then will return the
        dff trace for that single cell specimen id.

    Parameters
    ----------
    ophysObject : (BehaviorOphysExperiment)
        Object provided via allensdk.brain_observatory
        module
    cell_specimen_id : int
        unified id of segmented cell across experiments
        (assigned after cell matching). Will return dff
        trace for this single cell_specimen_id.

    Returns
    -------
    tuple
        dff_trace, timestamps (sec)
    """
    dff_traces_df = ophysObject.dff_traces.reset_index()
    if cell_specimen_id is None:
        dff = get_all_cells_mean_dff(dff_traces_df)
    else:
        dff = get_cell_dff(dff_traces_df, cell_specimen_id)
    timestamps = ophysObject.ophys_timestamps
    return dff, timestamps


def get_all_cells_dff(dff_traces_df):
    """gets the dff traces for all cells
    in a BehaviorOphysExperiment

    Parameters
    ----------
    dff_traces_df :pandas dataframe
        dff_traces attribute of a BehaviorOphysExperiment
        object.

    Returns
    -------
    array
        array of arrays with each second level array containing
        the dff timeseries values for a single cell
    """
    dff_trace_array = np.vstack(dff_traces_df['dff'].values)
    return dff_trace_array


def get_cell_dff(dff_traces_df, cell_specimen_id):
    """_summary_

    Parameters
    ----------
    dff_traces_df : pandas dataframe
        dff_traces attribute of a BehaviorOphysExperiment
        object.
    cell_specimen_id : int
       unified id of segmented cell across experiments
       (assigned after cell matching).

    Returns
    -------
    array
       dff timeseries values for the given specified cell
    """

    cell_dff = dff_traces_df.loc[dff_traces_df["cell_specimen_id"] == cell_specimen_id, "dff"].values[0]  # noqa: E501
    return cell_dff


def get_all_cells_mean_dff(dff_traces_df):
    """gets the mean dff trace for all cells
    for a given BehaviorOphysExperiment

    Parameters
    ----------
    dff_traces_df : pandas dataframe
        dff_traces attribute of a BehaviorOphysExperiment
        object.
    Returns
    -------
    array
        mean dff timeseries values for all cells
    """
    mean_dff = util.average_df_timeseries_values(dff_traces_df, 'dff')
    return mean_dff


def get_transparent_segmentation_mask(ophysObject):
    """transforms the segmentation mask image to
    make the background transparent

    Parameters
    ----------
    ophysObject : (BehaviorOphysExperiment)
        Object provided via allensdk.brain_observatory
        module
    Returns
    -------
    2D image
        1 where an ROI mask and NaN everywhere else
    """
    segmentation_mask = ophysObject.segmentation_mask_image
    transparent_mask = np.zeros(segmentation_mask[0].shape)
    transparent_mask[:] = np.nan
    transparent_mask[segmentation_mask[0] == 1] = 1
    return transparent_mask


def get_trial_type(trials_df, trial_type,
                   include_aborted):
    """filters the trials table to a specific trial type

    Parameters
    ----------
    trials_df : pandas dataframe
        _description_
    trial_type : str
        options:
            "all": all trial types (both go and catch)
            "go": go trials (change presented)
            "catch": catch trials (no change presented)
    include_aborted : bool,
        include aborted trials,
    Returns
    -------
    pandas dataframe
        filtered trials table
    """
    if trial_type == "all":
        if include_aborted is False:
            filtered_trials = trials_df.loc[trials_df["aborted"] == False]  # noqa: E501
        else:
            filtered_trials = trials_df
    else:
        filtered_trials = \
            trials_df.loc[trials_df[trial_type] == True]
    return filtered_trials


def get_response_type(trials_df, response_type,
                      include_aborted):
    """filters the trials table to a specific mouse
       behavior response type.

    Parameters
    ----------
    trials_df : pandas dataframe
        _description_
    response_type : str,
        options:
            "all": all responses
            "hit": "hit" responses, only occurs on go trial type
            "miss": "miss" responses, only occurs on
                go trial type
            "false_alarm": "false_alarm" responses,
                only occurs on catch trial type
            "correct_reject": "correct_reject" responses,
                only occurs on catch trial type
    include_aborted : bool
        include aborted trials, by default True

    Returns
    -------
    pandas dataframe
        filtered trials table
    """
    if response_type == "all":
        if include_aborted is False:
            filtered_trials = trials_df.loc[trials_df["aborted"] == False]
        else:
            filtered_trials = trials_df
    else:
        filtered_trials = trials_df.loc[trials_df[response_type] == True]
    return filtered_trials


def get_trials_data(dataObject,
                    trial_type="all", response_type="all",
                    include_aborted_trials=True):
    """gets the trials dataframe attribute and can optionally
       filter for specific trial or behavior response types.

    Parameters
    ----------
    dataObject : (BehaviorSesson, BehaviorOphysExperiment)
        Objects provided via allensdk.brain_observatory module
    trial_type : str, optional
        by default "all", options:
            "all": all trial types (both go and catch)
            "go": go trials (change presented)
            "catch": catch trials (no change presented)
    response_type : str, optional
        by default "all", options:
            "all": all responses
            "hit": "hit" responses, only occurs on go trial type
            "miss": "miss" responses, only occurs on
                go trial type
            "false_alarm": "false_alarm" responses,
                only occurs on catch trial type
            "correct_reject": "correct_reject" responses,
                only occurs on catch trial type
    include_aborted_trials : bool, optional
        whether to include aborted trials, by default True

    Returns
    -------
    pandas dataframe
        trials dataframe, optionally filtered
    """
    trials_df = dataObject.trials
    filtered_df = get_trial_type(trials_df,
                                 trial_type=trial_type,
                                 include_aborted=include_aborted_trials)
    filtered_df = get_response_type(filtered_df,
                                    response_type=response_type,
                                    include_aborted=include_aborted_trials)
    return filtered_df
