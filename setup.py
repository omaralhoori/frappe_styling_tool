# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in styling_tool/__init__.py
from styling_tool import __version__ as version

setup(
	name='styling_tool',
	version=version,
	description='ERP System Styling Tool',
	author='Omar Alhori',
	author_email='non',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
