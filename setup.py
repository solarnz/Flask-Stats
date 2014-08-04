#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = [
    'Flask',
    'statsd',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='Flask-Stats',
    version='0.1.0',
    description='A flask plugin to keep stats about your application',
    long_description=readme,
    author='Chris Trotman',
    author_email='chris@trotman.io',
    url='https://github.com/solarnz/Flask-Stats',
    packages=[
        'flask_stats',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='Flask-Stats',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
