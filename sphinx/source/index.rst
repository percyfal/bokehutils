.. bokehutils documentation master file, created by
   sphinx-quickstart on Thu Jun 11 09:23:22 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

bokehutils - utility library for bokeh
======================================

`Bokeh <http://bokeh.pydata.org/en/latest/>`_ utility library with
wrapper functions to generate plots mainly for **static** documents.
Most of the functions will probably become obsolete in time as
development of Bokeh is rapid - indeed, much of what is in this
library may already be implemented in Bokeh itself. In particular, I
expect the `Bokeh charts interface
<http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html>`_ to
become a replacement for most functions. The wrappers in bokehutils
can be seen as an abstraction layer somewhere inbetween that of the
`Bokeh plotting interface
<http://bokeh.pydata.org/en/latest/docs/reference/plotting.html>`_ and
the charts interface. The implementation is inspired by ggplot2 as can
be seen by the nomenclature, even though it is not a proper ggplot2
implementation.

Contents
--------

.. toctree::
   :maxdepth: 2

   docs/about
   docs/publishing
   docs/release_notes
   api/modules
