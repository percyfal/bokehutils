# Copyright (C) 2015 by Per Unneberg
from bokehutils.core import inspect_fig_arg
import logging

logger = logging.getLogger(__name__)


@inspect_fig_arg
def xaxis(fig, i=None, **kwargs):
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
          from bokehutils.axes import xaxis, yaxis, grid, main, legend

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])
          f = figure(title="Test", plot_width=300, plot_height=300)
          points(f, "x", "y", df, color="red")
          points(f, "y", "x", df, legend="y")
          
          xaxis(f, axis_label="x", major_label_orientation=np.pi/3)
          yaxis(f, axis_label=None, axis_line_color=None)
          grid(f, grid_line_color="black")
          main(f, title="My plot", title_text_font_style="italic",
                title_text_color="olive", title_text_font="times")
          legend(f, orientation="bottom_left")
          show(f)


    """
    for k, v in kwargs.items():
        try:
            if i is None:
                setattr(fig.xaxis, k, v)
            else:
                setattr(fig.xaxis[i], k, v)
        except AttributeError:
            logger.error("unexpected attribute {} to {}".format(k, fig.xaxis))
            raise

@inspect_fig_arg
def yaxis(fig, i=None, **kwargs):
    """yaxis - modify the yaxis
    
    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      i (int): index to use if setting tick formatters and the like; see `tick label formats <http://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#tick-label-formats>`_
      kwargs: keyword arguments to pass to figure yaxis
      
    Example:

      see xaxis example
    """
    for k, v in kwargs.items():
        try:
            if i is None:
                setattr(fig.yaxis, k, v)
            else:
                setattr(fig.yaxis[i], k, v)
        except AttributeError:
            logger.error("unexpected attribute {} to {}".format(k, fig.yaxis))
            raise


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
        try:
            setattr(fig.grid, k, v)
        except AttributeError:
            logger.error("unexpected attribute {} to {}".format(k, fig.grid))
            raise

@inspect_fig_arg
def main(fig, **kwargs):
    """main - modify the title
    
    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      kwargs: keyword arguments to pass to figure.title
      
    Example:


    """
    for k, v in kwargs.items():
        if not k.startswith("title"):
            logger.warn("trying to set attribute {} via title".format(k))
            continue
        try:
            setattr(fig, k, v)
        except AttributeError:
            logger.error("unexpected attribute {} to 'main'".format(k))
            raise

@inspect_fig_arg
def legend(fig, **kwargs):
    """legend - modify the legend
    
    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      kwargs: keyword arguments to pass to figure.legend

    Example:

    See xaxis.
    """
    if len(fig.legend) == 0:
        logger.warn("no legend defined in figure; creation of new legend currently not supported")
        return
    for k, v in kwargs.items():
        try:
            setattr(fig.legend, k, v)
        except AttributeError:
            logger.error("unexpected attribute {} to {}".format(k, fig.legend))
            raise
        except:
            raise
