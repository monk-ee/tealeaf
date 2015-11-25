#! /usr/bin/env python

from setuptools import setup

exec(open("./tea_leaf/_version.py").read())

setup(name="aws-tea_leaf-sdk",
      version=__version__,
      author="monkeemagic",
      author_email="lyndon.swan@cloudtrek.com.au",
      packages=['tea_leaf'],
      install_requires = [
          'boto3',
      ],
      license='GPLv3+',
      description="Provide a modular interface to push stats into CLoudWatch",
      test_suite='aws_iot_sdk.tests',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ]
      )