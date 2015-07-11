# Copyright (C) 2015 by Per Unneberg
from setuptools import setup, find_packages
import glob
import versioneer

INSTALL_REQUIRES = [
    'sphinx>=1.3',
    'nose>=1.3.4',
    'bokeh>=0.9.1',
]

_version = versioneer.get_version()
_cmdclass = versioneer.get_cmdclass()

setup(name="bokehutils",
      version=_version,
      cmdclass=_cmdclass,
      author="Per Unneberg",
      author_email="per.unneberg@scilifelab.se",
      description="Utility functions for working with bokeh plots",
      license="MIT",
      scripts=glob.glob('scripts/*.py'),
      install_requires=INSTALL_REQUIRES,
      test_suite='nose.collector',
      packages=find_packages(exclude=['ez_setup', 'test*']),
      namespace_packages=[
          'bokehutils',
      ],
      package_data={
          'bokehutils': [
              'static/*',
              'bokehutils/_templates/*',
          ],
      })
