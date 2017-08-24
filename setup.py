#!/usr/bin/env python

from setuptools import setup, find_packages
import evalidator

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='evalidator',
      version=evalidator.__version__,
      description='Checks if an e-mail address exists or not',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'evalidate = evalidator.evalidator:command_line',
            ]
      },
      url='https://www.github.com/ritiek/email-validator',
      keywords=['email', 'validator', 'exists', 'check', 'command-line', 'library', 'python'],
      license='MIT',
      download_url='https://github.com/Ritiek/AskQuora/archive/v' + evalidator.__version__ + '.tar.gz',
      classifiers=[],
      install_requires=[
            'requests',
      ]
)
