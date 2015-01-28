'''
intervaltree-bio: Interval tree convenience classes for genomic data.

Note that "python setup.py test" invokes pytest on the package. With appropriately
configured setup.cfg, this will check both xxx_test modules and docstrings.

Copyright 2014, Konstantin Tretyakov.

Licensed under MIT.
'''
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


version = '1.0'
setup(
    name = 'intervaltree_bio',
    version = version,
    description = 'Interval tree convenience classes for genomic data',
    long_description=open("README.rst").read(),
    classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Software Development :: Libraries',
    ],
    keywords="interval-tree data-structure intervals tree genomics bioinformatics ucsc", # Separate with spaces
    author = 'Konstantin Tretyakov',
    author_email = 'kt@ut.ee',
    url='https://github.com/konstantint/intervaltree-bio',
    license="MIT",
    packages=find_packages(exclude=['examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=['intervaltree'],    
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    entry_points={}
)
