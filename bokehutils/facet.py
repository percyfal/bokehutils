# Copyright (C) 2015 by Per Unneberg
"""The facet functions emulate the behaviour found in ggplot. They
behave slightly differently from other bokehutils functions in that
they don't modify an existing plot; rather, the generate a series of
plots that are stitched together in a gridplot.
"""
from bokeh.plotting import figure, gridplot
from bokeh.models import ColumnDataSource
from bokehutils.core import InspectArgs
from bokeh.models.renderers import GlyphRenderer, Legend
import logging

logger = logging.getLogger(__name__)

@InspectArgs(allow_y_list=True)
def facet_grid(fig, x, y, df=None, source=None, groups=None, ncol=3,
               share_x_range=False, share_y_range=False, **kwargs):
    """
    facet_grid - generate a simple gridplot from a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str, list): string or list of strings for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.ColumnDataSource`): bokeh
                                        ColumnDataSource object
      groups (str, list(str)): groups to group by
      ncol (int): number of columns to use in gridplot
      share_x_range (bool): share x range across plots
      share_y_range (bool): share y range across plots
      kwargs: keyword arguments to pass to figure

    Examples:

      .. bokeh-plot::
          :source-position: above

          from bokeh.sampledata.iris import flowers
          from bokeh.models import ColumnDataSource
          from bokeh.plotting import figure, show
          from bokehutils.facet import facet_grid
          from bokehutils.geom import lines, points
          from bokehutils.publish import static_html
          from bokehutils.templates import EXAMPLE, _templates_path

          source = ColumnDataSource(flowers)
          f = figure()
          points(f, "sepal_length", "sepal_width", source=source)
          gp = facet_grid(f, "sepal_length", "sepal_width",
                          flowers, groups="species",
                          width=300, height=300,
                          share_x_range=True,
                          share_y_range=True)

          show(gp)
    """
    if not groups:
        logger.warn("no groups defined; returning without modifying figure")
        return
    try:
        grouped = df.groupby(groups)
    except:
        raise
    flist = []
    gr = fig.select(GlyphRenderer)
    lgd = fig.select(Legend)
    if len(gr) == 0:
        logger.warn("no glyph renderer defined for plot; aborting")
    j = 0
    for name, group in grouped:
        subfig = figure(title=name, **kwargs)
        for glyph, yy in zip(gr, y):
            plotfn = str(glyph.glyph).split(", ")[0].lower()
            kw = glyph.glyph.vm_props()
            kw.pop('x')
            kw.pop('y')
            source = ColumnDataSource(group)
            kw['legend'] = yy if len(lgd) > 0 else None
            getattr(subfig, plotfn)(x=x, y=yy, source=source, **kw)
        if j > 0:
            if share_x_range:
                subfig.x_range = flist[0].x_range
            if share_y_range:
                subfig.y_range = flist[0].y_range
        j = j + 1
        flist.append(subfig)
    return gridplot([flist[i:i+ncol] for i in range(0, len(flist), ncol)])
    
