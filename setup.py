#!/usr/bin/env python
import sys
from setuptools import setup

install_requires = [
	'string',
	'cPickle',
	'pickle',
	're',
	'warnings',
	'time'
]

tests_require = [
]

setup(
	name='Cookie',
	version='0.0.1',
	description='Forked version of Pyramids Cookie',
	author='Patrick Crownover',
	author_email='pcrownov@redhat.com',
	license='Apache 2.0',
	url='https://github.com/pcrownov/Cookie',
	
	packages=[	
		'Cookie'],
	
	package_dir={'': 'src'},
	package_data={'': ['xml/*.xml']},
	classifiers=[
		"Development Status :: 4 - Beta"],

	install_requires=install_requires,
	zip_safe=False,
)
