# Copyright (C) 2015 by Per Unneberg
"""NOTE: the functions in this module allow for plotting of multiple
columns of a data frame. If ggplot conventions are to be followed, the
data frame should first be stacked. I keep these here for now as I'm
uncertain what is the best way forward.

"""
import pandas.core.common as com
from bokehutils.core import InspectArgs
from bokehutils.geom import points, dotplot
import logging

logger = logging.getLogger(__name__)


@InspectArgs(allow_y_list=True)
def mpoints(fig, x, y,
           df=None, source=None, glyph='circle', **kwargs):
    """points: add points from multiple columns to a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str, list): string or list of strings for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.ColumnDataSource`): bokeh ColumnDataSource object
      glyph (str): glyph character to use
      kwargs: keyword arguments to pass to glyph drawing function

    Examples:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from bokehutils.mgeom import mpoints

          df = pd.DataFrame([[1,2,3], [2,5,2], [3,9,6]], columns=["x", "y", "z"])

          f = figure(title="Points", width=400, height=400)
          mpoints(f, "x", ["y", "z"], df)
          show(f)
    
    """
    logger.debug("Adding mpoints to figure {}".format(fig))
    for yy in y:
        points(fig=fig, x=x, y=yy, df=df, source=source, glyph=glyph, **kwargs)


@InspectArgs
def abline(fig, x, y, df=None, source=None, slope=0, intercept=0, **kwargs):
    """abline - add an abline to current plot

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.ColumnDataSource`): bokeh ColumnDataSource object
      slope (int): slope of line
      intercept (int): intercept
      kwargs: keyword arguments to pass to line drawing function


    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from bokehutils.geom import abline

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])

          f = figure(title="abline", height=300, width=300)
          abline(f, "x", "y", df=df, slope=1)
          abline(f, "x", "y", df=df, slope=2)
          abline(f, "x", "y", df=df, intercept=3, color="blue", line_width=5)
          show(f)

    """
    logger.debug("Adding abline to figure {}".format(fig))
    x0 = 0
    y0 = intercept
    x1 = max(df[x])
    y1 = (x1-x0) * slope + y0
    kwargs['color'] = kwargs.get('color', 'red')
    fig.line(x=[x0, x1], y=[y0, y1], **kwargs)

@InspectArgs
def dotplot(fig, x, y, df=None, source=None,
            binaxis="x", **kwargs):
    """dotplot: make a dotplot.

    In this implementation, the explanatory variable is treated as a
    factor.

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.ColumnDataSource`): bokeh ColumnDataSource object
      binaxis (str): axis to bin dots on
      kwargs: keyword arguments to pass to glyph drawing function

    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show
          from bokehutils.geom import dotplot
          from bokehutils.axes import grid

          df = pd.DataFrame([[1,2,"A"], [2,5,"B"], [3,9,"A"]], columns=["x", "y", "foo"])

          # NB: currently *must* set the range here, otherwise figure
          # will use linear axis by default. It is currently cumbersome
          # to change axes types in an existing figure.
          f = figure(title="Dotplot", width=400, height=400, x_range=list(df["foo"]))
          dotplot(f, "foo", "y", df)
          grid(f, grid_line_color=None)

          show(f)

    """
    logger.debug("Adding dotplot to figure {}".format(fig))
    if com.is_numeric_dtype(source.to_df()[x]) == True:
        raise TypeError("{}: dependant variable must not be numerical type".format(__name__))
    fig.circle(x=x, y=y, source=source, **kwargs)

@InspectArgs
def lines(fig, x, y, df=None, source=None, **kwargs):
    """lines: add lines to a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.ColumnDataSource`): bokeh ColumnDataSource object
      kwargs: keyword arguments to pass to fig.line

    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from bokehutils.geom import lines

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])

          f = figure(title="Line plot", width=400, height=400)
          lines(f, "x", "y", df, legend="y")
          lines(f, "x", "x", df, legend="x", color="red")

          show(f)

    """
    logger.debug("Adding points to figure {}".format(fig))
    fig.line(x=x, y=y, source=source, **kwargs)
