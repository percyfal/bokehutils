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
      source (:py:class:`~bokeh.models:ColumnDataSource`): bokeh ColumnDataSource object
      glyph (str): glyph character to use
      kwargs: keyword arguments to pass to glyph drawing function

    Example:

      .. bokeh-plot::
      
          import pandas as pd
          from bokeh.plotting import figure, show
          from bokehutils.geom import points

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])
      
          f = figure()
          points(f, "x", "y", df)
          show(f)

    """      
      
    logger.debug("Adding points to figure {}".format(fig))
    try:
        getattr(fig, glyph)(x=x, y=y, source=source, **kwargs)
    except AttributeError:
        logger.error("no such glyph function {} for {}".format(glyph, fig))
        raise
