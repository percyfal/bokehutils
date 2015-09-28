# Copyright (C) 2015 by Per Unneberg
from setuptools import setup, find_packages
import glob
import versioneer

INSTALL_REQUIRES = [
    'sphinx>=1.3',
    'pytest',
    'pytest-cov>=1.8.1',
    'bokeh>=0.10.0',
]

# Integrating pytest with setuptools: see
# https://pytest.org/latest/goodpractises.html#integrating-with-distutils-python-setup-py-test
from distutils.core import setup, Command
# you can also import from setuptools

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

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
      packages=find_packages(exclude=['ez_setup', 'test*']),
      package_data={
          'bokehutils': [
              '_templates/*',
              'static/*',
          ],
      })
