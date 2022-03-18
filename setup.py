from setuptools import setup, find_packages

setup(name='vb_plotting',
      version='0.1.7',
      description='Utilities for loading and visualizing data from the Allen Institute Mindscope Visual Behavior Project',  # noqa: E501
      url='https://github.com/DowntonCrabby/visual_behavior_plotting',
      author='University of Washington, MSDS Data515 NeuroViz project group',
      author_email='kater@alleninstitute.org, Braj1@uw.edu, amrit.bhat786@gmail.com',  # noqa: E501
      license='Allen Institute',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'License :: Other/Proprietary License',  # Allen Institute Software License  # noqa: E501
          'Natural Language :: English',
          'Programming Language :: Python :: 3.8'
          ],
      packages=find_packages(),
      include_package_data = True,
      install_requires=[
          'flake8',
          'pytest',
          'pathlib',
          'path',
          'allensdk>=2.13.3',
          'coverage',
          'markupsafe==2.0.1'
          ],
      tests_require=['flake8'],

)


