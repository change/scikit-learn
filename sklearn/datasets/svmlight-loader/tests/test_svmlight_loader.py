import numpy as np
import os.path
from StringIO import StringIO

from numpy.testing import assert_equal, assert_array_equal
from nose.tools import raises

from svmlight_loader import (load_svmlight_file, load_svmlight_files,
                             dump_svmlight_file)
from sklearn.datasets import load_svmlight_file as sk_load_svmlight_file

currdir = os.path.dirname(os.path.abspath(__file__))
datafile = os.path.join(currdir, "data", "svmlight_classification.txt")
invalidfile = os.path.join(currdir, "data", "svmlight_invalid.txt")


def test_load_svmlight_file():
    X, y = load_svmlight_file(datafile)

    # test X's shape
    assert_equal(X.indptr.shape[0], 4)
    assert_equal(X.shape[0], 3)
    assert_equal(X.shape[1], 20)
    assert_equal(y.shape[0], 3)

    # test X's non-zero values
    for i, j, val in ((0, 1, 2.5), (0, 9, -5.2), (0, 14, 1.5),
                     (1, 4, 1.0), (1, 11, -3),
                     (2, 19, 27)):

        assert_equal(X[i, j], val)

    # tests X's zero values
    assert_equal(X[0, 2], 0)
    assert_equal(X[0, 4], 0)
    assert_equal(X[1, 7], 0)
    assert_equal(X[1, 15], 0)
    assert_equal(X[2, 17], 0)

    # test can change X's values
    X[0, 1] *= 2
    assert_equal(X[0, 1], 5)

    # test y
    assert_array_equal(y, [1, 2, 3])


def test_load_svmlight_files():
    X_train, y_train, X_test, y_test = load_svmlight_files([datafile] * 2,
                                                           dtype=np.float32)
    assert_array_equal(X_train.toarray(), X_test.toarray())
    assert_array_equal(y_train, y_test)
    assert_equal(X_train.dtype, np.float32)
    assert_equal(X_test.dtype, np.float32)

    X1, y1, X2, y2, X3, y3 = load_svmlight_files([datafile] * 3,
                                                 dtype=np.float64)
    assert_equal(X1.dtype, X2.dtype)
    assert_equal(X2.dtype, X3.dtype)
    assert_equal(X3.dtype, np.float64)


def test_load_svmlight_file_n_features():
    X, y = load_svmlight_file(datafile, n_features=14)

    # test X'shape
    assert_equal(X.indptr.shape[0], 4)
    assert_equal(X.shape[0], 3)
    assert_equal(X.shape[1], 14)

    # test X's non-zero values
    for i, j, val in ((0, 1, 2.5), (0, 9, -5.2),
                     (1, 4, 1.0), (1, 11, -3)):

        assert_equal(X[i, j], val)


@raises(ValueError)
def test_load_invalid_file():
    load_svmlight_file(invalidfile)


@raises(ValueError)
def test_load_invalid_file2():
    load_svmlight_files([datafile, invalidfile, datafile])


@raises(TypeError)
def test_not_a_filename():
    load_svmlight_file(1)


@raises(IOError)
def test_invalid_filename():
    load_svmlight_file("trou pic nic douille")


def test_dump():
    Xs, y = load_svmlight_file(datafile)
    Xd = Xs.toarray()

    for X in (Xs, Xd):
        f = StringIO()
        dump_svmlight_file(X, y, f, zero_based=False)
        f.seek(0)
        X2, y2 = sk_load_svmlight_file(f)
        assert_array_equal(Xd, X2.toarray())
        assert_array_equal(y, y2)
