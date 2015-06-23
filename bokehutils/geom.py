# Copyright (C) 2015 by Per Unneberg
import pandas.core.common as com
from bokeh.models import ColumnDataSource
from bokehutils.core import InspectArgs
from bokehutils.color import colorbrewer
import logging

logger = logging.getLogger(__name__)


@InspectArgs()
def points(fig, x, y,
           df=None, source=None, glyph='circle', **kwargs):
    """points: add points to a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.ColumnDataSource`): bokeh ColumnDataSource object
      glyph (str): glyph character to use
      kwargs: keyword arguments to pass to glyph drawing function

    Examples:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from bokehutils.geom import points

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])

          f = figure(title="Points", width=400, height=400)
          points(f, "x", "y", df)
          points(f, "x", "x", df, color="red")
          show(f)
    
      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from bokehutils.geom import points

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])

          f1 = figure(title="Large plot, small points", width=400, height=400)
          points(f1, "x", "y", df)

          f2 = figure(title="Small plot, large points",
                      title_text_font_size="8pt",
                      plot_width=200, plot_height=200)
          points(f2, "x", "y", df, line_color="black", color="red", size=20,
                 glyph="asterisk")
          # Link the x ranges
          f2.x_range = f1.x_range
          show(hplot(f1, f2))

    """
    logger.debug("Adding points to figure {}".format(fig))
    try:
        getattr(fig, glyph)(x=x, y=y, source=source, **kwargs)
    except AttributeError:
        logger.error("no such glyph function {} for {}".format(glyph, fig))
        raise

@InspectArgs()
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

@InspectArgs()
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
    # FIXME: once axes can be modified, one could also transform
    # numerical ranges into factors on the fly
    if com.is_numeric_dtype(source.to_df()[x]) == True:
        raise TypeError("{}: dependant variable must not be numerical type".format(__name__))
    fig.circle(x=x, y=y, source=source, **kwargs)

@InspectArgs()
def lines(fig, x, y, df=None, source=None, groups=None, **kwargs):
    """lines: add lines to a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.ColumnDataSource`): bokeh ColumnDataSource object
      groups (str, list(str)): string or list of strings for columns to group by
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
    if groups is None:
        fig.line(x=x, y=y, source=source, **kwargs)
    else:
        try:
            grouped = df.groupby(groups)
        except:
            raise
        colors = colorbrewer(datalen=len(grouped.groups.keys()))
        for k, color in zip(grouped.groups.keys(), colors):
            name = k
            group = grouped.get_group(name)
            source = ColumnDataSource(group)
            if 'legend' in kwargs:
                kwargs['legend'] = name
            if 'color' in kwargs:
                kwargs['color'] = color
            fig.line(x=x, y=y, source=source, **kwargs)
