# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904, C0301, C0103, C0111, R0201, E1101, C0325
import unittest
from . import data, source, fig
from nose.tools import raises
from bokehutils.core import InspectArgs, inspect_fig_arg

@InspectArgs()
def func(fig, x, y, df=None, source=None,
        glyph='circle', **kwargs):
    d = {'fig': fig, 'x': x, 'y': y, 'df': df,
        'source': source, 'glyph': glyph}
    d.update(kwargs)
    return d

@InspectArgs(allow_y_list=True)
def func_m(fig, x, y, df=None, source=None,
        glyph='circle', **kwargs):
    d = {'fig': fig, 'x': x, 'y': y, 'df': df,
        'source': source, 'glyph': glyph}
    d.update(kwargs)
    return d

@inspect_fig_arg
def func_f(fig, **kwargs):
    return fig

    
class TestInspectArgs(unittest.TestCase):
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

    @raises(IndexError)
    def test_noargs(self):
        func()

    @raises(IndexError)
    def test_onearg(self):
        func(fig=self._fig)


    @raises(IndexError)
    def test_twoargs(self):
        func(fig=self._fig, x="x")


    @raises(TypeError)
    def test_threeargs(self):
        func("x", fig=self._fig, y="y")


    @raises(AssertionError)
    def test_fig_w(self):
        func(fig="fig", x="x", y="y")

    @raises(TypeError)
    def test_wrong_col(self):
        func(fig=self._fig, x="x", y="foo", df=self._data)

    def test_args_ok(self):
        d = func(self._fig, "x", "y", self._data)
        self.assertEqual(d['x'], "x")
        self.assertEqual(d['y'], "y")
        self.assertEqual(d['fig'], self._fig)

    def test_args_ok_order(self):
        d = func("x", x="y", fig=self._fig, df=self._data)
        self.assertEqual(d['x'], "y")
        self.assertEqual(d['y'], "x")
        self.assertEqual(d['fig'], self._fig)


    def test_args_source(self):
        d = func("x", x="y", fig=self._fig, source=self._source)
        self.assertEqual(d['x'], "y")
        self.assertEqual(d['y'], "x")
        self.assertEqual(d['fig'], self._fig)
        self.assertEqual(d['source'], self._source)
        self.assertListEqual(sorted(list(d['df'].columns)),
                                sorted(self._source.column_names))


class TestInspectYArgs(unittest.TestCase):
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

    @raises(AssertionError)
    def test_wrong_args(self):
        func_m(self._fig, "x", 3, self._data)

    @raises(AssertionError)
    def test_wrong_arglist(self):
        func_m(self._fig, "x", ["1", 2], self._data)

    def test_str(self):
        d = func_m(self._fig, "x", ["y"], self._data)
        self.assertListEqual(d["y"], ["y"])

    def test_list(self):
        d = func_m(self._fig, "x", ["y", "z"], self._data)
        self.assertListEqual(sorted(d["y"]), ["y", "z"])

class TestInspectFigArgs(unittest.TestCase):
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

    def test(self):
        func_f(self._fig)

    @raises(AssertionError)
    def test_error(self):
        func_f(fig="foo")
