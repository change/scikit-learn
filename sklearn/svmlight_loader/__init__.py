"""
This is a fast and memory efficient loader for the
svmlight / libsvm sparse data file format in Python.
See https://github.com/mblondel/svmlight-loader
"""

from .svmlight_loader import load_svmlight_file
from .svmlight_loader import load_svmlight_files
from .svmlight_loader import dump_svmlight_file

__all__ = ['load_svmlight_file',
        'load_svmlight_files',
        'dump_svmlight_file']
