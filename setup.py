from setuptools import setup

setup(name='visual_behavior_plotting',
    version='0.1.0',
    packages=['visual_behavior_plotting'],
    include_package_data = True,
    description='Utilities for visualizing data from the Allen Institute Visual Behavior Project',
    url='https://github.com/AllenInstitute/mindscope_utilities',
    author='NeurViz project group, University of Washington Masters in Data Science Program',
    author_email='kater@alleninstitute.org, amrit.bhat786@gmail.com, ',
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