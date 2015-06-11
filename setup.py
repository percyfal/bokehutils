# Copyright (C) 2015 by Per Unneberg
from setuptools import setup, find_packages
import glob
import versioneer

versioneer.VCS = 'git'
versioneer.versionfile_source = 'gaqtk/gaqtk/_version.py'
versioneer.versionfile_build = 'gaqtk/gaqtk/_version.py'
versioneer.tag_prefix = ''  # tags are like 1.2.0
versioneer.parentdir_prefix = 'gaqtk-'  # dirname like 'myproject-1.2.0'

setup(name="bokehutils",
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author="Per Unneberg",
      author_email="per.unneberg@scilifelab.se",
      description="Utility functions for working with bokeh plots",
      license="MIT",
      scripts=glob.glob('scripts/*.py'),
      install_requires=[
          "bokeh",
          "sphinx",
          "nose",
      ],
      test_suite='nose.collector',
      packages=find_packages(exclude=['ez_setup', 'test*']),
      namespace_packages=[
          'bokehutils',
      ],
      package_data={
          'bokehutils': [
              'static/*',
              'templates/*',
          ],
      })
