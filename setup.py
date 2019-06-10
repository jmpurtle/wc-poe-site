#!/usr/bin/env python3

from setuptools import setup


setup(
	name = "WebCore-PathOfExile-Site",
	version = "0.1",
	
	description = "A clone of the Path of Exile website with forums built in WebCore.",
	long_description = "",
	url = "https://github.com/jmpurtle/wc-poe-site",
	author = "John Purtle",
	author_email = "hello@johnpurtle.com",
	license = "MIT",
	keywords = [],
	
	packages = ('web.app.wc_poe_site', ),
	include_package_data = True,
	package_data = {'': [
		'README.rst',
		'LICENSE.txt'
	]},
	
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
		'backlash', # debug tests
	],
	
	install_requires = [
		'WebCore[development]~=3.0', # Web framework.
		'web.dispatch.object~=3.0', # Object (class-based filesystem-like) dispatch.
		'web.dispatch.resource~=3.0', # Resource (RESTful) dispatch.
		'marrow.mongo~=2.0', # Database connectivity.
		'cinje~=1.1.2', # Template engine.
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
