from setuptools import setup, find_packages

setup(name='visual_behavior_plotting',
      version='0.1.6',
      packages=find_packages(),
      include_package_data = True,
      description='Utilities for loading and visualizing data from the Allen Institute Mindscope Visual Behavior Project',  # noqa: E501
      url='https://github.com/DowntonCrabby/visual_behavior_plotting',
      author='University of Washington, MSDS Data515 NeuroViz project group',
      author_email='kater@alleninstitute.org, Braj1@uw.edu, amrit.bhat786@gmail.com',  # noqa: E501
      license='Allen Institute',
      install_requires=[
          'flake8>=3.9.8',
          'pytest>=6.2.4',
          'allensdk>=2.13.3',
          'pandas>=1.4.1>=1.4.1',
          'pytest>=6.2.3',
          'seaborn>=0.11.1',
          'path>=16.0.0',
          'numpy>=1.22.0'
          ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'License :: Other/Proprietary License',  # Allen Institute Software License  # noqa: E501
          'Natural Language :: English',
          'Programming Language :: Python :: 3.8'
          ],
)