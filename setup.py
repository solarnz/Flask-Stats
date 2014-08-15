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

test_requirements = open('requirements-testing.txt').readlines()

setup(
    name='Flask-Stats',
    version='1.0.1',
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
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
