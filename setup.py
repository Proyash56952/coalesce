# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# This uses the template https://github.com/pypa/sampleproject/blob/master/setup.py

# To build/upload the package, do the following as described in
# https://python-packaging-user-guide.readthedocs.org/en/latest/distributing.html
# sudo python3 setup.py sdist
# sudo python3 setup.py bdist_wheel --universal
# sudo python3 setup.py sdist bdist_wheel upload

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
import sys

setup(
    name='PyCertCoalesce',

    version='0.0.1',

    description='Certificate Pools for NDN',

    url='https://github.com/Proyash56952/coalesce',

    maintainer='People',
    maintainer_email='email',

    license='LGPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',

        'Programming Language :: Python :: 3'
    ],

    keywords='NDN',

    packages=find_packages(exclude=['tests', 'tests.*']),
    python_requires='>=3.7',

    install_requires=['python-ndn>=0.3a1.post3'],

    extras_require={  # Optional
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
        ],
    },
)
