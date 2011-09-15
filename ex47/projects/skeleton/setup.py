
#!/usr/local/bin/python
#-*- coding:utf-8 -*-
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Exercise 47',
	'author': 'gulimujyujyu',
	'url': 'URL',
	'download_url': 'Download URL',
	'author_email': 'author_email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Ex47'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)