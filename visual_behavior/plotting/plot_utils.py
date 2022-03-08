# colors are all hexidecimel 

DATASTREAM_STYLE_DICT = {
    "licks":                  {"color": "#252525",                  # black 
                               "label": "licks"},
    "rewards_earned":         {"color": "#2171b5",                  # dark blue
                               "label": "earned rewards"},
    "rewards_auto":           {"color": "#6baed6",                  # light blue
                               "label": "auto rewards"},
    "pupil_area":             {"color": "#fdc086",                  # light orange
                               "label": "pupil area"},
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
    "TRAINING_0": {"color": "#525252", "label": "training: gratings"}, # gray (darkest)
    "TRAINING_1": {"color": "#525252", "label": "training: gratings"}, 
    "TRAINING_2": {"color": "#525252", "label": "training: gratings"}, 
    "TRAINING_3": {"color": "#bdbdbd", "label": "training: images"},   
    "TRAINING_4": {"color": "#bdbdbd", "label": "training: images"},   
    "TRAINING_5": {"color": "#bdbdbd", "label": "training: images"}, 
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

def get_color_for_dict_key(dictionary, key):
    color = dictionary[key]['color']
    return color

def get_label_for_dict_key(dictionary, key):
    label = dictionary[key]['label']
    return label

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

# def generate_plot_title():

# def generate_plot_palette():


# def plot_timeseries(values, timestamps, palette, labels):
#     sns.lineplot(x = values, y = timestamps, palette = palette)


