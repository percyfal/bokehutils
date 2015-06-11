# Copyright (C) 2015 by Per Unneberg
from bokehutils.core import inspect_args, inspect_fig_arg
import logging

logger = logging.getLogger(__name__)


@inspect_fig_arg
def xaxis(fig, i=0, **kwargs):
    """xaxis - modify the xaxis

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      i (int): index to use if setting tick formatters and the like; see `tick label formats <http://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#tick-label-formats>`_
      kwargs: keyword arguments to pass to figure xaxis

    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          import numpy as np
          from bokeh.plotting import figure, show, hplot
          from bokehutils.geom import points
          from bokehutils.axes import xaxis, yaxis, grid

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])
          f = figure(title="Test", width=300, height=300)
          points(f, "x", "y", df, color="red")
          points(f, "y", "x", df, legend="y")
          
          xaxis(f, axis_label="x", major_label_orientation=np.pi/3)
          yaxis(f, axis_label=None, axis_line_color=None)
          grid(f, grid_line_color="black")
          show(f)


    """
    # Should work on splattable list except if tick formatter etc
    for k, v in kwargs.items():
        setattr(fig.xaxis, k, v)

@inspect_fig_arg
def yaxis(fig, i=0, **kwargs):
    """yaxis - modify the yaxis
    
    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      i (int): index to use if setting tick formatters and the like; see `tick label formats <http://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#tick-label-formats>`_
      kwargs: keyword arguments to pass to figure yaxis
      
    Example:

      see xaxis example
    """
    # Should work on splattable list except if tick formatter
    for k, v in kwargs.items():
        setattr(fig.yaxis, k, v)


@inspect_fig_arg
def grid(fig, **kwargs):
    """grid - modify the grid
    
    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      kwargs: keyword arguments to pass to figure grid
      
    Example:

      see xaxis example
    """
    for k, v in kwargs.items():
        setattr(fig.grid, k, v)
