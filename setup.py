#!/usr/bin/env python
# encoding: utf-8

import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


setup(
	name = "WebCore-PathOfExile-Site",
	version = "0.1",

	description = "A clone of the Path of Exile website with forums built in WebCore.",
	long_description = "",
	url = "https://github.com/jmpurtle/wc-poe-site",
	author = "John Purtle",
	author_email = "hello@johnpurtle.com",
	license = "mit",
	keywords = [],

	packages = find_packages(exclude=['test', 'example', 'conf', 'benchmark', 'tool', 'doc']),
	include_package_data = True,
	package_data = {'': [
		'README.rst',
		'LICENSE.txt'
	]},

	namespace_packages = [
		'web',
		'web.app'
	],

	setup_requires = [
		'pytest-runner',
	],

	tests_require = [
		'pytest-runner',
		'coverage',
		'pytest',
		'pytest-cov',
		'pytest-spec',
		'pytest-flakes',
	],

	install_requires = [
		'WebCore>=2.0,<3',
		'marrow.mongo', # Database connectivity.
		'web.dispatch.object', # Object (class-based filesystem-like) dispatch.
		'web.dispatch.resource', # Resource (RESTful) dispatch.
		'cinje', # Template engine.
	],

	extras_require = dict(
		development = [
			'pytest-runner',
			'coverage',
			'pytest',
			'pytest-spec',
			'pytest-flakes',
		],
	),

	entry_points = {}
)