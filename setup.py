#!/usr/bin/env python

from distutils.core import setup

setup(
    name='ffprobe',
    version='0.3',
    description='Wrapper around ffprobe command to extract metadata from media files',
    author='Simon Hargreaves',
    author_email='simon@simon-hargreaves.com',
    url='http://www.simon-hargreaves.com/ffprobe',
    packages=['ffprobe'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Natural Language :: English',
		'Topic :: Multimedia :: Video',
		'Topic :: Software Development :: Libraries'
		])