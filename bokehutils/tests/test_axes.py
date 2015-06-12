# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103, C0111, R0201, E1101, C0325
import unittest
from . import data, fig, source
from nose.tools import raises
import numpy as np
from bokeh.plotting import show, output_file
from bokeh.models import NumeralTickFormatter
from bokehutils.geom import points
from bokehutils.axes import xaxis, legend


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

    @raises(AttributeError)
    def test_axis_wrong_args(self):
        points(self._fig, "x", "y", self._data)
        xaxis(self._fig, foo="bar")

    def test_axis_no_splat(self):
        points(self._fig, "x", "y", self._data)
        xaxis(self._fig, formatter=NumeralTickFormatter(format="0.0%"))
        
    def test_axis(self):
        points(self._fig, "x", "y", self._data)
        points(self._fig, "y", "x", self._data, color="red")
        xaxis(self._fig, axis_label="x", major_label_orientation=np.pi/3)

class TestLegend(unittest.TestCase):
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

    def test_legend(self):
        points(self._fig, "x", "y", self._data)
        legend(self._fig, orientation="bottom_left")
