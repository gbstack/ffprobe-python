#!/usr/bin/env python

from distutils.core import setup

setup(
    name='ffprobe3',
    version='0.1.2',
    description="""
    Original Project: ffprobe (https://pypi.python.org/pypi/ffprobe)

    A wrapper around ffprobe command to extract metadata from media files.

    This project which is maintained by Dheerendra Rathor is a Python 3 port of original ffprobe.
    """,
    author='Simon Hargreaves',
    author_email='simon@simon-hargreaves.com',
    maintainer='Dheerendra Rathor',
    maintainer_email='dheeru.rathor14@gmail.com',
    url='https://github.com/DheerendraRathor/ffprobe3',
    packages=['ffprobe3'],
    keywords='ffmpeg, ffprobe, mpeg, mp4',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: English',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries'
    ])
