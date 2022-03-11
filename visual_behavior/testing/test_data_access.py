import allensdk
from allensdk.brain_observatory.behavior.behavior_project_cache import VisualBehaviorOphysProjectCache
import matplotlib.pyplot as plt
import numpy as np
import path as Path
import pytest

from plotting.neural_plots import *

@pytest.fixture(autouse=True)
def set_variables():
    data_storage_directory = Path("/./visual_behavior_ophys_cache_dir")
    cache = VisualBehaviorOphysProjectCache.from_s3_cache(cache_dir=data_storage_directory)
    pytest.experiment_data = cache.get_behavior_ophys_experiment(940433497)
    assert("ophys_experiment_id" in pytest.experiment_data)

    return

@pytest.fixture(autouse=True)
def set_variables():
    data_storage_directory = Path("/./visual_behavior_ophys_cache_dir")
    cache = VisualBehaviorOphysProjectCache.from_s3_cache(cache_dir=data_storage_directory)
    pytest.experiment_data = cache.get_behavior_ophys_experiment(940433497)
    pytest.behavior_data = cache.get_behavior_session(870987812)
    assert("ophys_experiment_id" in pytest.experiment_data)
    assert("behavior_session_id" in pytest.behavior_data and "ophys_experiment_id" not in pytest.experiment_data)
    return

def test_get_lick_timestamps():
    res = data.get_lick_timestamps(pytest.experiment_data)
    assert('licks' in res)
    res = data.get_lick_timestamps(pytest.behavior_data)
    assert('licks' in res)

def test_get_reward_timestamps():
    res = data.get_reward_timestamps(pytest.experiment_data)
    assert('rewards' in res)
    res = data.get_reward_timestamps(pytest.behavior_data)
    assert('rewards' in res)

def test_get_running_speed():
    res, timestamps = data.get_pupil_area(pytest.experiment_data)
    assert('pupil_area' in res)


def test_get_dff_trace():
    res, timestamps = data.get_dff_trace(pytest.experiment_data)
    assert('dff' in res)