#!/usr/bin/env python

from setuptools import setup
# from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ffprobe-python',
    version='1.0.3',
    description="""
    A wrapper around ffprobe command to extract metadata from media files.
    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Simon Hargreaves',
    author_email='simon@simon-hargreaves.com',
    maintainer='Mark Ma',
    maintainer_email='519329064@qq.com',
    url='https://github.com/gbstack/ffprobe-python',
    packages=['ffprobe'],
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
