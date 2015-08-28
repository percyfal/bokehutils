# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103, C0111, R0201, E1101, C0325
import unittest
from nose.tools import raises
from . import data, fig, source
from bokeh.plotting import show, output_file
from bokehutils.mgeom import mpoints, mlines, mdotplot


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


class TestMLines(unittest.TestCase):
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
        mlines(self._fig, "x", ["y", "z"], self._data, color=["red", "blue"], legend=["y", "z"])
        output_file("tabort.html")
        show(self._fig)


class TestMDotplot(unittest.TestCase):

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


    def test_mdotplot(self):
        mdotplot(self._fig, x="treatment", y=["y", "z"],
                 df=self._data, color=["red", "blue"],
                 legend=["y", "z"],
                 size=10, alpha=0.5)
        output_file("tabort.html")
        show(self._fig)

    @raises(AttributeError)
    def test_mdotplot_title(self):
        mdotplot(self._fig, x="treatment", y=["x", "y"],
                 df=self._data, size=10, alpha=0.5,
                 title="test",title_text_font_size='12pt')
