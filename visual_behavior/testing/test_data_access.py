import allensdk
from allensdk.brain_observatory.behavior.behavior_project_cache import VisualBehaviorOphysProjectCache
import matplotlib.pyplot as plt
import numpy as np
import path as Path
import pytest

import data_access as data


@pytest.fixture(autouse=True)
def set_variables():
    data_storage_directory = os.path.join(".","visual_behavior_ophys_cache_dir")
    cache = VisualBehaviorOphysProjectCache.from_s3_cache(cache_dir=data_storage_directory)
    pytest.experiment_data = cache.get_behavior_ophys_experiment(940433497)
    pytest.behavior_data = cache.get_behavior_session(870987812)
    assert("ophys_experiment_id" in pytest.experiment_data.list_data_attributes_and_methods())
    assert("behavior_session_id" in pytest.behavior_data.list_data_attributes_and_methods())
    return

def test_get_lick_timestamps():
    res = data.get_lick_timestamps(pytest.experiment_data)
    assert(len(res) > 0)
    # assert('licks' in res)
    res = data.get_lick_timestamps(pytest.behavior_data)
    assert(len(res) > 0)
    # assert('licks' in res)

def test_get_reward_timestamps():
    res = data.get_reward_timestamps(pytest.experiment_data)
    # assert('rewards' in res)
    assert(len(res) > 0)
    res = data.get_reward_timestamps(pytest.behavior_data)
    assert(len(res) > 0)
    # assert('rewards' in res)

def test_get_running_speed():
    res, timestamps = data.get_running_speed_timeseries(pytest.behavior_data)
    assert(len(res) > 0)
    # assert('pupil_area' in res)

def test_get_pupil_area_timeseries():
    res, timestamps = data.get_pupil(pytest.experiment_data)
    assert(len(res) > 0)

def test_get_dff_trace():
    res, timestamps = data.get_dff_trace(pytest.experiment_data)
    assert(len(res) > 0)
    # assert('dff' in res)