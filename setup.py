try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup
from setuptools.command.install import install
import pkg_resources
import sys
import site
import os
from configparser import ConfigParser
from subprocess import call, Popen, PIPE
import work      


data_files = [
    ('/etc/wukong/', ['config.ini']),
    ('/usr/bin', ['wukong']),
    ('.', ['requirements.txt'])
]

setup(name='Wukong',
      version=work.__version__,
      description='A Tools for working backup.',
      author='Kevin Kong',
      author_email='kfxw2007@163.com',
      license='http://www.apache.org/licenses/LICENSE-2.0.html',
      url='',
      data_files=data_files,
      packages=find_packages(),
      package_dir={'%s' % 'wukong': 'wukong'},
      include_package_data=True,
      python_requires='>=3.5',
      install_requires=[
          "autils"
      ],
    )
