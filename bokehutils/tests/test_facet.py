# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103, C0111, R0201, E1101, C0325
import unittest
from . import data, fig, source
from bokehutils.facet import facet_grid


class TestFacet(unittest.TestCase):
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
        self._fig.circle("x", "y", source=self._source)
        facet_grid(self._fig, "x", "y", source=self._source)

    def test_init_groups(self):
        self._fig.line("x", "y", legend="y", source=self._source)
        self._fig.line("x", "z", legend="z", source=self._source, color="red")
        gp = facet_grid(self._fig, "x", ["y", "z"], self._data, groups=["sex"])
