## Functional Specifications 

#### Background.

The Allen Institute produces large and public neuroscience resources that seek to drive discoveries in fundamental brain properties through integration of experiments, modeling, and theory. Specifically the Visual Behavior 2P project (which we focused our project on) used in vivo 2-photon calcium imaging (also called optical physiology, or “ophys”) to measure the activity of populations of genetically identified neurons in the visual cortex of mice performing a visually guided behavioral task 

The Allen Software Development Kit (allen-sdk) houses source code in python for reading and processing Allen Brain Atlas data. However, despite providing the allen-sdk as an access point, the datasets the institute creates are highly dimensional and can be complicated to visualize and analyze. In order to lower the barrier to entry and further to mission of “open science” we decided to build a plotting package to allow easy axis to basic dataset visualizations. This assists researchers in exploring the datasets quickly and easily, to identify elements of interest that can later be analyzed in more detail.

#### User profile.

- Scientists
- Researchers
- Students/Academics
    
#### Data sources.

- [Allen Brain Map](https://portal.brain-map.org/)
- [Allen SDK](https://allensdk.readthedocs.io/en/latest/install.html)
    

#### Use cases.

Plotting Neural Plots
  - USER: Provides datatable to analyze optical physiology (ophys) features 
  - USER: Provides features to be plotted
  - PROGRAM: Filters data to subset of features
  - PROGRAM: Adds all visualization with subsetted data
  - OUTPUT: Returns visualization of all neural plots specified.

Plotting Behavioral Plots
  - USER: Provides datatable to analyze behavioral activity features 
  - USER: Provides features to be plotted
  - PROGRAM: Filters data to subset of features
  - PROGRAM: Adds all visualization with subsetted data
  - OUTPUT: Returns visualization of all behavioral plots specified.
