# Copyright (C) 2015 by Per Unneberg
"""NOTE: the functions in this module allow for plotting of multiple
columns of a data frame. If ggplot conventions are to be followed, the
data frame should first be stacked. I keep these here for now as I'm
uncertain what is the best way forward.

"""
import pandas.core.common as com
from bokehutils.core import InspectArgs
from bokehutils.geom import points, dotplot, lines
import logging

logger = logging.getLogger(__name__)


@InspectArgs(allow_y_list=True)
def mpoints(fig, x, y,
           df=None, source=None, glyph='circle', color=False,
           legend=False, **kwargs):
    """points: add points from multiple columns to a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str, list): string or list of strings for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.sources.ColumnDataSource`): bokeh sources.ColumnDataSource object
      glyph (str): glyph character to use
      color (bool): set color
      legend (bool): set legend
      kwargs: keyword arguments to pass to glyph drawing function

    Examples:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from bokehutils.mgeom import mpoints

          df = pd.DataFrame([[1,2,3], [2,5,2], [3,9,6]], columns=["x", "y", "z"])

          f = figure(title="Points", plot_width=400, plot_height=400)
          mpoints(f, "x", ["y", "z"], df, size=10, line_color="black")
          show(f)
    
    """
    logger.debug("Adding mpoints to figure {}".format(fig))
    for i in range(len(y)):
        points(fig=fig, x=x, y=y[i], df=df, source=source,
               glyph=glyph, **kwargs)
        if color:
            # Add color here
            # color = brewer["PiYG"][min(max(3, len(y)), 10)]
            pass
        if legend:
            # Add legend here via legend function
            pass

@InspectArgs(allow_y_list=True)
def mdotplot(fig, x, y, df=None, source=None,
             color=False, legend=False, binaxis="x", **kwargs):
    """mdotplot: make a mdotplot.

    In this implementation, the explanatory variable is treated as a
    factor.

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.sources.ColumnDataSource`): bokeh sources.ColumnDataSource object
      color (bool): set color
      legend (bool): set legend
      binaxis (str): axis to bin dots on
      kwargs: keyword arguments to pass to glyph drawing function

    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show
          from bokehutils.mgeom import mdotplot

          df = pd.DataFrame([[1,2,"A"], [2,5,"B"], [3,9,"A"]],
                            columns=["x", "y", "foo"])
          # NB: currently *must* set the range here
          f = figure(title="Dotplot", plot_width=400, plot_height=400,
                     x_range=list(set(df["foo"])))
          mdotplot(f, "foo", ["y", "x"], df)

          show(f)

    Note that we in the example we must set the range in the call to
    figure, otherwise figure will use linear axis by default. It is
    currently cumbersome to change axes types in an existing figure.
    See `categorical axes
    <http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#categorical-axes>`_
    for more information.
    """
    logger.debug("Adding dotplot to figure {}".format(fig))
    if com.is_numeric_dtype(source.to_df()[x]) == True:
        raise TypeError("{}: dependant variable must not be numerical type".format(__name__))
    for i in range(len(y)):
        dotplot(fig=fig, x=x, y=y[i], source=source, **kwargs)
        if color:
            # Add color here
            # color = brewer["PiYG"][min(max(3, len(y)), 10)]
            pass
        if legend:
            # Add legend here via legend function
            pass
    


@InspectArgs(allow_y_list=True)
def mlines(fig, x, y, df=None, source=None, **kwargs):
    """lines: add lines to a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.sources.ColumnDataSource`): bokeh sources.ColumnDataSource object
      color (bool): set color
      legend (bool): set legend
      kwargs: keyword arguments to pass to fig.line

    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from bokehutils.mgeom import mlines

          df = pd.DataFrame([[1,2,4], [2,5,2], [3,9,12]], columns=["x", "y", "foo"])

          f = figure(title="Line plot", plot_width=400, plot_height=400)
          mlines(f, "x", ["y", "foo"], df, color=["red", "blue"], legend=["y", "foo"])

          show(f)

    """
    logger.debug("Adding points to figure {}".format(fig))
    color = kwargs.pop('color') if 'color' in kwargs else [None] * len(y)
    legend = kwargs.pop('legend') if 'legend' in kwargs else [None] * len(y)
    for yy, c, l in zip(y, color, legend):
        kw = kwargs
        kw['color'] = c
        kw['legend'] = l
        lines(fig=fig, x=x, y=yy, source=source, **kwargs)
    # NB: there is a multi_line plotter already; try it
    # fig.multi_line(xs=x, ys=y, source=source, **kwargs)
