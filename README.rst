.. -*- mode: rst -*-

change.org fork of scikit-learn
===============================

scikit-learn is awesome but fast moving. The objective of the fork
(more precisely of the stable branch) is to have a production-ready
branch including various modifications to the vanilla scikit-learn.

Dependencies
============

On Ubuntu 12.04 LTS do:

  sudo apt-get install build-essential python-dev python-numpy python-setuptools python-scipy libatlas-dev

The required dependencies to build the software are Python >= 2.6,
setuptools, Numpy >= 1.3, SciPy >= 0.7 and a working C/C++ compiler.

For running the examples Matplotlib >= 0.99.1 is required and for running the
tests you need nose >= 0.10.

This configuration matches the Ubuntu 10.04 LTS release from April 2010.

Install
=======

Make sure you have all the dependencies installed and then do:

  python setup.py build
  sudo python setup.py install

Testing
-------

After installation, you can launch the test suite from outside the
source directory (you will need to have nosetests installed)::

   $ nosetests --exe sklearn

See the web page http://scikit-learn.org/stable/install.html#testing
for more information.

    Random number generation can be controlled during testing by setting
    the ``SKLEARN_SEED`` environment variable.
