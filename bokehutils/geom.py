# Copyright (C) 2015 by Per Unneberg
from bokehutils.core import inspect_args
import logging

logger = logging.getLogger(__name__)


@inspect_args
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

    Example:

      .. bokeh-plot::

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from bokehutils.geom import points

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])

          f1 = figure(title="Large plot, small points")
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
