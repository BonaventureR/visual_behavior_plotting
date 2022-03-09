Functional Specifications 

Background.

The Allen Software Development Kit (allen-sdk) provides data for reading and processing Allen Brain Atlas Data. Our intention is to work with the Visual Behavior dataset provided by the allen-sdk. Specifically, we aim to create a plotting package that aids in pre-analysis and visualization of information provided by the experiments.

User profile.

    Researchers
    Students
    

Data sources.

    https://portal.brain-map.org/
    https://allensdk.readthedocs.io/en/latest/install.html
    

Use cases.

    Plotting Neural Plots
        USER: Provides datatable to analyze optical physiology (ophys) features 
        USER: Provides features to be plotted
        PROGRAM: Filters data to subset of features
        PROGRAM: Adds all visualization with subsetted data
        OUTPUT: Returns visualization of all neural plots specified.
    Plotting Behavioral Plots
        USER: Provides datatable to analyze behavioral activity features 
        USER: Provides features to be plotted
        PROGRAM: Filters data to subset of features
        PROGRAM: Adds all visualization with subsetted data
        OUTPUT: Returns visualization of all behavioral plots specified.
