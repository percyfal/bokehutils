# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103, C0111, R0201, E1101, C0325
import unittest
from . import data, fig, source
from nose.tools import raises
from bokeh.plotting import show, output_file, figure
from bokehutils.geom import points


class TestAxes(unittest.TestCase):
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

    def test_axis(self):
        points(self._fig, "x", "y", self._data)
        points(self._fig, "y", "x", self._data)
        print(self._fig.xaxis)
