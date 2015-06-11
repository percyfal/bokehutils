# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103, C0111, R0201, E1101, C0325
import unittest
from . import data, fig, source
from nose.tools import raises
from bokeh.plotting import show, output_file, figure
from bokehutils.geom import points, dotplot


class TestPoints(unittest.TestCase):
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
        points(self._fig, "x", "y", self._data)

    def test_style(self):
        points(self._fig, "x", "y", self._data, line_color='gray', size=20, color="red", width=200, height=200)


class TestDotplot(unittest.TestCase):
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

    @raises(TypeError)
    def test_dotplot_int(self):
        dotplot(self._fig, "x", "y", self._data)

    # This works
    def test_dotplot(self):
        # BUG: must currently set x_range to categorical axis,
        # otherwise we would need to recreate the figure in the
        # dotplot function
        f = figure(x_range=list(self._data["treatment"]), height=200, width=200)
        dotplot(f, "treatment", "y", self._data, line_color='gray', size=20, color="red", legend="y")
        # output_file("tabort.html")
        # show(f)

    # How to update axes when range not set?!?
    def test_dotplot_fig(self):
        dotplot(self._fig, "treatment", "y", self._data, line_color='gray', size=20, color="red")
        # output_file("tabort.html")
        # show(self._fig)
