About
=====

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

Motivation
----------

I am using bokeh for `another project
<http://snakemakelib.readthedocs.org/>`_. I wrote several wrapper
functions for generating dotplots and scatterplots without a
consistent interface, eventually making it difficult to know when and
how to use what function. This module is an attempt to remedy that
situation. Moreover, it is an exploration of bokeh itself.

More specifically, what I wanted was

1. simplified visual styling via ggplot-like functions
++++++++++++++++++++++++++++++++++++++++++++++++++++++

Although Bokeh `doesn't directly implement ggplot
<http://bokeh.pydata.org/en/latest/docs/faq.html#does-bokeh-implement-r-s-ggplot2>`_,
it bears a lot of similarity. For instance, styling axes can be done
as follows (see `complete example at Bokeh web page
<bokeh.pydata.org/en/latest/docs/user_guide/styling.html#axes>`_)

.. bokeh-plot::
   :source-position: above

   from bokeh.plotting import figure, show

   p = figure(plot_width=400, plot_height=400)
   p.circle([1,2,3,4,5], [2,5,8,2,7], size=10)

   # change just some things about the x-axes
   p.xaxis.axis_label = "Temp"
   p.xaxis.axis_line_width = 3
   p.xaxis.axis_line_color = "red"

   show(p)

However, this quickly leads to many lines of code. Consequently,
bokehutils adds wrapper functions for styling axes (and other
objects). Styling the axes in the the above example with bokehutils
would look like

.. bokeh-plot::
   :source-position: above

   from bokeh.plotting import figure, show
   from bokehutils.axes import xaxis

   p = figure(plot_width=400, plot_height=400)
   p.circle([1,2,3,4,5], [2,5,8,2,7], size=10)

   # change just some things about the x-axes
   xaxis(p, axis_label="Temp",
         axis_line_width=3,
	 axis_line_color="red")

   show(p)


2. high-level plot wrappers that allow shared data sources
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The `charts interface
<http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html>`_
implements many high-level plotting functions, such as dotplots and
scatterplots. However, to my knowledge, it is not possible to pass
source parameters between plots for linked brushing, to give an
example. In bokehutils, one can do the following to generate two
linked dotplots:

.. bokeh-plot::
   :source-position: above

   import pandas as pd
   from bokeh.models import ColumnDataSource
   from bokeh.plotting import figure, show, gridplot
   from bokehutils.geom import dotplot

   df = pd.DataFrame([["foo", 1, 2],
                      ["bar", 3, 4],
		      ["foobar", 2, 6]], 
		      columns=["cat", "x", "y"])
   source = ColumnDataSource(df)
   TOOLS = "box_select,reset,save,wheel_zoom"
   # NB: must set x_range here for categorical axes to work
   f1 = figure(x_range=list(df["cat"]), height=400, width=400,
	       tools=TOOLS)
   dotplot(f1, "cat", "x", source=source)
   f2 = figure(x_range=list(df["cat"]), height=400, width=400,
	       tools=TOOLS)
   dotplot(f2, "cat", "y", source=source, legend="y")

   show(gridplot([[f1, f2]]))

3. easy faceting
++++++++++++++++

The `CrossFilter tool
<http://bokeh.pydata.org/en/latest/docs/user_guide/charts.html>`_
presents an approach to interactive faceting. This is awesome, but at
the time of writing, I was more in the need of "standard" faceting
functionality, in which a plot can be subdivided into panels based on
factors in the data:

.. bokeh-plot::
    :source-position: above

    from bokeh.plotting import figure, show
    from bokeh.sampledata.iris import flowers
    from bokeh.models import ColumnDataSource
    from bokehutils.geom import points
    from bokehutils.facet import facet_grid


    source = ColumnDataSource(flowers)
    f = figure()
    points(f, "sepal_length", "sepal_width", source=source)
    gp = facet_grid(f, "sepal_length", "sepal_width", 
                    flowers, groups="species",
		    width=300, height=300,
		    share_x_range=True,
		    share_y_range=True)
    show(gp)
    
