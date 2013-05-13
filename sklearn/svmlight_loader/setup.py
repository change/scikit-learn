import numpy
import os

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('svmlight_loader', parent_package, top_path)
    config.add_extension('_svmlight_loader',
            include_dirs=[numpy.get_include()],
            sources = ['_svmlight_loader.cpp'],
            extra_compile_args=['-O3'])
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
