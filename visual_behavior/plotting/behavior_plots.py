import numpy as np
import matplotlib.pyplot as plt

from plot_utils import * 
import visual_behavior.data_access as data


def plot_behavioral_streams(dataObject):
    """ __summary_ : 
        plot behavioral streams including running, licks, rewards, and df/f streams.
    Parameters
    ----------
        dataObject : (BehaviorSesson, BehaviorOphysExperiment) 
            Objects provided via allensdk.brain_observatory module
    Returns
    ----------
        MatPlotLib: 
    """
    experiment = False
    fig, axes = None, None

    if "ophys_experiment_id" in dataObject.list_data_attributes_and_methods():
        print("experiment=True")
        fig, axes = plt.subplots(3, 1, figsize=(15, 8), sharex=True)
        experiment = True
    else:
        fig, axes = plt.subplots(2, 1, figsize=(15, 8), sharex=True)

    for ax in axes:
        plot_stimuli(dataObject, ax)

    plot_running(dataObject, axes[0])
    plot_licks(dataObject, axes[1])
    plot_rewards(dataObject, axes[1])

    axes[1].set_title("licks and rewards")
    axes[1].set_yticks([])
    axes[1].legend(["licks", "rewards"])

    if experiment:
        plot_pupil(dataObject, axes[2])

    fig.tight_layout()
    return fig, axes


def plot_running(dataObject, ax=None):
    """ __summary_ : 
        plot running speed for trial on specified dataset
    Parameters
    ----------
        dataObject : (BehaviorSesson, BehaviorOphysExperiment) 
            Objects provided via allensdk.brain_observatory module
        ax : (matplotlib.axes), optional
            Figure axes
    Returns
    ----------
    None
    """
    if ax is None:
        fig, ax = plt.subplots()

    speed, timestamps = data.get_running_speed(dataObject)

    ax.plot(timestamps, speed,
        color = DATASTREAM_STYLE_DICT['running_speed']['color'])
    ax.set_title("running speed")
    ax.set_ylabel("speed (cm/s)")


def plot_licks(dataObject, ax=None):
    """ __summary_ : 
        plot licks as black dots on specified dataset
    Parameters
    ----------
        dataObject : (BehaviorSesson, BehaviorOphysExperiment) 
            Objects provided via allensdk.brain_observatory module
        ax : (matplotlib.axes), optional
            Figure axes
    Returns
    ----------
    None
    """
    if ax is None:
        fig, ax = plt.subplots()

    licks = data.get_lick_timestamps(dataObject)
    ax.plot(licks, np.zeros_like(licks), marker="o",
            linestyle="none", 
            color = DATASTREAM_STYLE_DICT['licks']['color'])




def plot_rewards(dataObject, ax=None, reward_type="all"):
    """ __summary_ : 
        plot rewards as blue diamonds on specified axis
    Parameters
    ----------
        dataObject : (BehaviorSesson, BehaviorOphysExperiment) 
            Objects provided via allensdk.brain_observatory module
        ax : (matplotlib.axes), optional
            Figure axes
        reward_type : string
            options: 
                "all": all rewards (auto and earned)
                "auto": only free or unearned rewards 
                "earned": only earned (hit on a go trial) rewards
    Returns
    ----------
    None
    """
    if ax is None:
        fig, ax = plt.subplots()

    reward_timesestamps = data.get_reward_timestamps(dataObject,
        reward_type=reward_type)
    ax.plot(
        reward_timesestamps,
        np.zeros_like(reward_timesestamps),
        marker="d",
        linestyle = "none",
        color = DATASTREAM_STYLE_DICT['rewards']['color'],
        markersize = 10,
        alpha = 0.25,
    )


def plot_stimuli(dataObject, ax):
    """ __summary_ : 
        plot stimuli as colored bars on specified axis
    Parameters
    ----------
        dataObject : (BehaviorSesson, BehaviorOphysExperiment) 
            Objects provided via allensdk.brain_observatory module
        ax : (matplotlib.axes), optional
            Figure axes
    Returns
    ----------
    None
    """
    for _, stimulus in dataObject.stimulus_presentations.iterrows():
        ax.axvspan(stimulus["start_time"], stimulus["stop_time"], alpha=0.5)


def plot_pupil(dataObject, ax=None):
    """ __summary_ : 
        plot pupil area on specified axis
    Parameters
    ----------
        dataObject : (BehaviorSesson, BehaviorOphysExperiment) 
            Objects provided via allensdk.brain_observatory module
        ax : (matplotlib.axes), optional
            Figure axes
    Returns
    ----------
    None
    """
    if ax is None:
        fig, ax = plt.subplots()

    pupil_area, timestamps = data.get_pupil_area(dataObject)

    ax.plot(
        timestamps, pupil_area,
        color = DATASTREAM_STYLE_DICT['pupil_area']['color'],
    )
    ax.set_title(DATASTREAM_STYLE_DICT['pupil_area']['label'])
    ax.set_ylabel("pupil area\n$(pixels^2)$")


def plot_lick_raster(dataObject, exclude_aborted=False, ax=None):

    """_summary_
        plots distribution of licks across multiple trials
    Parameters
    ----------
        dataObject : (BehaviorSesson, BehaviorOphysExperiment) 
            Objects provided via allensdk.brain_observatory module
        exclude_aborted : Boolean
                Flag to exclude aborted trials, or trials where the animal licks prematurely
        ax : (matplotlib.axes), optional
            Figure axes
    Returns
    ----------
    Matplotlib fig,axis
    """
    if exclude_aborted:
        #subset data to remove aborted trials
        dataObject = dataObject[dataObject["aborted"] == False]    
    dataObject = dataObject.reset_index()

    fig,ax = plt.subplots(figsize=(5,10))
    for trial_index, trial_id in enumerate(dataObject.index.values): 
        trial_data = dataObject.loc[trial_id]
        # get times relative to change time
        lick_times = [(t - trial_data["change_time"]) for t in trial_data["lick_times"]]
        reward_time = [(t - trial_data["change_time"]) for t in [trial_data["reward_time"]]]

        # plot reward times
        if len(reward_time)>0:
               ax.plot(reward_time[0], trial_index + 0.5, 
                    '.', color='b', label='reward', markersize = 6)

        # plot lick times
        ax.vlines(lick_times, trial_index, 
                  trial_index + 1, color='k', linewidth=1)

        # put a line at the change time
        ax.vlines(0, trial_index, trial_index + 1, 
                  color=[.5, .5, .5], linewidth = 1)

    # gray bar for response window
    ax.axvspan(0.1, 0.7, facecolor = 'gray', alpha = .3, edgecolor = 'none')
    ax.grid(False)

    fig.tight_layout()
    return fig, ax

if __name__ == "__main__":
    # make_plots(experiment_dataset) - test
    pass
