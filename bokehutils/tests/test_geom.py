# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103, C0111, R0201, E1101, C0325
import unittest
from . import data, source
from nose.tools import raises
from bokeh.plotting import show, output_file, figure
from bokehutils.geom import points


class TestPoints(unittest.TestCase):
    def setUp(self):
        self.f = figure()
    
    @classmethod
    def setUpClass(cls):
        cls._data = data
        cls._source = source


    @classmethod
    def tearDownClass(cls):
        del cls._data
        del cls._source


    def test_init(self):
        points(self.f, "x", "y", self._data)

    def test_style(self):
        points(self.f, "x", "y", self._data, line_color='gray', size=20, color="red", width=200, height=200)

