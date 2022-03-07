import numpy as np
import matplotlib.pyplot as plt

from data_access import *


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

    speed, timestamps = get_running_speed(dataObject)

    ax.plot(timestamps, speed, color="black")
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

    licks = get_lick_timestamps(dataObject)
    ax.plot(licks, np.zeros_like(licks), marker="o", linestyle="none", color="black")


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

    rewards = get_reward_timestamps(dataObject, reward_type=reward_type)
    ax.plot(
        rewards,
        np.zeros_like(rewards),
        marker="d",
        linestyle="none",
        color="blue",
        markersize=10,
        alpha=0.25,
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

    pupil_area, timestamps = get_pupil_area(dataObject)

    ax.plot(
        timestamps, pupil_area, color="black",
    )
    ax.set_title("pupil area")
    ax.set_ylabel("pupil area\n$(pixels^2)$")


if __name__ == "__main__":
    # make_plots(experiment_dataset) - test
    pass
