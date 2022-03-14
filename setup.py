from setuptools import setup

setup(name='visual_behavior_plotting',
    version='0.1.9',
    packages=['visual_behavior_plotting'],
    include_package_data = True,
    description='Utilities for loading and visualizing data from the Allen Institute Mindscope Visual Behavior Project',
    url='https://github.com/DowntonCrabby/visual_behavior_plotting',
    author='University of Washington, MSDS Data515 NeuroViz project group',
    author_email='kater@alleninstitute.org, Braj1@uw.edu, amrit.bhat786@gmail.com',
    license='Allen Institute',
    install_requires=[
        'flake8',
        'pytest',
        'allensdk',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: Other/Proprietary License', # Allen Institute Software License
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8'
  ],
)