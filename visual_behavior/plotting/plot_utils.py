import seaborn as sns
import matplotlib.pyplot as plt

# colors are all hexidecimel 

DATASTREAM_STYLE_DICT = {
    "licks":                  {"color": "#252525",                  # black 
                               "label": "licks"},
    "rewards_earned":         {"color": "#2171b5",                  # dark blue
                               "label": "earned rewards"},
    "rewards_auto":           {"color": "#6baed6",                  # light blue
                               "label": "auto rewards"},
    "pupil_diameter":         {"color": "#fdc086",                  # light orange
                               "label": "pupil diameter"},
    "physio":                 {"color": "#7fc97f",                  # light green
                               "label":  "df/f"},
    "running_speed":          {"color": "#beaed4",                  # light purple
                               "label": "running speed (cm/sec)"},
    "stimulus_presentations": {"color": "#cccccc",                  # light grey 
                               "label": "stim presentations"}
}

CRELINE_STYLE_DICT = {
    "Sst-IRES-Cre":      {"color": "#b35806", "label": "Sst"}, # orange (dark)
    "Vip-IRES-Cre":      {"color": "#fdb863", "label": "Vip"}, # orange (medium-light)
    "Slc17a7-IRES2-Cre": {"color": "#8073ac", "label": "Slc"}  # purple (medium-dark)
}

NOVELTY_STYLE_DICT = {
    "TRAINING_0": {"color": "#525252", "label": "TRAINING gratings"}, # gray (darkest)
    "TRAINING_1": {"color": "#525252", "label": "TRAINING gratings"}, 
    "TRAINING_2": {"color": "#525252", "label": "TRAINING gratings"}, 
    "TRAINING_3": {"color": "#bdbdbd", "label": "TRAINING images"},   
    "TRAINING_4": {"color": "#bdbdbd", "label": "TRAINING images"},   
    "TRAINING_5": {"color": "#bdbdbd", "label": "TRAINING images"}, 
    "OPHYS_0":    {"color": "#f7f7f7", "label": "habituation"},       # light gray
    "OPHYS_1":    {"color": "#2166ac", "label": "familiar 1"},        # blue (dark)
    "OPHYS_2":    {"color": "#67a9cf", "label": "familiar 2"},        # blue (medium)
    "OPHYS_3":    {"color": "#d1e5f0", "label": "familiar 3"},        # blue (light)
    "OPHYS_4":    {"color": "#b2182b", "label": "novel 1"},           # red (dark)
    "OPHYS_5":    {"color": "#ef8a62", "label": "novel 2"},           # red (medium)
    "OPHYS_6":    {"color": "#fddbc7", "label": "novel 3"}            # red (light) 
}

TRAINING_STYLE_DICT = {
    "TRAINING_0": {"color": "#525252", "label": "TRAINING 0 gratings"}, # gray (darkest)
    "TRAINING_1": {"color": "#737373", "label": "TRAINING 1 gratings"}, 
    "TRAINING_2": {"color": "#969696", "label": "TRAINING 2 gratings"}, 
    "TRAINING_3": {"color": "#bdbdbd", "label": "TRAINING 3 images"},   
    "TRAINING_4": {"color": "#d9d9d9", "label": "TRAINING 4 images"},   
    "TRAINING_5": {"color": "#f7f7f7", "label": "TRAINING 5 images"}    # gray (lightest)
}


IMAGE_SET_STYLE_DICT = {
    "A": {"color": "#a6611a", "label": "A"}, # dark brown
    "B": {"color": "#018571", "label": "B"}, # dark teal
    "G": {"color": "#dfc27d", "label": "G"}, # light brown
    "H": {"color": "#80cdc1", "label": "H"},  # light teal
    "gratings": {"color": "#737373", "label": "gratings"} # gray
}

BEHAV_RESP_STYLE_DICT = {
    "hit":            {"color": "#4dac26", "label": "hit" },            # bright green    
    "miss":           {"color": "#d01c8b", "label": "miss"},            # hot pink
    "false_alarm":    {"color": "#f1b6da", "label": "false alarm"},     # light pink
    "correct_reject": {"color": "#b8e186", "label": "correct reject"},  # light green
    "aborted":        {"color": "#525252", "label": "aborted"}          # dark grey
}

def get_style_for_stim_name(dictionary, stimulus_name):
    dict_keys = dictionary.keys()
    for key in dict_keys:
        if key in stimulus_name:
            return dictionary[key]["color"], dictionary[key]["label"]
        else:
            print("Stimulus name cannot be aligned dictionary keys.")

def get_image_set_style_for_stim_name(stimulus_name):
    return get_style_for_stim_name(IMAGE_SET_STYLE_DICT,
                                   stimulus_name)

def get_novelty_style_for_stim_name(stimulus_name):
    return get_style_for_stim_name(NOVELTY_STYLE_DICT,
                                   stimulus_name)

# STIM_NOVELTY_STYLE_DICT = {
#     'TRAINING_0_gratings_autorewards_15min': {"color": TRAINING_STYLE_DICT["TRAINING_0"]["color"]}, 
#     'TRAINING_1_gratings':                   {"color": TRAINING_STYLE_DICT["TRAINING_1"]["color"]}, 
#     'TRAINING_2_gratings_flashed':           {"color": TRAINING_STYLE_DICT["TRAINING_2"]["color"]}, 
#     'TRAINING_3_images_A_10uL_reward': {"color": TRAINING_STYLE_DICT["TRAINING_3"]["color"], "label": },
#     'TRAINING_3_images_B_10uL_reward': {"color": TRAINING_STYLE_DICT["TRAINING_3"]["color"], "label": },
#     'TRAINING_3_images_G_10uL_reward': {"color": TRAINING_STYLE_DICT["TRAINING_3"]["color"], "label": },
#     'TRAINING_4_images_A_training':       {"color": TRAINING_STYLE_DICT["TRAINING_4"]["color"], "label": },
#     'TRAINING_4_images_A_handoff_ready':  {"color": TRAINING_STYLE_DICT["TRAINING_4"]["color"], "label": },
#     'TRAINING_4_images_A_handoff_lapsed': {"color": TRAINING_STYLE_DICT["TRAINING_4"]["color"], "label": },
#     'TRAINING_4_images_B_training':       {"color": TRAINING_STYLE_DICT["TRAINING_4"]["color"], "label": },
#     'TRAINING_4_images_G_training':       {"color": TRAINING_STYLE_DICT["TRAINING_4"]["color"], "label": },   
#     'TRAINING_5_images_A_epilogue':       {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": },
#     'TRAINING_5_images_A_handoff_ready':  {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": },
#     'TRAINING_5_images_A_handoff_lapsed': {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": }, 
#     'TRAINING_5_images_B_epilogue':       {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": },
#     'TRAINING_5_images_B_handoff_ready':  {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": },
#     'TRAINING_5_images_B_handoff_lapsed': {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": },
#     'TRAINING_5_images_G_epilogue':       {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": },  
#     'TRAINING_5_images_G_handoff_ready':  {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": },  
#     'TRAINING_5_images_G_handoff_lapsed': {"color": TRAINING_STYLE_DICT["TRAINING_5"]["color"], "label": }, 
#     'OPHYS_0_images_A_habituation': {"color": NOVELTY_STYLE_DICT["TRAINING_5"]["color"], "label": },
#     'OPHYS_0_images_B_habituation': {"color": NOVELTY_STYLE_DICT["TRAINING_5"]["color"], "label": },
#     'OPHYS_0_images_G_habituation': {"color": NOVELTY_STYLE_DICT["TRAINING_5"]["color"], "label": },
#     'OPHYS_1_images_A': {"color": NOVELTY_STYLE_DICT["OPHYS_1"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_1"]['label']},  
#     'OPHYS_1_images_B': {"color": NOVELTY_STYLE_DICT["OPHYS_1"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_1"]['label']},
#     'OPHYS_1_images_G': {"color": NOVELTY_STYLE_DICT["OPHYS_1"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_1"]['label']},
#     'OPHYS_2_images_A_passive': {"color": NOVELTY_STYLE_DICT["OPHYS_2"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_2"]['label']},
#     'OPHYS_2_images_B_passive': {"color": NOVELTY_STYLE_DICT["OPHYS_2"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_2"]['label']},
#     'OPHYS_2_images_G_passive': {"olor": NOVELTY_STYLE_DICT["OPHYS_2"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_2"]['label']},
#     'OPHYS_3_images_A': {"color": NOVELTY_STYLE_DICT["OPHYS_3"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_3"]['label']},
#     'OPHYS_3_images_B': {"color": NOVELTY_STYLE_DICT["OPHYS_3"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_3"]['label']},
#     'OPHYS_3_images_G': {"color": NOVELTY_STYLE_DICT["OPHYS_3"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_3"]['label']},
#     'OPHYS_4_images_B': {"color": NOVELTY_STYLE_DICT["OPHYS_4"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_4"]['label']},
#     'OPHYS_4_images_A': {"color": NOVELTY_STYLE_DICT["OPHYS_4"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_4"]['label']},
#     'OPHYS_4_images_H': {"color": NOVELTY_STYLE_DICT["OPHYS_4"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_4"]['label']},
#     'OPHYS_5_images_B_passive': {"color": NOVELTY_STYLE_DICT["OPHYS_5"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_5"]['label']},
#     'OPHYS_5_images_A_passive': {"color": NOVELTY_STYLE_DICT["OPHYS_5"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_5"]['label']},
#     'OPHYS_5_images_H_passive': {"color": NOVELTY_STYLE_DICT["OPHYS_5"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_5"]['label']},
#     'OPHYS_6_images_B': {"color": NOVELTY_STYLE_DICT["OPHYS_6"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_6"]['label']},
#     'OPHYS_6_images_A': {"color": NOVELTY_STYLE_DICT["OPHYS_6"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_6"]['label']},
#     'OPHYS_6_images_H': {"color": NOVELTY_STYLE_DICT["OPHYS_6"]["color"], "label": NOVELTY_STYLE_DICT["OPHYS_6"]['label']},
# }

# STIM_IMG_SET_STYLE_DICT = {
#     'TRAINING_0_gratings_autorewards_15min': 
#         {"color": IMAGE_SET_STYLE_DICT["gratings"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["gratings"]["label"]}, 
#     'TRAINING_1_gratings':
#         {"color": IMAGE_SET_STYLE_DICT["gratings"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["gratings"]["label"]}, 
#     'TRAINING_2_gratings_flashed':
#         {"color": IMAGE_SET_STYLE_DICT["gratings"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["gratings"]["label"]},
#     'TRAINING_3_images_A_10uL_reward': 
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#         "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'TRAINING_4_images_A_training':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'TRAINING_4_images_A_handoff_ready':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'TRAINING_4_images_A_handoff_lapsed':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'TRAINING_5_images_A_epilogue':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'TRAINING_5_images_A_handoff_ready':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'TRAINING_5_images_A_handoff_lapsed':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]}, 
#     'OPHYS_0_images_A_habituation':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'OPHYS_1_images_A':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},  
#     'OPHYS_2_images_A_passive':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'OPHYS_3_images_A':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'OPHYS_4_images_A':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'OPHYS_5_images_A_passive':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'OPHYS_6_images_A':
#         {"color": IMAGE_SET_STYLE_DICT["A"]["color"], 
#          "label": IMAGE_SET_STYLE_DICT["A"]["label"]},
#     'TRAINING_3_images_B_10uL_reward':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'TRAINING_4_images_B_training':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'TRAINING_5_images_B_epilogue':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'TRAINING_5_images_B_handoff_ready':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'TRAINING_5_images_B_handoff_lapsed':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'OPHYS_0_images_B_habituation':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'OPHYS_1_images_B':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'OPHYS_2_images_B_passive':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'OPHYS_3_images_B':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'OPHYS_4_images_B':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'OPHYS_5_images_B_passive':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'OPHYS_6_images_B':
#         {"color": IMAGE_SET_STYLE_DICT["B"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["B"]["label"]},
#     'TRAINING_3_images_G_10uL_reward':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]},
#     'TRAINING_4_images_G_training':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]},   
#     'TRAINING_5_images_G_epilogue':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]},  
#     'TRAINING_5_images_G_handoff_ready':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]},  
#     'TRAINING_5_images_G_handoff_lapsed':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]}, 
#     'OPHYS_0_images_G_habituation':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]},
#     'OPHYS_1_images_G':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]},
#     'OPHYS_2_images_G_passive':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]},
#     'OPHYS_3_images_G':
#         {"color": IMAGE_SET_STYLE_DICT["G"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["G"]["label"]},
#     'OPHYS_4_images_H':
#         {"color": IMAGE_SET_STYLE_DICT["H"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["H"]["label"]},
#     'OPHYS_5_images_H_passive':
#         {"color": IMAGE_SET_STYLE_DICT["H"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["H"]["label"]},
#     'OPHYS_6_images_H':
#         {"color": IMAGE_SET_STYLE_DICT["H"]["color"],
#          "label": IMAGE_SET_STYLE_DICT["H"]["label"]},
# }
