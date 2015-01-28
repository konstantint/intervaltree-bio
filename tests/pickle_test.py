'''
Test module for GenomeIntervalTree

Copyright 2014, Konstantin Tretyakov

Licensed under MIT license.
'''
import os

from intervaltree_bio import GenomeIntervalTree
from collections import defaultdict
import pickle

def test_pickling():
    git = GenomeIntervalTree()
    git['a'][1:2] = ['some', 'data']
    git['a'][1.5:2.5] = ['more', 'data']
    git['b'][10:12] = ['even', 'more', 'data']
    s = pickle.dumps(git)
    new_git = pickle.loads(s)
    assert len(git) == len(new_git)
    assert len(git['a']) == len(new_git['a'])
