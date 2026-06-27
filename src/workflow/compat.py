"""Python 3 compatibility helpers for Alfred-Workflow."""

import pickle
import plistlib

basestring = str
unicode = str


def read_plist(path):
    with open(path, 'rb') as fp:
        return plistlib.load(fp)


def write_plist(data, path):
    with open(path, 'wb') as fp:
        plistlib.dump(data, fp)


# cPickle was merged into pickle in Python 3.
cPickle = pickle
