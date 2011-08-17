
#!/usr/local/bin/python
#-*- coding:utf-8 -*-
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'author': 'gulimujyujyu',
	'url': 'URL',
	'download_url': 'Download URL',
	'author_email': 'author_email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projecyname'
}

setup(**config)