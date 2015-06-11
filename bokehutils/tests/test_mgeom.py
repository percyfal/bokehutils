# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103, C0111, R0201, E1101, C0325
import unittest
from . import data, fig, source
from nose.tools import raises
from bokeh.plotting import show, output_file, figure
from bokehutils.mgeom import mpoints


class TestMPoints(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls._data = data
        cls._source = source
        cls._fig = fig


    @classmethod
    def tearDownClass(cls):
        del cls._data
        del cls._source
        del cls._fig

    def test_init(self):
        print ("Testing init")
        mpoints(self._fig, "x", ["y", "z"], self._data)
        output_file("tabort.html")
        show(self._fig)

