# visual_behavior_plotting
Utilities for manipulating and visualizing data from the [Allen Institute Visual Behavior project](https://allensdk.readthedocs.io/en/latest/visual_behavior_optical_physiology.html).

Functions in this repository depend on the AllenSDK
https://github.com/AllenInstitute/AllenSDK


# Installation

Set up a dedicated conda environment for visual behavior plotting :

```
conda create -n visual_behavior python=3.8 
```

Activate the new environment:

```
conda activate visual_behavior
```

Make the new environment visible in the Jupyter 
```
pip install ipykernel
python -m ipykernel install --user --name visual_behavior
```

Install visual_behavior_plotting
```
pip install visual_behavior_plotting
```

