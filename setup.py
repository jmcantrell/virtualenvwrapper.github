#!/usr/bin/env python

from setuptools import setup

PROJECT = 'virtualenvwrapper.github'
VERSION = '0.1.2'

setup(
        name=PROJECT,
        version=VERSION,

        description='Plugin for virtualenvwrapper to automatically create projects based on github repositories.',

        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',

        url = 'http://github.com/jmcantrell/%s/' % PROJECT,
        download_url='http://github.com/jmcantrell/%s/tarball/%s' % (PROJECT, VERSION),

        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Intended Audience :: Developers',
            'Environment :: Console',
            ],

        platforms=[
            'Any',
            ],

        namespace_packages=[
            'virtualenvwrapper',
            ],

        packages=[
            'virtualenvwrapper',
            ],

        install_requires=[
            'virtualenv',
            'virtualenvwrapper',
            'virtualenvwrapper.project',
            ],

        entry_points={
            'virtualenvwrapper.project.template': [
                'github = virtualenvwrapper.github:template',
                ]
            },

        zip_safe=False,
        )
