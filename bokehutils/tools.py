# Copyright (C) 2015 by Per Unneberg
from bokeh.models.tools import Tool
from bokehutils.core import inspect_fig_arg

@inspect_fig_arg
def tooltips(fig, tool, tips):
    """tooltips - set the tooltips for a figure

    Args:
      fig (:py:class:`bokeh.plotting.Figure`): figure object
      tool (:py:class:`bokeh.models.tools.Tool`): 
      tips (list[(str,str), ...]): list of 2-tuple strings

    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show
          from bokeh.models.tools import HoverTool
          from bokehutils.geom import points
          from bokehutils.tools import tooltips

          df = pd.DataFrame([[1, 1, "A", "1"],
                             [2, 0, "B", "2"],
                             [3, 8, "C", "3"],
                             [4, 12, "D", "7"]],
                             columns=["x", "y", "foo", "bar"])
          fig = figure(tools="hover")
          points(fig, "x", "y", df=df, size=20)
          tooltips(fig, HoverTool, [("foo", "@foo"),
                                    ("bar", "@bar")])
          show(fig)
    """
    assert type(tool) == type(Tool),\
        "tool parameter must be of type {}".format(Tool)
    h = fig.select(dict(type=tool))
    h.tooltips = tips

