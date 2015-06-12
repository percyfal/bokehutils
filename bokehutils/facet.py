# Copyright (C) 2015 by Per Unneberg
"""The facet functions emulate the behaviour found in ggplot. They
behave slightly differently from other bokehutils functions in that
they don't modify an existing plot; rather, the generate a series of
plots that are stitched together in a gridplot.
"""
from bokeh.plotting import figure, gridplot
from bokehutils.core import InspectArgs
from bokeh.models import ColumnDataSource
from bokeh.models.renderers import GlyphRenderer, Legend
import logging

logger = logging.getLogger(__name__)

@InspectArgs(allow_y_list=True)
def facet_grid(fig, x, y, df=None, source=None, groups=None, ncol=3,
               share_x_range=False, share_y_range=False, **kwargs):
    """facet_grid - generate a simple gridplot from a figure

    Args:
      fig ()
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
            if j > 0:
                if share_x_range:
                    kw['x_range'] = flist[0].x_range
                if share_y_range:
                    kw['y_range'] = flist[0].y_range
            getattr(subfig, plotfn)(x=x, y=yy, source=source, **kw)
        flist.append(subfig)
    # Could possibly use curdoc()._current_plot = gridplot()
    return gridplot([flist[i:i+ncol] for i in range(0, len(flist), ncol)])
