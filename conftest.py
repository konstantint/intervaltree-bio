import os

import pytest

def pytest_addoption(parser):
    parser.addoption("--datadir",
                     help="path to data files")

def pytest_generate_tests(metafunc):
    if 'base_url' in metafunc.fixturenames:
        if metafunc.config.option.datadir:
            base_url = ('file://'
                        + os.path.abspath(metafunc.config.option.datadir)
                        + os.sep)
        else:
            base_url = 'http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/'
            # Mirror. Slightly faster and more stable, I believe -KT

            base_url = 'http://kt.era.ee/distribute/pyintervaltree/'
        metafunc.parametrize('base_url',[base_url])
